from numpy import average
import requests
import os
from datetime import date
import ast
import datetime
#from requests.exceptions import HTTPError 
import pprint


def getDisclosures(endpoint="https://senate-stock-watcher-data.s3-us-west-2.amazonaws.com/aggregate/all_transactions.json"):
  """
  Writes the daily disclosures of senators to a log file. Log file is seperated by day.
 
  Parameters
  ----------
  endpoint: str
    The REST endpoint of senate stock watcher used to grab the senator information.
  """
  # data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
 
  # Save today's disclosures in a log file. Log files are segregated by day.
  # todays_date = date.today().strftime("%d-%m-%Y")
 
  # with open(f'{data_dir}/disclosure-{todays_date}', "w+") as fw:
  req = requests.get(endpoint, allow_redirects=True)
    #fw.write(req.text) 
  return req.text
 

 
 #####################
 ### CLEAN UP DATA ###
 #####################
stock_history = ast.literal_eval(getDisclosures())
stock_history_validated = []

# Remove all tickers with no value, or amounts given
for n in range(len(stock_history)):
  if stock_history[n]["ticker"] == "--" or stock_history[n]["ticker"] == "N/A" or stock_history[n]["amount"].upper() == "UNKNOWN":
    pass
  else:
    stock_history_validated.append(stock_history[n])

# Replace trading amount from range to average of the range
for n in range(len(stock_history_validated)):
  strAmountMin = stock_history_validated[n]['amount'].split(' - ')[0]
  strAmountMax = stock_history_validated[n]['amount'].split(' - ')[1]
  amountMin = int(strAmountMin.replace(",","").replace("$",""))
  amountMax = int(strAmountMax.replace(",","").replace("$",""))
  stock_history_validated[n]['amount'] = (amountMin + amountMax)/2
  stock_history_validated[n]['transaction_date'] = datetime.datetime.strptime(stock_history_validated[n]['transaction_date'], "%m/%d/%Y").strftime("%Y-%m-%d")



#Table add record script
import sqlite3

def add_records(recordsList):
    try:
        sqliteConnection = sqlite3.connect('./django_project/db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")

        sqlite_insert_query = """INSERT INTO StockTable
                            (ticker, asset_description, asset_type, amount, type, transaction_date, senator) 
                            VALUES 
                            (?,?,?,?,?,?,?)"""
        for i,j in enumerate(recordsList):
          data_tuple = (stock_history_validated[i]["ticker"],
                          stock_history_validated[i]["asset_description"],
                          stock_history_validated[i]["asset_type"],
                          stock_history_validated[i]["amount"],
                          stock_history_validated[i]["type"],
                          stock_history_validated[i]["transaction_date"],
                          stock_history_validated[i]["senator"])
          count = cursor.execute(sqlite_insert_query, data_tuple)
          sqliteConnection.commit()
        print(f"{len(stock_history_validated)} records inserted successfully into SqliteDb_developers table ", cursor.rowcount)
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

add_records(stock_history_validated)