
# Phone Price Scraper - Price and Availability Scraper for TechnoLife and Digikala

Phone Price Scraper is a Python-based web scraping tool that helps users retrieve price and availability information for phone models from the TechnoLife and Digikala website. It uses Selenium for automated browser interactions, allowing users to gather data efficiently, even for phones that are out of stock or unavailable.

## Features

- **Phone Model Scraping:** Scrapes price and availability information for various phone models from TechnoLife & Digikala.
- **Error Handling:** Automatically detects missing or out-of-stock models and logs them for future reference.
- **Data Output:** Outputs relevant data, such as prices or stock status, in a user-friendly format.
- **Easy Customization:** Users can easily adjust scraping targets and error-handling processes.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Snipguy/phone_price_scraper.git
   cd phone_price_scraper
2. **Install the required dependencies: Make sure you have Python 3.x installed, then install the required libraries using pip:**
   ```bash
   pip install -r requirements.txt
3. **Install WebDriver: Download and install the appropriate WebDriver (e.g., ChromeDriver for Google Chrome):**
   [ChromeDriver Download](https://developer.chrome.com/docs/chromedriver/downloads)

## Usage

1. Edit the ```phone_models``` list in the script:
  Add or modify phone models you want to scrape within the ```main.py``` file.
2. Run the scraper
   ```bash
   python main.py
3. Interpreting the output:
  -  Phone models that are available will have their price listed.
  -  Models that are out of stock will be marked with ```**```.
  -  Errors during scraping will be marked with ```//``` in the output.

## Example Output

``` bash
  Phone: ModelX, Color Price, (Availability: In Stock )
  Phone: ModelY,  ** (Availability: Out Of Stock)
  Phone: ModelZ, Error: //
```

## Project Structure

``` plaintext
TechnoScraper/
│
├── main.py      # Main scraping script
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## Contributing

This is my first project, and I’m open to feedback, suggestions, and contributions! Feel free to fork the repository and submit pull requests.

## Contact

If you have any questions or are interested in collaborating, feel free to reach out:

- Email : snipguy.business@gmail.com
- Telegram : Babak4400

## Future Improvements

- Add support for scraping other electronic products.
- Implement a GUI for easier user interaction.
- Expand error handling and reporting mechanisms.

