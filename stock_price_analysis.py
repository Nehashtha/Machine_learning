import pandas as pd
import csv
from bs4 import BeautifulSoup
import requests

def construct_today_quote_url(ticker):
    url = "https://finance.yahoo.com/quote/"+ticker+"?p="+ticker
    return url

def construct_historical_url(ticker):
    url ="https://finance.yahoo.com/quote/"+ticker+"/history?p="+ticker
    # "https://finance.yahoo.com/quote/NVDA/history?p=NVDA"
    # "https://finance.yahoo.com/quote/AMD/history?p=AMD"

    return url

def get_historical_data(page, ticker):
    """
    get_historical_data(page, ticker): Parses historical section of finance.yahoo.com to retrieve stock prices and volume on a given day for given ticker
    :param page: page is result obtained from requests.get(url_string)
    :param ticker:
    :return:
    """
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find('table')
    tr_all = table.find_all('tr')

    csv_file = open("./historical_data_"+ticker+".csv", "w")
    writer = csv.writer(csv_file, delimiter=',')

    lst = ['date', 'Open', 'High', 'Low', 'Close', 'Adj_Close', 'Volume']
    writer.writerow(lst)

    count = 0
    for tr in tr_all:
        td_all = tr.find_all('td')
        # td = tr.find('td')
        '''
        date = td_all[0]
        Open = td_all[1]
        High = td_all[2]
        Low = td_all[3]
        Close = td_all[4]
        Adj_Close = td_all[5]
        Volume = td_all[6]
        '''
        # print(tr)
        # print(td_all)
        lst = []
        if td_all:
            print(td_all)
            for td in td_all:
                print(td.text)
                lst.append(td.text)
            writer.writerow(lst)
        print()
    csv_file.close()


def parsePage(page):
    """
    parsePage(page): Parses the max and min for a given stock_ticker for today's date
    :param page: page is result obtained from requests.get(url_string)
    :return:
    """
    # print(page.content)
    soup = BeautifulSoup(page.content, 'html.parser')
    # paragraph = soup.find_all('p')
    table = soup.find_all('table')

    my_table = table[0]
    rows = my_table.findChildren(['th', 'tr'])

    for r in rows:
        print_next = False
        for td in r.find_all('td', attrs={'data-test':"DAYS_RANGE-value"}):

            # if ("Day's Range" in td.text):
            #     if(print_next):
            min, max = td.text.split(' - ')
            print(min)
            print(max)
            #     print_next = True


def getHtmlPage(url):
    page = requests.get(url)
    return page

def csv_try():
    csv_file = open("./historical_data.csv", "w")
    writer = csv.writer(csv_file, delimiter=',')
    lst = ['hello', 'world', 'how', 123, 65]
    lst1 = ['doing', 5454,232323, 'good']
    writer.writerow(lst)
    writer.writerow(lst1)
    csv_file.close()

def main():
    # htmlPage = getHtmlPage("https://finance.yahoo.com/quote/MSFT?p=MSFT")
    # htmlPageAMD = getHtmlPage("https://finance.yahoo.com/quote/AMD?p=AMD")
    # parsePage(htmlPageAMD)


    # url = construct_today_quote_url("NVDA")
    # htmlPage = getHtmlPage(url)
    # parsePage(htmlPage)

    # print(help(parsePage))
    ticker_lst = ["NVDA", "AMD", "TEAM", "MSFT", "FB"]
    # ticker = "GOOG"
    for ticker in ticker_lst:
        url = construct_historical_url(ticker)
        print(url)

        # htmlPage = getHtmlPage(url)
        # print(htmlPage.content)
        # get_historical_data(htmlPage, ticker)
    #
    # csv_try()


if __name__=='__main__':
    main()