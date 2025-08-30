import asyncio
import json
import os
import time
from pathlib import Path
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode

async def scrape_single_wayback_page(url, output_dir="wayback_output"):
    """Scrape a single Wayback Machine page and extract all content"""
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Configure browser
    browser_config = BrowserConfig(
        browser_type="chromium",
        headless=True,
        verbose=True
    )
    
    # Configure crawling
    run_config = CrawlerRunConfig(
        verbose=True,
        cache_mode=CacheMode.ENABLED,
        word_count_threshold=0,
        page_timeout=30000,
        wait_for_images=True,
        screenshot=True,
        pdf=False,
        remove_overlay_elements=True,
        js_code=[
            "window.scrollTo(0, document.body.scrollHeight);",
            "await new Promise(resolve => setTimeout(resolve, 2000));"
        ]
    )
    
    print(f"Scraping: {url}")
    
    async with AsyncWebCrawler(config=browser_config) as crawler:
        try:
            result = await crawler.arun(url=url, config=run_config)
            
            if not result.success:
                print(f"Failed to scrape: {result.error_message}")
                return None
            
            # Extract all the content
            page_data = {
                "url": url,
                "original_url": url.replace("https://web.archive.org/web/20100423054747/", ""),
                "wayback_timestamp": "20100423054747",
                "title": result.metadata.get("title", "") if result.metadata else "",
                "status_code": result.status_code,
                "success": result.success,
                "scraped_at": time.time(),
                
                # Content in different formats
                "html": result.html,
                "cleaned_html": result.cleaned_html,
                "markdown": result.markdown.raw_markdown if hasattr(result.markdown, 'raw_markdown') else str(result.markdown),
                
                # Metadata and structure
                "metadata": result.metadata,
                "links": result.links,
                "media": result.media,
                
                # Additional data
                "network_requests": getattr(result, "network_requests", None),
                "console_messages": getattr(result, "console_messages", None)
            }
            
            # Save the complete data as JSON
            json_path = os.path.join(output_dir, "msdn_page_complete.json")
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(page_data, f, indent=2, ensure_ascii=False)
            
            # Save markdown separately for easy reading
            if page_data["markdown"]:
                md_path = os.path.join(output_dir, "msdn_page_content.md")
                with open(md_path, 'w', encoding='utf-8') as f:
                    f.write(page_data["markdown"])
            
            # Save cleaned HTML separately
            if page_data["cleaned_html"]:
                html_path = os.path.join(output_dir, "msdn_page_cleaned.html")
                with open(html_path, 'w', encoding='utf-8') as f:
                    f.write(page_data["cleaned_html"])
            
            # Save screenshot if available
            if hasattr(result, 'screenshot') and result.screenshot:
                import base64
                screenshot_path = os.path.join(output_dir, "msdn_page_screenshot.png")
                try:
                    with open(screenshot_path, "wb") as f:
                        f.write(base64.b64decode(result.screenshot))
                    page_data["screenshot_path"] = screenshot_path
                except Exception as e:
                    print(f"Could not save screenshot: {e}")
            
            # Extract and save key information
            summary = {
                "url": url,
                "title": page_data["title"],
                "word_count": len(page_data["markdown"].split()) if page_data["markdown"] else 0,
                "links_found": {
                    "internal": len(page_data["links"].get("internal", [])) if page_data["links"] else 0,
                    "external": len(page_data["links"].get("external", [])) if page_data["links"] else 0
                },
                "images_found": len(page_data["media"].get("images", [])) if page_data["media"] else 0,
                "scraped_successfully": True,
                "files_created": [
                    "msdn_page_complete.json",
                    "msdn_page_content.md",
                    "msdn_page_cleaned.html"
                ]
            }
            
            summary_path = os.path.join(output_dir, "scrape_summary.json")
            with open(summary_path, 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2, ensure_ascii=False)
            
            print(f"\n✅ Successfully scraped the page!")
            print(f"📁 Output directory: {os.path.abspath(output_dir)}")
            print(f"📄 Title: {page_data['title']}")
            print(f"📝 Word count: {summary['word_count']}")
            print(f"🔗 Links found: {summary['links_found']['internal']} internal, {summary['links_found']['external']} external")
            print(f"🖼️  Images found: {summary['images_found']}")
            
            return page_data
            
        except Exception as e:
            print(f"Error scraping {url}: {str(e)}")
            return None

async def main():
    url = "https://web.archive.org/web/20100423054747/http://msdn.microsoft.com:80/en-us/library/bb313877.aspx"
    
    print("🚀 Starting Wayback Machine scraper for MSDN page...")
    print(f"🎯 Target URL: {url}")
    
    result = await scrape_single_wayback_page(url, "msdn_wayback_scrape")
    
    if result:
        print("\n🎉 Scraping completed successfully!")
        print("📂 Check the 'msdn_wayback_scrape' folder for all extracted content.")
    else:
        print("\n❌ Scraping failed. Check the error messages above.")

if __name__ == "__main__":
    asyncio.run(main())