'''

 sample_redirect_contents.py
 Richard Wen (init.r.w@gmail.com)
 
 Dependencies: Python 2.7
 Developed on: Windows 8 64-bit
 
===============================================================
 
 A simple script to read a single file containing a redirect
 link
 
 Installation
 ------------
 > pip install requests
 
'''

# =============================================================
# A. Modules
# =============================================================
import os,requests

# =============================================================
# B. Settings
# =============================================================
link = 'https://data.gov.in//resources//traffic-handled-chennai-port-1950-51-2013-14//download'

# =============================================================
# C. Execute requests
# =============================================================

# Requests
## Get the content of the link request
## Display the link content
url = requests.get(link)
url_content = url.content
print url_content
