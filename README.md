# Python Excel Spreadsheets Examples
  
  
Richard Wen (rich.rwen@gmail.com)  
  
This repository contains some quick examples on working with Excel spreadsheets via Python's [pyexcel](https://pypi.python.org/pypi/pyexcel) and [pyexcel-xls](https://pypi.python.org/pypi/pyexcel-xls) libraries.
* Coded for the purpose of merging nonstandard data from [censusindia.gov.in](http://censusindia.gov.in/)
  
**Requirements**  
* [Python 2.7](https://www.python.org/downloads/)  
* [pyexcel](https://pypi.python.org/pypi/pyexcel) and [pyexcel-xls](https://pypi.python.org/pypi/pyexcel-xls) `pip install pyexcel pyexcel-xls`    
  
## Quick Start
  
1. Install [Python 2.7](https://www.python.org/downloads/) if it is not installed  
2. Download [this repository](https://github.com/rrwen/py-examples/archive/xls.zip)  
3. Run cmd.bat    
4. Install pyexcel and pyexcel-xls `pip install pyexcel pyexcel-xls`  
  
**Example 1: Local Spreadsheet Merger**  
  
The `complete\censusindia_xls_merger_local.py` code takes in a folder with spreadsheets (see [input](https://github.com/rrwen/py-examples/tree/xls/input)) and merges them into a single spreadsheet. All spreadsheets in the folder will be merged.  
  
1. Run cmd.bat and type in `python complete\censusindia_xls_merger_local.py`  
2. When prompted for a folder, type in `input`  
3. When prompted for a single spreadsheet to save to, type in `output\\local_merged.xls` 
<img src="https://raw.githubusercontent.com/rrwen/py-examples/xls/img/censusindia_xls_merger_local.JPG" width="700;"/>  
  
**Example 2: URL Spreadsheet Merger**  
  
The `complete\censusindia_xls_merger_url.py` code accepts a list of spreadsheet urls (see [censusindia_urls.txt](https://github.com/rrwen/py-examples/blob/xls/input/censusindia_urls.txt)) and merges them into a single spreadsheet.
  
1. Run cmd.bat and type in `python complete\censusindia_xls_merger_url.py`  
2. When prompted for a list of urls, type in `input\\censusindia_urls.txt`
3. When prompted for a single spreadsheet to save to, type in `output\\url_merged.xls` 
<img src="https://raw.githubusercontent.com/rrwen/py-examples/xls/img/censusindia_xls_merger_url.JPG" width="700;"/>  
  
**More Examples:**
* [complete](https://github.com/rrwen/py-examples/tree/xls/complete) for prepared code  
* [sample](https://github.com/rrwen/py-examples/tree/xls/sample) for snippets of code  
* [input](https://github.com/rrwen/py-examples/tree/xls/input) for samples of acceptable file inputs  
  
