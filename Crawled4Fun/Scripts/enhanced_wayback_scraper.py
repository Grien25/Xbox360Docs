import asyncio
import json
import os
import time
import hashlib
from pathlib import Path
from urllib.parse import urlparse
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode

class EnhancedWaybackScraper:
    def __init__(self, output_dir="enhanced_wayback_scrape"):
        self.output_dir = output_dir
        self.visited_urls = set()
        self.scraped_pages = []
        
        # Create output directories
        os.makedirs(output_dir, exist_ok=True)
        os.makedirs(os.path.join(output_dir, "pages"), exist_ok=True)
        
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
    
    def extract_section_links(self, page_data):
        """Extract the main section links from the scraped page"""
        section_links = []
        
        if page_data.get("links") and page_data["links"].get("internal"):
            for link in page_data["links"]["internal"]:
                href = link.get("href", "")
                text = link.get("text", "")
                
                # Focus on the main documentation links (bb313xxx series)
                if ("bb313871" in href or  # Inline Microcode Assembly
                    "bb313874" in href or  # Vertex Fetching
                    "bb313873" in href or  # Texture Fetching
                    "bb313962" in href or  # Source Register Swizzling
                    "bb313961" in href):   # Microcode Instructions
                    
                    section_links.append({
                        "url": href,
                        "title": text,
                        "filename": self.safe_filename(href)
                    })
        
        return section_links
    
    async def scrape_single_page(self, crawler, url, title=""):
        """Scrape a single page and return the data"""
        if url in self.visited_urls:
            return None
            
        self.visited_urls.add(url)
        print(f"🔍 Scraping: {title or 'Page'}")
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
                "original_url": url.replace("https://web.archive.org/web/20100423054747/", ""),
                "title": result.metadata.get("title", title) if result.metadata else title,
                "status_code": result.status_code,
                "success": result.success,
                "scraped_at": time.time(),
                
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
    
    async def scrape_main_page_and_sections(self, main_url):
        """Scrape the main page and all its section links"""
        
        browser_config = BrowserConfig(
            browser_type="chromium",
            headless=True,
            verbose=False
        )
        
        async with AsyncWebCrawler(config=browser_config) as crawler:
            
            # First, scrape the main page
            print("🚀 Starting enhanced Wayback Machine scraper...")
            print(f"📄 Main page: {main_url}")
            
            main_page = await self.scrape_single_page(crawler, main_url, "Main Page")
            
            if not main_page:
                print("❌ Failed to scrape main page")
                return
            
            self.scraped_pages.append(main_page)
            
            # Extract section links
            section_links = self.extract_section_links(main_page)
            print(f"\n🔗 Found {len(section_links)} section links to scrape:")
            
            for link in section_links:
                print(f"   • {link['title']}")
            
            # Scrape each section
            print(f"\n📚 Scraping sections...")
            
            for i, link in enumerate(section_links, 1):
                print(f"\n[{i}/{len(section_links)}]", end=" ")
                
                # Add delay between requests
                if i > 1:
                    await asyncio.sleep(1.5)
                
                page_data = await self.scrape_single_page(
                    crawler, 
                    link["url"], 
                    link["title"]
                )
                
                if page_data:
                    self.scraped_pages.append(page_data)
                    
                    # Save individual page
                    filename = link["filename"]
                    page_path = os.path.join(self.output_dir, "pages", f"{filename}.json")
                    
                    with open(page_path, 'w', encoding='utf-8') as f:
                        json.dump(page_data, f, indent=2, ensure_ascii=False)
                    
                    # Save markdown
                    if page_data["markdown"]:
                        md_path = os.path.join(self.output_dir, "pages", f"{filename}.md")
                        with open(md_path, 'w', encoding='utf-8') as f:
                            f.write(f"# {page_data['title']}\n\n")
                            f.write(f"**Source:** {page_data['original_url']}\n\n")
                            f.write(page_data["markdown"])
            
            # Save main page separately
            main_filename = self.safe_filename(main_url)
            main_path = os.path.join(self.output_dir, "pages", f"{main_filename}_main.json")
            with open(main_path, 'w', encoding='utf-8') as f:
                json.dump(main_page, f, indent=2, ensure_ascii=False)
            
            if main_page["markdown"]:
                main_md_path = os.path.join(self.output_dir, "pages", f"{main_filename}_main.md")
                with open(main_md_path, 'w', encoding='utf-8') as f:
                    f.write(f"# {main_page['title']}\n\n")
                    f.write(f"**Source:** {main_page['original_url']}\n\n")
                    f.write(main_page["markdown"])
            
            # Create comprehensive summary
            await self.create_comprehensive_summary()
    
    async def create_comprehensive_summary(self):
        """Create a comprehensive summary of all scraped content"""
        
        total_words = sum(page.get("word_count", 0) for page in self.scraped_pages)
        
        summary = {
            "scrape_info": {
                "total_pages_scraped": len(self.scraped_pages),
                "total_word_count": total_words,
                "scrape_completed_at": time.time(),
                "wayback_timestamp": "20100423054747"
            },
            "pages": []
        }
        
        # Add page summaries
        for page in self.scraped_pages:
            page_summary = {
                "title": page.get("title", ""),
                "original_url": page.get("original_url", ""),
                "word_count": page.get("word_count", 0),
                "success": page.get("success", False),
                "filename": self.safe_filename(page.get("url", ""))
            }
            summary["pages"].append(page_summary)
        
        # Save summary
        summary_path = os.path.join(self.output_dir, "comprehensive_summary.json")
        with open(summary_path, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
        
        # Create a combined markdown file with all content
        combined_md_path = os.path.join(self.output_dir, "all_content_combined.md")
        with open(combined_md_path, 'w', encoding='utf-8') as f:
            f.write("# XNA Game Studio 3.1 - Microcode Documentation\n\n")
            f.write("**Complete documentation scraped from MSDN Wayback Machine**\n\n")
            f.write(f"**Scrape Date:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"**Total Pages:** {len(self.scraped_pages)}\n")
            f.write(f"**Total Words:** {total_words:,}\n\n")
            f.write("---\n\n")
            
            for i, page in enumerate(self.scraped_pages, 1):
                f.write(f"## {i}. {page.get('title', 'Untitled')}\n\n")
                f.write(f"**Source:** {page.get('original_url', '')}\n\n")
                if page.get("markdown"):
                    # Clean up the markdown (remove wayback header)
                    content = page["markdown"]
                    if content.startswith("The Wayback Machine"):
                        lines = content.split('\n')
                        # Skip the first line (wayback header)
                        content = '\n'.join(lines[1:])
                    f.write(content)
                f.write("\n\n---\n\n")
        
        print(f"\n🎉 Scraping completed successfully!")
        print(f"📊 Summary:")
        print(f"   • Total pages scraped: {len(self.scraped_pages)}")
        print(f"   • Total word count: {total_words:,}")
        print(f"   • Output directory: {os.path.abspath(self.output_dir)}")
        print(f"   • Combined content: all_content_combined.md")
        print(f"   • Individual pages: pages/ folder")

async def main():
    main_url = "https://web.archive.org/web/20100423054747/http://msdn.microsoft.com:80/en-us/library/bb313877.aspx"
    
    scraper = EnhancedWaybackScraper("msdn_complete_scrape")
    await scraper.scrape_main_page_and_sections(main_url)

if __name__ == "__main__":
    asyncio.run(main())