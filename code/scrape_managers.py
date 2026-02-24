
import pandas as pd
import requests
import os

# Scrape the Wikipedia page for Manchester United managers
url = "https://en.wikipedia.org/wiki/List_of_Manchester_United_F.C._managers"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
response = requests.get(url, headers=headers)
response.raise_for_status()
html = response.text

tables = pd.read_html(html)

# Find the largest wikitable (should be the managers table)
managers_table = max(tables, key=lambda df: df.shape[0])

# Save to CSV
output_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
os.makedirs(output_dir, exist_ok=True)
csv_path = os.path.join(output_dir, 'managers.csv')
managers_table.to_csv(csv_path, index=False)
print(f"Saved table to {csv_path}")
