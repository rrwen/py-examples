'''

 sample_datagovin_dl_loop.py
 Richard Wen (init.r.w@gmail.com)
 
 Dependencies: Python 2.7
 Developed on: Windows 8 64-bit
 
===============================================================
 
 A simple script to download files from the portal at https://data.gov.in/
 
 Installation
 ------------
 > pip install requests
 
'''

# =============================================================
# A. Modules
# =============================================================
import urllib,requests,os

# =============================================================
# B. Settings
# =============================================================

# B0. Current Path
current_directory = os.getcwd()

# B1. Links
# Add your links here separated by a comma inside the brackets []
# e.g.['https://data.gov.in//resources//traffic-handled-chennai-port-1950-51-2013-14//download']
url_file = os.path.join(current_directory,"input\\sample_datagovin.txt")
with open(url_file, 'r') as f:
	url_list = f.readlines()
print url_list


# B2. Directory
# Add the directory to download all the files to
# e.g. 'C:\\Users\\Users\\Desktop\\'
directory = os.path.join(current_directory,"output")

# =============================================================
# C. Functions
# =============================================================

# datagovin_dl: (listof str) str -> None
# Downloads the file at the link to the directory - a file type and link must be specified
def datagovin_dl(link_list,directory):
	
	# 1. Loop through list of links
	for link in link_list:
		
		# 1.0 Remove newline characters
		link = link.rstrip()
		
		# 1.1 Open the base URL and extract the url redirect link
		url = requests.get(link)
		url_content = url.content.split()
		
		# 1.2 Find the redirection link with a pattern
		for content in url_content:
			if 'content="1;url=' in content:
				link_redirect = content[15:-2]
		
		# 1.3 Open the redirected URL and download it
		url_download = urllib.URLopener()
		url_download.retrieve(link_redirect,os.path.join(directory,os.path.basename(link_redirect)))

# =============================================================
# D. Execution
# =============================================================
datagovin_dl(url_list,directory)
