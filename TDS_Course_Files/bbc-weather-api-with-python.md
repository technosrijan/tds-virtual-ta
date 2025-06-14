## BBC Weather location ID with Python

[](https://youtu.be/IafLrvnamAw)

You'll learn how to get the location ID of any city from the BBC Weather API -- as a precursor to scraping weather data -- covering:

- **Understanding API Calls**: Learn how backend API calls work when searching for a city on the BBC weather website.
- **Inspecting Web Interactions**: Use the browser's inspect element feature to track API calls and understand the network activity.
- **Extracting Location IDs**: Identify and extract the location ID from the API response using Python.
- **Using Python Libraries**: Import and use requests, json, and urlencode libraries to make API calls and process responses.
- **Constructing API URLs**: Create structured API URLs dynamically with constant prefixes and query parameters using urlencode.
- **Building Functions**: Develop a Python function that accepts a city name, constructs the API call, and returns the location ID.

To open the browser Developer Tools on Chrome, Edge, or Firefox, you can:

- Right-click on the page and select "Inspect" to open the developer tools
- OR: Press `F12`
- OR: Press `Ctrl+Shift+I` on Windows
- OR: Press `Cmd+Opt+I` on Mac

Here are links and references:

- BBC Location ID scraping - Notebook
- BBC Weather - Palo Alto (location ID: 5380748)
- BBC Locator Service - Los Angeles
- Learn about the `requests` package. Watch Python Requests Tutorial: Request Web Pages, Download Images, POST Data, Read JSON, and More

## BBC Weather data with Python

[](https://youtu.be/Uc4DgQJDRoI)

You'll learn how to scrape the live weather data of a city from the BBC Weather API, covering:

- **Introduction to Web Scraping**: Understand the basics of web scraping and its legality.
- **Libraries Overview**: Learn the importance of `requests` and `BeautifulSoup`.
- **Fetching HTML**: Use `requests` to fetch HTML content from a web page.
- **Parsing HTML**: Utilize `BeautifulSoup` to parse and navigate the HTML content.
- **Identifying Data**: Inspect HTML elements to locate specific data (e.g., high and low temperatures).
- **Extracting Data**: Extract relevant data using `BeautifulSoup`'s `find_all()` function.
- **Data Cleanup**: Clean extracted data to remove unwanted elements.
- **Post-Processing**: Use regular expressions to split large strings into meaningful parts.
- **Data Structuring**: Combine extracted data into a structured pandas DataFrame.
- **Handling Special Characters**: Replace unwanted characters for better data manipulation.
- **Saving Data**: Save the cleaned data into CSV and Excel formats.

Here are links and references:

- BBC Weather scraping - Notebook
- BBC Locator Service - Mumbai
- BBC Weather - Mumbai (location ID: 1275339)
- BBC Weather API - Mumbai (location ID: 1275339)
- Learn about the `json` package. Watch Python Tutorial: Working with JSON Data using the json Module
- Learn about the `BeautifulSoup` package. Watch Python Tutorial: Web Scraping with BeautifulSoup and Requests
- Learn about the `pandas` package. Watch
  - Python Pandas Tutorial (Part 1): Getting Started with Data Analysis - Installation and Loading Data
  - Python Pandas Tutorial (Part 2): DataFrame and Series Basics - Selecting Rows and Columns
- Learn about the `re` package. Watch Python Tutorial: re Module - How to Write and Match Regular Expressions (Regex)
- Learn about the `datetime` package. Watch Python Tutorial: Datetime Module - How to work with Dates, Times, Timedeltas, and Timezones