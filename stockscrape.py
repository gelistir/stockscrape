import bs4
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os
import csv
import pandas
from datetime import date
import pyfiglet
import os.path
import time
import schedule

# ------------------- Logging ----------------------- #
# This is optional. If you dont want to use the library 
# delete this whole logging part and replace
# every logger function with print().
import coloredlogs, logging
logger = logging.getLogger(__name__)
coloredlogs.install(fmt='%(message)s',level='DEBUG', logger=logger)
# --------------------------------------------------- #


print(pyfiglet.figlet_format("StockScrape"))

logger.warning("Enter the yahoo finance URL of your desired stock.")
logger.warning("ex. https://finance.yahoo.com/quote/AAPL/")
url = input("> ")

try:
    page=urlopen(url)
except Exception as e:
    logger.error("Error while opening the URL : " + str(e))
    exit()

soup = bs4.BeautifulSoup(page, "html.parser")
has_header = False

output_file = "scrape_output.csv" # Change however you want

#------------------------------
def parsePrice():
    # Parses current stock price.
    price = soup.find('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text
    return price

def parseClosePrice():
    # Parses open price
    closeprice = soup.find('td',{'class': 'Ta(end) Fw(600) Lh(14px)', "data-test":"PREV_CLOSE-value"}).find('span').text
    return closeprice

def parseOpenPrice():
    # Parses (previous) close price.
    openprice = soup.find('td',{'class': 'Ta(end) Fw(600) Lh(14px)', "data-test":"OPEN-value"}).find('span').text
    return openprice
#-------------------------------


def AutoScrape():
    has_header = False
    soup = bs4.BeautifulSoup(page, "html.parser")

    # If the output file has some data inside, check if it has a csv header
    # has_header = True / False
    try:
        if os.stat(output_file).st_size != 0:
            with open(output_file, 'r') as csv_file:
                sniffer = csv.Sniffer()
                has_header = sniffer.has_header(csv_file.read(2048))
    except:
        # file does not exist, it will be created.
        pass

    with open(output_file, mode='a+', newline='') as csv_file:
        fieldnames = ['Date', 'Open', 'Close']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        if has_header == False: # If the output file doesnt have a header, write one.
            writer.writeheader()

        writer.writerow({'Date': date.today(), 'Open': parseOpenPrice(), 'Close': parsePrice()})
        #logger.debug("current: " + parsePrice() +"\n" + "open: " + parseOpenPrice() + "\n" "close: " + parseClosePrice())
        
        # These two lines just create a nice table of the data in the output csv file. You can delete them if you want.
        df = pandas.read_csv(output_file)
        logger.debug(df)

        logger.debug("\n Inserted data to an output file: " + output_file + "\n")


schedule.every().day.at("22:00").do(AutoScrape) # Change the time depending on when does the stockmarket close, because we need to get todays close value.

while True:
    try:
        schedule.run_pending()
    except KeyboardInterrupt:
        logger.error("Exiting...")
        exit()