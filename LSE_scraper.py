from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import re
import itertools

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

    dates_dict = dict(zip(columns, dates))

    company_name = 'Amiad Water Systems Ltd'
    metrics = ['Total Revenue', 'Dividend per share', 'Operating profit', 'Net interest', 'Taxes']
    js_extension = '&q;,&q;value&q;:'
    pattern2 = r'\d+(?:\.\d+)?'

    # Get currency positions and values, compare with dates dict to get currency by year
    pattern3 = r'currency&q;:{&q;label&q'
    pattern4 = r'[A-Z]{3}'
    currency_pos = [c.start() for c in re.finditer(pattern3, text)]
    currency_values = []
    for c in currency_pos:
        currency_soup = text[c: c + 100]
        currency = re.search(pattern4, currency_soup)
        currency_values.append(currency.group())

    currency_dict = dict(zip(currency_pos, currency_values))

    # Sort keys for loop
    dates_dict_keys = list(reversed(sorted(dates_dict.keys())))

    cur_dat_dict = {}
    for cur in currency_dict:
        for d in dates_dict_keys:
            if d < cur:
                cur_dat_dict[dates_dict[d]] = currency_dict[cur]
                break

    output_list = []
    # For loop over metrics
    for metric in metrics:

        # Get positions of the metric so we can find the year
        metric_positions = [p.start() for p in re.finditer(metric+js_extension, text)]

        metric_dates = []
        for item in metric_positions:
            for k in dates_dict_keys:
                if k < item:
                    metric_dates.append(dates_dict[k])
                    break


        # Pull out values
        value_soup = re.findall(metric+js_extension+pattern2, text)
        values = []
        for value in value_soup:
            v = re.search(pattern2, value)
            values.append(v.group())

        metrics_list = [metric for i in range(len(metric_dates))]
        company_list = [company_name for i in range(len(metric_dates))]

        working_output = list(zip(company_list, metrics_list, metric_dates, values))
        working_output = list(set(working_output))
        output_list.append(working_output)
    
    output_list = list(itertools.chain.from_iterable(output_list))

    # get in to dataframe long narrow format
    df = pd.DataFrame(output_list, columns = ['Company name', 'Metric', 'FYE', 'Value'])

    # Add currencies to dataframe
    #currency_map_dict = cur_dat_dict
    currency_map_dict = {}
    for k in cur_dat_dict:
        key_ = (re.search(r'\d{4}', k)).group()
        value_ = cur_dat_dict[k]
        currency_map_dict[key_] = value_
    #df['Currency'] = 
    # add all extra metrics 
    # export to excel
    df.to_excel(r'test_output.xlsx', encoding='UTF-8')

    return currency_map_dict

# Output to csv/excel format

print(processor(contents))

# test output

# with open("output.txt", "w") as text_file:
#     text_file.write(test)
