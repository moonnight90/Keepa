# Keepa Product Data Scraper

## Description
This script is designed to scrape product information from Keepa using their WebSocket API. It retrieves data such as product title, ASIN, EAN, price, condition, Bookscouter price, price difference, percentage difference, Amazon link, and last fresh date and time. The scraped data is then saved into a CSV file named `Products.csv`.

## Prerequisites
Before running the script, make sure you have Python installed on your system. Additionally, ensure you have the required Python packages installed. You can install them using `pip`:

```bash
pip install -r requirements.txt
```

## Usage
1. Clone the repository or download the script file.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Run the script using Python:

```bash
python main.py
```

5. Follow the prompts to provide your Keepa username/email and password when requested.
6. The script will start scraping product information from Keepa.

## Important Notes
- This script requires valid credentials (username/email and password) to access Keepa's data through their API.
- Ensure you have a stable internet connection while running the script.
- Keepa's terms of service apply when using their API. Make sure you comply with their terms and conditions.
- The scraped data is saved into a file named `Products.csv` in the same directory as the script. Make sure you have write permissions for the directory.
- This script is provided as-is and may require further customization or maintenance depending on your specific use case or changes in Keepa's API.