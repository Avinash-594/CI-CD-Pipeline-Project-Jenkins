import requests
import csv
import json
from io import StringIO
from datetime import datetime

CSV_URL = "https://github.com/Avinash-594/pesticide-for-blackgram/blob/main/ferti.csv"
PRICE_LIMIT = 800

response = requests.get(CSV_URL)
response.raise_for_status()

reader = csv.DictReader(StringIO(response.text))

filtered = []
for row in reader:
    if float(row["price"]) <= PRICE_LIMIT:
        filtered.append(row)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = f"filtered_products_{timestamp}.json"

with open(output_file, "w") as f:
    json.dump(filtered, f, indent=4)

print(f"Saved file: {output_file}")
