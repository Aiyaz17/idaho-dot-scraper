# Web Scraping with Selenium

This code demonstrates web scraping using the Selenium library in Python. It scrapes data from a specific webpage and extracts information from individual pages.

## Installation

1. Clone the repository or download the code files.
2. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

   This will install Selenium and its required version specified in the `requirements.txt` file.

3. Download the appropriate Chrome WebDriver for your Chrome browser version from the following link: [Chrome WebDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads).

   - Ensure that the Chrome WebDriver executable is in your system's PATH.
   - Alternatively, you can place the Chrome WebDriver executable in the same directory as the code file.

## Usage

1. Open the code file `scraper.py` in a text editor.
2. Save the changes.
3. Execute the code by running the following command:

   ```
   python scraper.py
   ```

   The code will scrape the webpage, extract data from individual pages, and display the results in the console.

## Notes

- The code utilizes the headless mode of the Chrome browser, which means that the browser window will not be displayed during execution. If you want to see the browser window, you can remove the `headless` argument in the `chrome_options.add_argument()` line.
- Ensure that you have a stable internet connection to retrieve the webpage and its data.
