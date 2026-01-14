Bevzilla Product Web Scraper
📌 Overview
This repository contains a Python-based web scraping project that extracts structured product data from Bevzilla, an e-commerce platform built on Shopify.
The scraper is designed to collect key product attributes such as pricing, discounts, and product URLs, and store them in a clean, analysis-ready CSV format.
This project demonstrates practical skills in web scraping, API-based data extraction, pagination handling, and data cleaning.
 
🎯 Project Objectives
•	Independently identify relevant product data to scrape
•	Handle pagination across multiple product pages
•	Extract pricing and discount information
•	Convert unstructured web data into structured datasets
•	Ensure scraping is efficient, controlled, and interview-safe
 
🛠️ Technologies Used
•	Python 3
•	Requests – for HTTP API requests
•	Pandas – for data processing and CSV export
•	Shopify Public JSON API
 
📊 Data Collected
The scraper extracts the following fields:
Field	Description
Product Name	Name of the product
Sale Price (₹)	Current selling price
Original Price (₹)	MRP / compare-at price
Discount	Indicates whether a discount is available
Product URL	Direct link to the product page
 
🔍 Scraping Approach
•	Uses Shopify’s publicly available endpoint:
•	https://www.bevzilla.co/products.json
•	Fetches products in batches of 50 per page
•	Implements a page limit to avoid infinite scraping
•	Detects discounts by comparing sale price and original price
•	Cleans and deduplicates the dataset before export
 
📂 Project Structure
├── scraper.py
├── requirements.txt
├── final_project.csv
└── README.md
 
▶️ How to Run
1.	Install dependencies:
2.	python3 -m pip install -r requirements.txt
3.	Run the scraper:
4.	python3 scraper.py
5.	Output:
o	A CSV file named final_project.csv will be generated.
 
⚠️ Notes
•	Product ratings are not available through Shopify’s public API and are therefore excluded.
•	Pricing is extracted from the first available product variant.
•	The script includes delays and page limits to ensure responsible scraping.
 
🚀 Key Learnings
•	API-based scraping is more reliable than HTML parsing
•	Pagination handling is critical for large datasets
•	Clean data structures simplify downstream analysis
•	Responsible scraping prevents infinite loops and overload
