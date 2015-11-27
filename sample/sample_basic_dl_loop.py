'''

 sample_basic_dl_loop.py
 Richard Wen (init.r.w@gmail.com)
 
 Dependencies: Python 2.7
 Developed on: Windows 8 64-bit
 
===============================================================
 
 A simple script to download a number of files from a standard link
 with no redirect
 
'''

# =============================================================
# A. Modules
# =============================================================
import urllib,os

# =============================================================
# B. Settings
# =============================================================

# B0. Current Path
current_directory = os.getcwd()

# B1. Links
# Add your links here with quotations separated by a comma inside the brackets []
# e.g. 'http://censusindia.gov.in/pca/pcadata/DDW_PCA3501_2011_MDDS%20with%20UI.xlsx'
url_file = os.path.join(current_directory,"input\\sample_urls.txt")
with open(url_file, 'r') as f:
	url_list = f.readlines()
print url_list

# B2. Directory
# Add the directory to download all the files to inside the quotations
# e.g. 'C:\\Users\\User\\Desktop'
directory = os.path.join(current_directory,"output")

# =============================================================
# C. Functions
# =============================================================

# basic_dl: (listof str) str -> None
# Downloads the file at the link to the directory - a file type must be specified
def basic_dl(link_list,directory):
	
	# 1. Loop through list of links
	for link in link_list:
		
		# 1.1 Remove newline characters
		link = link.rstrip()
		
		# 1.2 Open the link and download the file to the directory
		url_download = urllib.URLopener()
		url_download.retrieve(link,os.path.join(directory,os.path.basename(link)))

# =============================================================
# D. Execution
# =============================================================
basic_dl(url_list,directory)
