# EOD Historical Data API Wrapper
A wrapper around EOD historical data API at https://eodhistoricaldata.com.

# Installation 
```bash
pip install pyeodhistoricaldata
```
# Usage
An Environment Variable named `EOD_HISTORICAL_API_KEY` needs to be defined:
```bash
export EOD_HISTORICAL_API_KEY="YOUR_API"
```
### Example
```python
from pyeodhistoricaldata import EODHistoricalData
import json

api = EODHistoricalData()
data = api.get_eod('AAPL', 'US', '2019-01-15', '2019-01-18')
print(json.dumps(data, indent=2))

"""
[
  {
    "date": "2019-01-15",
    "open": 150.27,
    "high": 153.39,
    "low": 150.05,
    "close": 153.07,
    "adjusted_close": 150.8041,
    "volume": 28710324
  },
  {
    "date": "2019-01-16",
    "open": 153.08,
    "high": 155.88,
    "low": 153,
    "close": 154.94,
    "adjusted_close": 152.6465,
    "volume": 30569706
  },
  {
    "date": "2019-01-17",
    "open": 154.2,
    "high": 157.66,
    "low": 153.26,
    "close": 155.86,
    "adjusted_close": 153.5528,
    "volume": 29821160
  },
  {
    "date": "2019-01-18",
    "open": 157.5,
    "high": 157.88,
    "low": 155.9806,
    "close": 156.82,
    "adjusted_close": 154.4986,
    "volume": 33751023
  }
]
"""
```

### Return Formats
By default the response is in JSON, you can also change the format to be _csv_ by adding an extra parameter to the API call e.g.
```python
data = api.get_eod('AAPL', 'US', '2019-01-15', '2019-01-18', fmt='csv')
print(data)

"""
Date,Open,High,Low,Close,Adjusted_close,Volume
2019-01-15,150.27,153.39,150.05,153.07,150.8041,28710324
2019-01-16,153.08,155.88,153,154.94,152.6465,30569706
2019-01-17,154.2,157.66,153.26,155.86,153.5528,29821160
2019-01-18,157.5,157.88,155.9806,156.82,154.4986,33751023
272
"""
