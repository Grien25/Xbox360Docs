import asyncio
import json
import os
import time
import hashlib
import re
from pathlib import Path
from urllib.parse import urlparse
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode

class DeepWaybackScraper:
    def __init__(self, output_dir="deep_wayback_scrape"):
        self.output_dir = output_dir
        self.visited_urls = set()
        self.scraped_pages = []
        
        # Create output directories
        os.makedirs(output_dir, exist_ok=True)
        os.makedirs(os.path.join(output_dir, "pages"), exist_ok=True)
        os.makedirs(os.path.join(output_dir, "instructions"), exist_ok=True)
        
    def safe_filename(self, url):
        """Create a safe filename from URL"""
        # Extract meaningful part from the URL
        if "bb313" in url:
            # Extract the bb number
            parts = url.split("/")
            for part in parts:
                if part.startswith("bb") and part.endswith(".aspx"):
                    return part.replace(".aspx", "")
        
        # Fallback to hash
        return hashlib.md5(url.encode()).hexdigest()[:12]
    
    def extract_all_instruction_links(self, page_data):
        """Extract all instruction-related links from a page"""
        instruction_links = []
        
        if page_data.get("links") and page_data["links"].get("internal"):
            for link in page_data["links"]["internal"]:
                href = link.get("href", "")
                text = link.get("text", "")
                
                # Look for instruction pages (bb313xxx series beyond our main ones)
                if ("bb313956" in href or  # tfetch1D
                    "bb313957" in href or  # tfetch2D
                    "bb313958" in href or  # tfetch3D
                    "bb313959" in href or  # tfetchCube
                    "bb313916" in href or  # Vector ALU Instructions
                    "bb313" in href):      # Any other bb313xxx pages
                    
                    # Skip the ones we already have
                    if not any(x in href for x in ["bb313871", "bb313874", "bb313873", "bb313962", "bb313961", "bb313877"]):
                        instruction_links.append({
                            "url": href,
                            "title": text,
                            "filename": self.safe_filename(href)
                        })
        
        return instruction_links
    
    def extract_additional_links_from_content(self, content):
        """Extract additional bb313xxx links from markdown content"""
        additional_links = []
        
        # Look for bb313xxx patterns in the content
        bb_pattern = r'bb313(\d+)\.aspx'
        matches = re.findall(bb_pattern, content)
        
        for match in matches:
            bb_id = f"bb313{match}"
            # Skip ones we already have
            if bb_id not in ["bb313871", "bb313874", "bb313873", "bb313962", "bb313961", "bb313877"]:
                # Construct the wayback URL
                wayback_url = f"https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/{bb_id}.aspx"
                additional_links.append({
                    "url": wayback_url,
                    "title": f"Instruction Page {bb_id}",
                    "filename": bb_id
                })
        
        return additional_links
    
    async def scrape_single_page(self, crawler, url, title="", category="page"):
        """Scrape a single page and return the data"""
        if url in self.visited_urls:
            return None
            
        self.visited_urls.add(url)
        print(f"🔍 Scraping {category}: {title or 'Page'}")
        print(f"   URL: {url}")
        
        try:
            run_config = CrawlerRunConfig(
                verbose=False,
                cache_mode=CacheMode.ENABLED,
                word_count_threshold=0,
                page_timeout=30000,
                wait_for_images=False,
                screenshot=False,
                pdf=False,
                remove_overlay_elements=True,
                js_code=["window.scrollTo(0, document.body.scrollHeight);"]
            )
            
            result = await crawler.arun(url=url, config=run_config)
            
            if not result.success:
                print(f"   ❌ Failed: {result.error_message}")
                return None
            
            # Extract content
            page_data = {
                "url": url,
                "original_url": url.replace("https://web.archive.org/web/20100423054747/", "").replace("https://web.archive.org/web/20100429090724/", ""),
                "title": result.metadata.get("title", title) if result.metadata else title,
                "status_code": result.status_code,
                "success": result.success,
                "scraped_at": time.time(),
                "category": category,
                
                # Content
                "html": result.html,
                "cleaned_html": result.cleaned_html,
                "markdown": result.markdown.raw_markdown if hasattr(result.markdown, 'raw_markdown') else str(result.markdown),
                
                # Metadata
                "metadata": result.metadata,
                "links": result.links,
                "media": result.media,
                "word_count": len(result.markdown.raw_markdown.split()) if hasattr(result.markdown, 'raw_markdown') else 0
            }
            
            print(f"   ✅ Success: {page_data['word_count']} words")
            return page_data
            
        except Exception as e:
            print(f"   ❌ Error: {str(e)}")
            return None
    
    async def scrape_deep_documentation(self, main_url):
        """Scrape the main page, sections, and all instruction pages"""
        
        browser_config = BrowserConfig(
            browser_type="chromium",
            headless=True,
            verbose=False
        )
        
        async with AsyncWebCrawler(config=browser_config) as crawler:
            
            print("🚀 Starting DEEP Wayback Machine scraper...")
            print(f"📄 Main page: {main_url}")
            
            # Phase 1: Scrape main page
            main_page = await self.scrape_single_page(crawler, main_url, "Main Page", "main")
            if not main_page:
                print("❌ Failed to scrape main page")
                return
            
            self.scraped_pages.append(main_page)
            
            # Phase 2: Scrape main sections
            section_links = [
                {"url": "https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313871.aspx", "title": "Inline Microcode Assembly", "filename": "bb313871"},
                {"url": "https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313874.aspx", "title": "Vertex Fetching", "filename": "bb313874"},
                {"url": "https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313873.aspx", "title": "Texture Fetching", "filename": "bb313873"},
                {"url": "https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313962.aspx", "title": "Swizzling", "filename": "bb313962"},
                {"url": "https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313961.aspx", "title": "Microcode Instructions", "filename": "bb313961"}
            ]
            
            print(f"\n📚 Scraping {len(section_links)} main sections...")
            
            all_instruction_links = set()
            
            for i, link in enumerate(section_links, 1):
                print(f"\n[{i}/{len(section_links)}]", end=" ")
                
                if i > 1:
                    await asyncio.sleep(1.5)
                
                page_data = await self.scrape_single_page(
                    crawler, 
                    link["url"], 
                    link["title"],
                    "section"
                )
                
                if page_data:
                    self.scraped_pages.append(page_data)
                    
                    # Extract instruction links from this page
                    instruction_links = self.extract_all_instruction_links(page_data)
                    additional_links = self.extract_additional_links_from_content(page_data.get("markdown", ""))
                    
                    for inst_link in instruction_links + additional_links:
                        all_instruction_links.add((inst_link["url"], inst_link["title"], inst_link["filename"]))
            
            # Phase 3: Scrape instruction pages
            instruction_list = list(all_instruction_links)
            
            if instruction_list:
                print(f"\n🔧 Found {len(instruction_list)} instruction pages to scrape:")
                for _, title, _ in instruction_list:
                    print(f"   • {title}")
                
                print(f"\n📖 Scraping instruction pages...")
                
                for i, (url, title, filename) in enumerate(instruction_list, 1):
                    print(f"\n[{i}/{len(instruction_list)}]", end=" ")
                    
                    if i > 1:
                        await asyncio.sleep(2.0)  # Longer delay for instruction pages
                    
                    page_data = await self.scrape_single_page(
                        crawler, 
                        url, 
                        title,
                        "instruction"
                    )
                    
                    if page_data:
                        self.scraped_pages.append(page_data)
                        
                        # Save to instructions folder
                        inst_path = os.path.join(self.output_dir, "instructions", f"{filename}.json")
                        with open(inst_path, 'w', encoding='utf-8') as f:
                            json.dump(page_data, f, indent=2, ensure_ascii=False)
                        
                        # Save markdown
                        if page_data["markdown"]:
                            md_path = os.path.join(self.output_dir, "instructions", f"{filename}.md")
                            with open(md_path, 'w', encoding='utf-8') as f:
                                f.write(f"# {page_data['title']}\n\n")
                                f.write(f"**Source:** {page_data['original_url']}\n\n")
                                f.write(page_data["markdown"])
            
            # Save all main pages
            for page in self.scraped_pages:
                if page.get("category") in ["main", "section"]:
                    filename = self.safe_filename(page.get("url", ""))
                    if page.get("category") == "main":
                        filename += "_main"
                    
                    page_path = os.path.join(self.output_dir, "pages", f"{filename}.json")
                    with open(page_path, 'w', encoding='utf-8') as f:
                        json.dump(page, f, indent=2, ensure_ascii=False)
                    
                    if page["markdown"]:
                        md_path = os.path.join(self.output_dir, "pages", f"{filename}.md")
                        with open(md_path, 'w', encoding='utf-8') as f:
                            f.write(f"# {page['title']}\n\n")
                            f.write(f"**Source:** {page['original_url']}\n\n")
                            f.write(page["markdown"])
            
            # Create comprehensive summary
            await self.create_comprehensive_summary()
    
    async def create_comprehensive_summary(self):
        """Create a comprehensive summary of all scraped content"""
        
        total_words = sum(page.get("word_count", 0) for page in self.scraped_pages)
        
        # Categorize pages
        main_pages = [p for p in self.scraped_pages if p.get("category") == "main"]
        section_pages = [p for p in self.scraped_pages if p.get("category") == "section"]
        instruction_pages = [p for p in self.scraped_pages if p.get("category") == "instruction"]
        
        summary = {
            "scrape_info": {
                "total_pages_scraped": len(self.scraped_pages),
                "main_pages": len(main_pages),
                "section_pages": len(section_pages),
                "instruction_pages": len(instruction_pages),
                "total_word_count": total_words,
                "scrape_completed_at": time.time(),
                "wayback_timestamp": "20100423054747"
            },
            "pages_by_category": {
                "main": [{"title": p.get("title", ""), "word_count": p.get("word_count", 0)} for p in main_pages],
                "sections": [{"title": p.get("title", ""), "word_count": p.get("word_count", 0)} for p in section_pages],
                "instructions": [{"title": p.get("title", ""), "word_count": p.get("word_count", 0)} for p in instruction_pages]
            }
        }
        
        # Save summary
        summary_path = os.path.join(self.output_dir, "deep_scrape_summary.json")
        with open(summary_path, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
        
        # Create a mega combined markdown file
        combined_md_path = os.path.join(self.output_dir, "complete_documentation.md")
        with open(combined_md_path, 'w', encoding='utf-8') as f:
            f.write("# XNA Game Studio 3.1 - Complete Microcode Documentation\n\n")
            f.write("**Complete documentation scraped from MSDN Wayback Machine (Deep Crawl)**\n\n")
            f.write(f"**Scrape Date:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"**Total Pages:** {len(self.scraped_pages)}\n")
            f.write(f"**Total Words:** {total_words:,}\n\n")
            
            f.write("## Content Overview\n\n")
            f.write(f"- **Main Pages:** {len(main_pages)}\n")
            f.write(f"- **Section Pages:** {len(section_pages)}\n")
            f.write(f"- **Instruction Pages:** {len(instruction_pages)}\n\n")
            f.write("---\n\n")
            
            # Write main page
            f.write("# PART I: MAIN DOCUMENTATION\n\n")
            for page in main_pages + section_pages:
                f.write(f"## {page.get('title', 'Untitled')}\n\n")
                f.write(f"**Source:** {page.get('original_url', '')}\n")
                f.write(f"**Word Count:** {page.get('word_count', 0)}\n\n")
                if page.get("markdown"):
                    content = page["markdown"]
                    if content.startswith("The Wayback Machine"):
                        lines = content.split('\n')
                        content = '\n'.join(lines[1:])
                    f.write(content)
                f.write("\n\n---\n\n")
            
            # Write instruction pages
            if instruction_pages:
                f.write("# PART II: INSTRUCTION REFERENCE\n\n")
                for page in instruction_pages:
                    f.write(f"## {page.get('title', 'Untitled')}\n\n")
                    f.write(f"**Source:** {page.get('original_url', '')}\n")
                    f.write(f"**Word Count:** {page.get('word_count', 0)}\n\n")
                    if page.get("markdown"):
                        content = page["markdown"]
                        if content.startswith("The Wayback Machine"):
                            lines = content.split('\n')
                            content = '\n'.join(lines[1:])
                        f.write(content)
                    f.write("\n\n---\n\n")
        
        print(f"\n🎉 DEEP SCRAPING COMPLETED!")
        print(f"📊 Final Summary:")
        print(f"   • Total pages scraped: {len(self.scraped_pages)}")
        print(f"   • Main pages: {len(main_pages)}")
        print(f"   • Section pages: {len(section_pages)}")
        print(f"   • Instruction pages: {len(instruction_pages)}")
        print(f"   • Total word count: {total_words:,}")
        print(f"   • Output directory: {os.path.abspath(self.output_dir)}")
        print(f"   • Complete documentation: complete_documentation.md")
        print(f"   • Main pages: pages/ folder")
        print(f"   • Instruction pages: instructions/ folder")

async def main():
    main_url = "https://web.archive.org/web/20100423054747/http://msdn.microsoft.com:80/en-us/library/bb313877.aspx"
    
    scraper = DeepWaybackScraper("msdn_deep_scrape")
    await scraper.scrape_deep_documentation(main_url)

if __name__ == "__main__":
    asyncio.run(main())