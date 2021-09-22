from stockwatcher.models import Stock
import requests
import json
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    """
    ticker = models.TextField(blank=True, null=True)
    asset_description = models.TextField(blank=True, null=True)
    asset_type = models.TextField(blank=True, null=True)
    amount = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    transaction_date = models.DateField(blank=True, null=True)
    senator = models.TextField(blank=True, null=True)
    """
    help = 'Gets the Senator History JSON data from the API'

    def handle(self, *args, **options):
      
      api_resp = getDisclosures()
      for resp in api_resp:
        s = Stock(
          ticker = resp["ticker"],
          asset_description = resp["asset_description"],
          asset_type = resp["asset_type"],
          amount = resp["amount"],
          type = resp["type"],
          transaction_date = resp["transaction_date"],
          senator = resp["senator"]
        )
        s.save()
      self.stdout.write("Finished API Polling")


def getDisclosures(endpoint="https://senate-stock-watcher-data.s3-us-west-2.amazonaws.com/aggregate/all_transactions.json"):
  """
  Writes the daily disclosures of senators to a log file. Log file is seperated by day.
 
  Parameters
  ----------
  endpoint: str
    The REST endpoint of senate stock watcher used to grab the senator information.
  """
  # Load the data into JSON format
  req_json = json.loads(requests.get(endpoint, allow_redirects=True).text)

  # Clean up the data (e.g. remove NULL tickers)
  stock_history_validated = []
  for n in range(len(req_json)):
    if req_json[n]["ticker"] == "--" or req_json[n]["ticker"] == "N/A" or req_json[n]["amount"].upper() == "UNKNOWN":
      pass
    else:
      min_amt, max_amt = req_json[n]["amount"].split('-')[0], req_json[n]["amount"].split('-')[1]
      min_amt, max_amt = int(min_amt.replace(",", "").replace("$", "")), int(max_amt.replace(",", "").replace("$", ""))
      req_json[n]["amount"] = round((min_amt + max_amt) / 2)
      req_json[n]["transaction_date"] = f'{req_json[n]["transaction_date"][6:10]}-{req_json[n]["transaction_date"][0:2]}-{req_json[n]["transaction_date"][3:5]}'
      stock_history_validated.append(req_json[n])
    
  validated_json = json.loads(json.dumps(stock_history_validated))
  return validated_json