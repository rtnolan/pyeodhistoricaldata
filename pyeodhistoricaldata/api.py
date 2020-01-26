import os
import requests
import json

class EODHistoricalData:
  def __init__(self):
    self.base_url = "https://eodhistoricaldata.com/api"
    self.api_key = os.environ.get('EOD_HISTORICAL_DATA_API_KEY_DEFAULT') or None
  
  def _url_builder(self, base, path):
    """
     Build URL for request
    Args:
        base (str): Base part of url.
        path (str): Path of request
        
    :returns: :str: URL.
    """
    endpoint = "/{base}/{path}".format(base=base,path=path)
    url = self.base_url + endpoint
    return url
  
  def get_eod(self, symbol, exchange, start_date=None, end_date=None, fmt='json'):
    """
    Get End of Day Information for a given symbol
    Args:
        symbol (str): The symbol to retrieve data for.
        exchange (str): The exchange it's part of.
        start_date (str): From which date to retriev data.
        end_date (str): To which date to retreive data.
        fmt (str): The format of the response to return.
        
    :returns: EOD Data for a given symbol.
    """
    path = symbol + "." + exchange
    url = self._url_builder('eod',path)
    params = {
      "api_token": self.api_key,
      "from": start_date,
      "to": end_date,
      "fmt": fmt
    }
    try:
      resp = requests.get(url, params=params)
    except requests.exceptions.RequestException as err:
      raise requests.exceptions.RequestException()
    if resp.status_code == requests.codes.ok:
      if fmt == 'json':
        return json.loads(resp.text)
      else:
        return resp.text
  
  def get_fundamentals(self, symbol, exchange, filter=None, fmt='json'):
    """
    Get Fundamental data for a given symbol
    Args:
        symbol (str): The symbol to retrieve data for.
        exchange (str): The exchange it's part of.
        filter (str): Filter string to limit data returned.
        fmt (str): The format of the response to return.
        
    :returns: Fundamental Data for a given symbol.
    """
    path = symbol + "." + exchange
    url = self._url_builder('fundamentals', path)
    params = {
      "api_token": self.api_key,
      "filter": filter,
      "fmt": fmt
    }
    try:
      resp = requests.get(url, params=params)
    except requests.exceptions.RequestException as err:
      raise requests.exceptions.RequestException()
    if resp.status_code == requests.codes.ok:
        if fmt == 'json':
          return json.loads(resp.text)
        else:
          return resp.text
