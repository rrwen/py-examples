'''

 basic_url_downloader.py
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

# B0. Introduction
print("\n===========================\nPython Basic URL Downloader\n===========================\n")

# B1. Link File
# The link file contains a list of urls, one url per line
url_file = raw_input('--Enter the path to the url file (e.g input\\\\basic_urls.txt): ')
with open(url_file, 'r') as f:
	url_list = f.readlines()

# B2. Directory
# The directory to download all the files to
directory = raw_input('--Enter the directory to store the downloads (e.g output): ')

# =============================================================
# C. Functions
# =============================================================

# basic_dl: (listof str) str -> None
# Downloads the file at the link to the directory - a file type must be specified
def basic_dl(link_list,directory):
	
	# 1. Loop through list of links
	print "\n--Progress"
	for link in link_list:
		
		# 1.1 Strip newlines and Progress Message
		link = link.rstrip()
		file_name = os.path.basename(link)
		print ".Downloading "+file_name+"..."
		
		# 1.2 Open the link and download the file to the directory
		try:
			url_download = urllib.URLopener()
			url_download.retrieve(link,os.path.join(directory,file_name))
		except:
			print "..Unable to download "+file_name+"..."
	
	# 2. Exit Message
	print "...Finished"

# =============================================================
# D. Execution
# =============================================================
basic_dl(url_list,directory)
