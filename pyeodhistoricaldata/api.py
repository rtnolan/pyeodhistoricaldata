import os
import requests
import json

class EODHistoricalData:
  def __init__(self):
    self.base_url = "https://eodhistoricaldata.com/api"
    self.api_key = os.environ.get('EOD_HISTORICAL_DATA_API_KEY_DEFAULT') or None
  
  def _url_builder(self, base, path, fmt, start_date, end_date):
    endpoint = "/{base}/{path}".format(base=base,path=path)
    params = {
        "api_token": self.api_key,
        "from": start_date,
        "to": end_date,
        "fmt": fmt
    }
    url = self.base_url + endpoint
    return url, params
  
  def get_eod(self, symbol, exchange, start_date=None, end_date=None, fmt='json'):
    path = symbol + "." + exchange
    url, params = self._url_builder('eod',path,fmt, start_date,end_date)
    resp = requests.get(url, params=params)
    if resp.status_code == requests.codes.ok:
      if fmt == 'json':
        return json.loads(resp.text)
      else:
        return resp.text