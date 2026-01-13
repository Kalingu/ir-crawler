#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import os
import time

# ------------------ STEP 1: SETUP ------------------
# Starting point (seed page)
seed_url = "https://www.wired.com"

# Folder to store downloaded pages
folder = r"C:\Users\User\Desktop\NIBM year 2\7. Information retrival and analytics\ir projects\Project 01\CrawledPages"
os.makedirs(folder, exist_ok=True)  # Create the folder if it doesn’t exist

# Initialize variables
visited = set()      # To avoid visiting the same page twice
queue = [seed_url]   # Pages to crawl (starts with the seed page)
page_limit = 500     # Crawl up to 500 pages

# ------------------ STEP 2: MAIN LOOP ------------------
while queue and len(visited) < page_limit:
    url = queue.pop(0)           # Get next URL from the queue
    if url in visited:
        continue                 # Skip if already visited

    try:
        # STEP 2.1: Download the page
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise an error for bad responses
        html = response.text

        # STEP 2.2: Save the page locally
        page_number = len(visited) + 1
        filename = f"page{page_number:03}kalingu.txt"
        filepath = os.path.join(folder, filename)

        with open(filepath, "w", encoding="utf-8") as file:
            file.write(html)

        visited.add(url)  # Mark page as visited

        # STEP 2.3: Extract new links
        soup = BeautifulSoup(html, "html.parser")
        for link in soup.find_all("a", href=True):
            href = link["href"]
            if href.startswith("http") and href not in visited:
                queue.append(href)

        # STEP 2.4: Pause between requests
        time.sleep(1)

        print(f"Crawled: {url} | Total pages: {len(visited)}")

    except Exception as e:
        # Handles network errors or invalid links
        print(f"Failed to fetch {url}: {e}")

# ------------------ STEP 3: FINISH ------------------
print("Crawling completed.")


# In[2]:


import os
import re
import json
import nltk
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# ---------------- STEP 1: SETUP ----------------
nltk.download('punkt')
ps = PorterStemmer()

# Folder with crawled .txt files
folder = r"C:\Users\User\Desktop\NIBM year 2\7. Information retrival and analytics\ir projects\Project 01\CrawledPages"
files = sorted([f for f in os.listdir(folder) if f.endswith(".txt")])
print(f"Found {len(files)} documents to index.")

# Dictionary to store the inverted index
inverted_index = {}

# ---------------- STEP 2: PROCESS EACH FILE ----------------
for doc_id, file_name in enumerate(files, start=1):
    try:
        # Read file content
        with open(os.path.join(folder, file_name), "r", encoding="utf-8", errors="ignore") as f:
            html = f.read()

        # Extract text from HTML
        text = BeautifulSoup(html, "html.parser").get_text(" ")

        # Clean and tokenize text
        text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
        tokens = word_tokenize(text)

        # Lowercase + stemming
        tokens = [ps.stem(t.lower()) for t in tokens if t.isalnum()]

        # Build inverted index (word → document list)
        for token in tokens:
            inverted_index.setdefault(token, []).append(doc_id)

    except Exception as e:
        print(f"Skipping {file_name}: {e}")

# ---------------- STEP 3: SAVE OUTPUT ----------------
output_path = r"C:\Users\User\Desktop\NIBM year 2\7. Information retrival and analytics\ir projects\Project 01\inverted_index.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(inverted_index, f, indent=4)

print(f"✅ Inverted index created with {len(inverted_index)} unique terms.")
print(f"Saved to: {output_path}")


# In[3]:


# ---------------- STEP 6: SEARCH EXAMPLE ----------------
search_word = "grosse"  # Example search term
stem = ps.stem(search_word.lower())  # Convert to lowercase and stem

if stem in inverted_index:
    print(f"✅ '{search_word}' found in documents: {inverted_index[stem]}")
else:
    print(f"❌ '{search_word}' not found in any document.")


# In[ ]:




