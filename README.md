# Free-News-Aggregator

This Python script scrapes trusted, free news websites for articles based on a keyword search. The results are returned in a JSON file, providing article title, article URL, article date, article source, and article text. The script supports multiple news websites, including NPR, USA Today, Reuters, The Hill, Time, and BBC.

## Prerequisites

To run this script, you need to have the following installed:

- Python 3
- Requests library (`requests`)
- BeautifulSoup library (`beautifulsoup4`)
- Selenium library (`selenium`)
- Chrome WebDriver (for Selenium) - Download from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and ensure it is in your system PATH.

To install the dependencies, run the following command:

pip install -r requirements.txt

Make sure you have pip installed and the requirements.txt file is in the same directory as the script.

## Usage

The script provides a function called `news_scrape` which takes a keyword string as input. It performs the news search and generates a JSON file with the search results.

To use the script, follow these steps:

1. Ensure you have met the prerequisites mentioned above.
2. Open the Python file containing the code.
3. Modify the last line of the file to specify the keyword you want to search for. For example: `news_scrape('cars')`.
4. Run the Python script.

After execution, the script will print status messages indicating the progress of the news search. Once completed, a file named `news_search.json` will be generated in the same directory, containing the search results.

## Function Details

The script includes several functions that perform the news search on different websites. Each website has a specific function dedicated to it:

- `npr_search`: Searches NPR for articles with the given keyword.
- `usatoday_search`: Searches USA Today for articles with the given keyword.
- `reuters_search`: Searches Reuters for articles with the given keyword.
- `thehill_search`: Searches The Hill for articles with the given keyword.
- `time_search`: Searches Time for articles with the given keyword.
- `bbc_search`: Searches BBC for articles with the given keyword.

These functions return a list of dictionaries, with each dictionary representing an article found in the search. The dictionaries include the following information:

- `title`: The title of the article.
- `url`: The URL of the article.
- `date`: The date of the article (if available).
- `source`: The news source (e.g., NPR, USA Today).
- `text`: The text content of the article (if available).

The main function, `news_scrape`, orchestrates the overall news search process. It calls each news search function with the provided keyword, aggregates the results, and stores them in a JSON file.

Feel free to modify the code or customize the scraping process to fit your specific needs.

**Note:** Please ensure that you use this script responsibly and respect the terms of service of the websites you are scraping.
