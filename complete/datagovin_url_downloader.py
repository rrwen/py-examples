'''

 datagovin_url_downloader.py
 Richard Wen (init.r.w@gmail.com)
 
 Dependencies: Python 2.7
 Developed on: Windows 8 64-bit
 
===============================================================
 
 A simple script to download a number of files from https://data.gov.in/
 
'''

# =============================================================
# A. Modules
# =============================================================
import urllib,os,requests

# =============================================================
# B. Settings
# =============================================================

# B0. Introduction
print("\n=================================\nPython data.gov.in URL Downloader\n=================================\n")

# B1. Link File
# The link file contains a list of urls, one url per line
url_file = raw_input('--Enter the path to the url file (e.g input\\\datagovin_urls.txt): ')
with open(url_file, 'r') as f:
	url_list = f.readlines()

# B2. Directory
# The directory to download all the files to
directory = raw_input('--Enter the directory to store the downloads (e.g output): ')

# =============================================================
# C. Functions
# =============================================================

# datagovin_dl: (listof str) str -> None
# Downloads the file at the link to the directory - a file type and link must be specified
def datagovin_dl(link_list,directory):
	
	## 1. Loop through list of links
	print "\n--Progress"
	for link in link_list:
		
		# 1.1 Strip newlines
		link = link.rstrip()
		
		## 1.2.1 Open the base URL and extract the url redirect link
		url = requests.get(link)
		url_content = url.content.split()
		
		## 1.2.2 Find the redirection link
		for content in url_content:
			if 'content="1;url=' in content:
				link_redirect = content[15:-2]
		
		# 1.3 Progress message and file name
		file_name = os.path.basename(link_redirect)
		print ".Downloading "+file_name+"..."
		
		## 1.4 Open the redirected URL and download it
		try:
			url_download = urllib.URLopener()
			url_download.retrieve(link_redirect,os.path.join(directory,file_name))
		except:
			print "..Unable to download "+file_name+"..."		
		
	# 2. Exit Message
	print "...Finished"


# =============================================================
# D. Execution
# =============================================================
datagovin_dl(url_list,directory)
