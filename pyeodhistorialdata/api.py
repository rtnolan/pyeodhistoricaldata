import os
import requests
import pandas as pd
from io import StringIO

class EODHistoricalData:
  def __init__(self):
    self.base_url = "https://eodhistoricaldata.com/api"
    self.api_key = os.environ.get('EOD_HISTORICAL_DATA_API_KEY_DEFAULT') or None
  
  def _url_builder(self, base, path, start_date = None, end_date = None):
    endpoint = "/{base}/{path}".format(base=base,path=path)
    params = {
        "api_token": self.api_key,
        "from": start_date,
        "to": end_date
    }
    url = self.base_url + endpoint
    return url, params
  
  def get_eod(self, symbol, exchange, start_date = None, end_date = None):
    path = symbol + "." + exchange
    url, params = self._url_builder("eod",path,start_date,end_date)
    resp = requests.get(url, params=params)
    if resp.status_code == requests.codes.ok:
      df = pd.read_csv(StringIO(resp.text), engine='python', skipfooter=1, parse_dates=[0], index_col=0)
      return df