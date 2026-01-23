# IR Crawler – Information Retrieval Project

This project implements a **web crawler and information retrieval (IR) pipeline** that collects web pages from a domain, builds an **inverted index**, and allows fast retrieval of relevant pages based on search queries.

*Role:* Contributor – implemented web crawling, text parsing, and inverted index construction.

---

## Problem Statement

Information retrieval is essential for search engines, QA systems, and NLP pipelines. Manually indexing web pages is infeasible, so this project automates:

- Crawling web pages from a seed URL  
- Extracting textual content  
- Building an inverted index for keyword-based retrieval

This helps in quickly finding relevant pages for a given query without scanning all raw HTML files.

---

## Project Overview

1. **Web Crawling**  
   - Starts from a seed page  
   - Follows internal links to collect multiple pages from the same domain  
   - Downloads pages to `CrawledPages/`

2. **Text Extraction & Preprocessing**  
   - Strips HTML tags  
   - Cleans text (removes punctuation, lowercasing, tokenization)

3. **Inverted Index Construction**  
   - Builds a JSON-based inverted index (`inverted_index.json`)  
   - Maps keywords → list of page IDs where they appear  
   - Supports efficient keyword search

4. **Search / Query** *(Optional if implemented)*  
   - Allows keyword-based lookup using the inverted index  
   - Returns relevant pages or snippets

---

## Dataset / Crawled Pages

- All downloaded pages are stored in the `CrawledPages` folder:  
  [Browse CrawledPages](https://github.com/Kalingu/ir-crawler/tree/main/CrawledPages)  
- Example: `CrawledPages/page1.html`, `page2.html`, etc.  
- Number of pages collected: 500  
- Inverted index file: `inverted_index.json`

---

## Tech Stack

- **Python:** Core language  
- **Web Crawling:** `requests`, `BeautifulSoup`  
- **Text Processing:** `re`, `nltk` / `spaCy` (optional)  
- **Data Storage:** JSON (inverted index)  
- **Optional Visualization / Search:** Jupyter Notebook

---

## Installation & Usage

Step 1: Clone the repository
```bash
git clone https://github.com/Kalingu/ir-crawler.git
cd ir-crawler
