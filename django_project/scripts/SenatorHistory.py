import requests
import os
from datetime import date
import ast
#from requests.exceptions import HTTPError 
 
def getDisclosures(endpoint="https://senate-stock-watcher-data.s3-us-west-2.amazonaws.com/aggregate/all_transactions.json"):
  """
  Writes the daily disclosures of senators to a log file. Log file is seperated by day.
 
  Parameters
  ----------
  endpoint: str
    The REST endpoint of senate stock watcher used to grab the senator information.
  """
  data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
 
  # Save today's disclosures in a log file. Log files are segregated by day.
  todays_date = date.today().strftime("%d-%m-%Y")
 
  with open(f'{data_dir}/disclosure-{todays_date}', "w+") as fw:
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
