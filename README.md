# Python URL Downloads Examples
  
  
Richard Wen (init.r.w@gmail.com)  
  
This repository contains some quick examples on file downloads via Python's [urllib](https://docs.python.org/2/library/urllib.html?highlight=urllib#module-urllib) and [requests](https://pypi.python.org/pypi/requests) libraries.
* Coded for purposes of downloading particular census and open data for india (e.g. [data.gov.in](https://data.gov.in/catalog/traffic-handled-major-ports-india#web_catalog_tabs_block_10), [censusindia.gov.in](http://www.censusindia.gov.in/2011census/population_enumeration.html))
  
**Requirements**  
* [Python 2.7](https://www.python.org/downloads/)  
* [requests](https://pypi.python.org/pypi/requests) `pip install requests`  
  
## Quick Start
  
1. Install [Python 2.7](https://www.python.org/downloads/) if it is not installed
2. Download [this repository](https://github.com/rwenite/ex-py-url/archive/master.zip)  
3. Run cmd.bat    
4. Install requests `pip install requests` 
  
**Example 1: Basic URL Downloader**  
  
The `complete\basic_url_downloader.py` code accepts a list of file urls (see [basic_urls.txt](https://github.com/rwenite/ex-py-url/blob/master/input/basic_urls.txt)) and downloads them to a directory.  
  
1. Run cmd.bat and type in `python complete\basic_url_downloader.py`  
2. When prompted for a list of urls, type in `input\\basic_urls.txt`
3. When prompted for a directory, type in `output` 
<img src="https://raw.githubusercontent.com/rwenite/ex-py-url/master/img/basic_url_downloader.JPG" width="650;"/>  
  
**Example 2: URL Downloader for data.gov.in**  
  
The `complete\datagovin_url_downloader.py` code accepts a list of redirecting [data.gov.in](https://data.gov.in/) urls (see [datagovin_urls.txt](https://github.com/rwenite/ex-py-url/blob/master/input/datagovin_urls.txt)) and downloads them to a directory.
  
1. Run cmd.bat and type in `python complete\datagovin_url_downloader.py`  
2. When prompted for a list of urls, type in `input\\datagovin_urls.txt`
3. When prompted for a directory, type in `output` 
<img src="https://raw.githubusercontent.com/rwenite/ex-py-url/master/img/datagovin_url_downloader.JPG" width="650;"/>  
  
**More Examples:**
* [complete](https://github.com/rwenite/ex-py-url/tree/master/complete) for prepared code
* [sample](https://github.com/rwenite/ex-py-url/tree/master/sample) for snippets of code
* [input](https://github.com/rwenite/ex-py-url/tree/master/input) for samples of acceptable file inputs
  
