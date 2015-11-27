'''

 sample_basic_dl.py
 Richard Wen (init.r.w@gmail.com)
 
 Dependencies: Python 2.7
 Developed on: Windows 8 64-bit
 
===============================================================
 
 A simple script to download a single file from a standard link,
 given that it does not redirect
 
'''

# =============================================================
# A. Modules
# =============================================================
import urllib,os

# =============================================================
# B. Settings
# =============================================================
current_directory = os.getcwd()
link = 'http://censusindia.gov.in/pca/pcadata/DDW_PCA3501_2011_MDDS%20with%20UI.xlsx'
directory = os.path.join(current_directory, "output")

# =============================================================
# C. Execute urllib
# =============================================================

# Download File
## Create a URLopener object
## Retrieve the file at the URL specified by variabl 'link'
url_download = urllib.URLopener()
url_download.retrieve(link,os.path.join(directory,os.path.basename(link)))
