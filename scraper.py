import requests
import pandas as pd
import time

BASE_URL = "https://www.bevzilla.co"
PRODUCTS_JSON = "https://www.bevzilla.co/products.json"

headers = {
    "User-Agent": "Mozilla/5.0"
}

products = []
page = 1
LIMIT = 50          # Shopify max per page
MAX_PAGES = 5       # hard stop (interview safe)

print("🔍 Starting Bevzilla product scrape...")

while page <= MAX_PAGES:
    params = {
        "limit": LIMIT,
        "page": page
    }

    r = requests.get(PRODUCTS_JSON, headers=headers, params=params, timeout=10)
    data = r.json()

    items = data.get("products", [])
    if not items:
        print("⛔ No more products.")
        break

    print(f"📄 Page {page} → {len(items)} products")

    for item in items:
        name = item.get("title", "N/A")
        handle = item.get("handle", "")
        product_url = f"{BASE_URL}/products/{handle}"

        variants = item.get("variants", [])

        if variants:
            sale_price = variants[0].get("price", "N/A")
            original_price = variants[0].get("compare_at_price", "N/A")
            discount = "Yes" if original_price and original_price != sale_price else "No Discount"
        else:
            sale_price = "N/A"
            original_price = "N/A"
            discount = "No Discount"

        products.append({
            "Product Name": name,
            "Sale Price (₹)": sale_price,
            "Original Price (₹)": original_price,
            "Discount": discount,
            "Product URL": product_url
        })

    page += 1
    time.sleep(1)

df = pd.DataFrame(products).drop_duplicates()

# 🔥 RENAMED FILE HERE
df.to_csv("final_project.csv", index=False)

print(f"\n✅ DONE — Total products scraped: {len(df)}")
print("📁 Saved as final_project.csv")
