# IR Crawler – Information Retrieval Project

This project implements a web crawler and information retrieval (IR) pipeline that collects web pages from a domain, builds an inverted index, and allows fast keyword-based retrieval of relevant pages.

**Role:** Contributor – implemented web crawling, text parsing, and inverted index construction.

---

## Problem Statement

Information retrieval is essential for search engines, QA systems, and NLP pipelines. Manually indexing web pages is time-consuming and error-prone, so this project automates the workflow:

- Crawl web pages starting from a seed URL
- Extract textual content from raw HTML
- Build an inverted index for keyword-based search

This allows users to quickly find relevant pages for a query without scanning all raw HTML files.

---

## Project Overview

### Web Crawling

- Starts from a seed page provided by the user
- Follows internal links to collect multiple pages within the same domain
- Downloads collected pages to the `CrawledPages/` folder

**Comment:** In the GitHub repo, these pages are saved as `.txt` files for convenience. In the real project, the original pages are HTML.

### Text Extraction & Preprocessing

- Strips HTML tags
- Cleans text: removes punctuation, converts to lowercase, and optionally tokenizes

**Comment:** This ensures that the inverted index contains clean, searchable text only.

### Inverted Index Construction

- Builds a JSON-based inverted index (`inverted_index.json`)
- Maps each keyword to a list of page IDs where it appears
- Supports efficient keyword-based lookup

### Search / Query (Optional)

- Allows users to query keywords against the inverted index
- Returns relevant pages or snippets

**Comment:** Useful for quick retrieval without scanning all page files.

---

## Dataset / Crawled Pages

- All downloaded pages are stored in the `CrawledPages` folder  
  Example: `CrawledPages/page1.txt`, `page2.txt`, etc.  
- Number of pages collected: 500  
- Inverted index file: `inverted_index.json`  

**Comment:** The GitHub version contains only a subset of the full index for easier sharing.

---

## Tech Stack

- **Python:** Core programming language  
- **Web Crawling:** `requests`, `BeautifulSoup`  
- **Text Processing:** `re`, `nltk` / `spaCy` (optional for tokenization)  
- **Data Storage:** JSON (inverted index)

---

## Installation & Usage

Step 1: Clone the repository
```bash
git clone https://github.com/Kalingu/ir-crawler.git
cd ir-crawler
```
Step 2: Clone the repository
```bash
pip install -r requirements.txt  
```
Step 3: Explore crawled pages
```bash
start CrawledPages\page1.txt
```
Step 4: Load and explore the inverted index
```bash
import json

with open("inverted_index.json", "r") as f:
    index = json.load(f)

# Example: print all pages containing the keyword "python"
print(index.get("python", []))
