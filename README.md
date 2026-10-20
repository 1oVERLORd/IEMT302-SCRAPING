# IEMT302 - Web Scraping Experiment

This repository extracts local South African news headlines from `sanews.gov.za` using Python and BeautifulSoup (`bs4`).

## What I Learned From This Exercise
1. **HTTP Requests & Web Structure**: Learned how to fetch web page content using Python's `requests` library and parse HTML DOM trees using `BeautifulSoup`.
2. **Data Extraction & Storage**: Extracted targeted XML/HTML tags (`<div>`, `<a>`, `<span>`) and saved unstructured web text into a structured `.csv` format.
3. **Repository Best Practices**: Learned the importance of repository setup for automated testing, including:
   - Adding a shebang (`#!/usr/bin/env python3`) at line 1 to specify the execution environment.
   - Using a `.gitignore` file to prevent tracking virtual environments (`venv/`, `__pycache__/`).
   - Standardizing dependency installation via `requirements.txt`.

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run the script: `python scraper.py`
3. Scraped data will print to the terminal and save to `local_sa_news.csv`.