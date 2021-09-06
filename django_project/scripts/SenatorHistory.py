from numpy import average
import requests
import os
from datetime import date
import ast
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

for n in range(len(stock_history)):
  if stock_history[n]["ticker"] == "--" or stock_history[n]["ticker"] == "N/A" or stock_history[n]["amount"].upper() == "UNKNOWN":
    pass
  else:
    stock_history_validated.append(stock_history[n])


for n in range(len(stock_history_validated)):
  strAmountMin = stock_history_validated[n]['amount'].split(' - ')[0]
  strAmountMax = stock_history_validated[n]['amount'].split(' - ')[1]
  amountMin = int(strAmountMin.replace(",","").replace("$",""))
  amountMax = int(strAmountMax.replace(",","").replace("$",""))
  stock_history_validated[n]['amount'] = (amountMin + amountMax)/2


#Table add record script
import sqlite3

def add_record(i):
    try:
        sqliteConnection = sqlite3.connect('../db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")

        sqlite_insert_query = """INSERT INTO StockTable
                            (ticker, asset_description, asset_type, amount, type, transaction_date, senator) 
                            VALUES 
                            (?,?,?,?,?,?,?)"""
        data_tuple = (stock_history_validated[i]["ticker"],
                        stock_history_validated[i]["asset_description"],
                        stock_history_validated[i]["asset_type"],
                        stock_history_validated[i]["amount"],
                        stock_history_validated[i]["type"],
                        stock_history_validated[i]["transaction_date"],
                        stock_history_validated[i]["senator"])
        count = cursor.execute(sqlite_insert_query, data_tuple)
        sqliteConnection.commit()
        print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

for i,j in enumerate(stock_history_validated):
    add_record(i)