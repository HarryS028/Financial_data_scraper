from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import re

# Select stock exchange and year 
exchange = 'London Stock Exchange'
year = 2020

# Take a spreadsheet of Company names and URLs and place in a dataframe
xls_file = pd.ExcelFile('test_data.xlsx')
df = xls_file.parse('Sheet1')

file_input = open("output.txt", "r")
if file_input.mode == 'r':
    contents = file_input.read()

# Function that scrapes financial data from a LSE fundamentals web page
def scraper(link):

    driver = webdriver.PhantomJS()
    driver.get(link)
    html = driver.execute_script("return document.body.outerHTML;")
    soup = BeautifulSoup(html, 'html.parser')

    return soup


# Function that converts scraped LSE data in to long and narrow format, columns company name, metric, year, value, currency, unit

def processor(text):

    # Get positions of dateyearend
    pattern = r'\d{4}-\d{2}-\d{2}'
    columns = [y.start() for y in re.finditer(pattern, text)]

    dates = []
    for p in columns:
        dates.append(text[p:p+9])

    metric = 'Total Revenue'
    js_extension = '&q;,&q;value&q;:'
    pattern2 = r'\d+(?:\.\d+)?'

    # Get positions of the metric so we can find the year
    metric_positions = [p.start() for p in re.finditer(metric+js_extension, text)]

    metric_dates = []
    for item in metric_positions:
        for col in columns:
            if item > col:
                

    # Pull out values
    value_soup = re.findall(metric+js_extension+pattern2, text)
    values = []
    for value in value_soup:
        v = re.search(pattern2, value)
        values.append(v.group())


    # Between dateyearends read data with regexs and process in to long format

    # Convert to dataframe and return 


    return columns



# Cycle through URls and call function to pull financial data in to a dataframe
# &q;revenue&q;:{&q;label&q;:&q;Total Revenue&q;,&q;value&q;:112269000,&q;visibility&q;:true,&q;errorText&q;:null}
# {&q;dateyearend&q;:{&q;label&q;:&q;-&q;,&q;value&q;:&q;2017-12-31&q;,&q;visibility&q;:true,&q;errorText&q;:null},
# &q;currency&q;:{&q;label&q;:&q;-&q;,&q;value&q;:&q;USD&q;,&q;visibility&q;:true,&q;errorText&q;:null},
# &q;totaldividend&q;:{&q;label&q;:&q;Dividend per share&q;,&q;value&q;:0.032,&q;visibility&q;:true,&q;errorText&q;:null},
# &q;taxes&q;:{&q;label&q;:&q;Taxes&q;,&q;value&q;:&q;-&q;,&q;visibility&q;:true,&q;errorText&q;:null}
# Output to csv/excel format

print(processor(contents))

# test output

# with open("output.txt", "w") as text_file:
#     text_file.write(test)
