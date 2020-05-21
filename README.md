### Financial Data Scrapers

**Summary**: This project consists of two files for scraping financial data for particular companies from the US Electronic Data Gathering, Analysis, and Retrieval system (EDGAR), and the London Stock Exchange. 

**Task**: To create a web scraper capable of scraping the income statements of UK and US based companies active in the water sector. 

**Functionality**: The LSE scraper (Scraper.ipynb) parses a company's URL to Beautiful Soup. Once a soup object is rendered the page's HTML structure is used to pull out relevant data using tags and class names. This is then tidied up and displayed in a dataframe and exported to csv format. 

Searching data on the EDGAR site is a little more complicated and use is made of the download data links. These are navigated to by using Beautiful Soup to go to a company's EDGAR filings page, and then navigating to the data by grabbing links and parsing them to Beautiful Soup iteratively to navigate between pages. Once a link to the data is found it is downloaded in Excel format. The format is different for each company and but there are some keywords that can be used to sort the data. Currently this only works for pulling revenue data, however changes will be made to fix this. Now an API is available it may be easier and cleaner to use that. 

**Improvement**: To scrape multiple companies at once. For this I will collect CIK codes and tickers for various companies and use a loop to visit each companies stock exchange entry. As the EDGAR website is not friendly to crawlers, I will use the organisations API to get data on multiple companies.
