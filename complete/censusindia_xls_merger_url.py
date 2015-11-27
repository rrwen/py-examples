'''

 censusindia_xls_merger_url.py
 Richard Wen (init.r.w@gmail.com)
 
 Dependencies: Python 2.7
 Developed on: Windows 8 64-bit
 
===============================================================
 
 A script to obtain data from census india and merge it together
 
'''

# =============================================================
# A. Modules
# =============================================================
import pyexcel, pyexcel.ext.xls, os

# =============================================================
# B. Settings
# =============================================================

# B0. Introduction
print("\n============================================\nPython Census India Excel Spreadsheet Merger\n============================================\n")

# B1. Link File
# The link file contains a list of urls, one url per line
url_file = raw_input('--Enter the path to the url file (e.g input\\\censusindia_urls.txt): ')
with open(url_file, 'r') as f:
	url_list = f.readlines()

# B2. Directory
# The directory to download all the files to
directory = raw_input('--Enter the merged file name (e.g output\\\url_merged.xls): ')

# =============================================================
# C. Read and Write xls
# =============================================================

# 0. Store merged sheet
merged_sheet = pyexcel.Sheet()
merged_sheet.row += [u'table',u'st_code',u'dist_code',u'area_name',
                     u'age',u'total_persons',u'total_males',u'total_females',
                     u'rural_persons',u'rural_males',u'rural_females',
                     u'urban_persons',u'males',u'females']
num_of_col = len(merged_sheet.row[0])

# 0.1 Display files to be merged
print '\n--Merging the following:\n'+''.join(url_list)
if len(url_list) == 0:
	print "\n...No .xls URLs Found"

# 1. Read url list
for link in url_list:
	
	# 1.1 Obtain sheet from link
	## rstrip for removing newline characters
	link = link.rstrip()
	try:
		# 1.1.1 Get excel sheet object
		sheet = pyexcel.get_sheet(url=link)

		# 1.1.2 Check column length for each row
		num_of_col_for_sheet = len(sheet.row[0])
		if num_of_col_for_sheet != num_of_col:
			print "..Warning: "+link+" has",num_of_col_for_sheet,"but expected",num_of_col,"columns"
	except:
		print "..Unable to download and read from "+link+"..."
	
	# 1.2 Merge sheet by row
	try:
		del sheet.row[0:7]
		merged_sheet.row += sheet
	except:
		print "..Unable to merge "+link+"..."		

# 2. Write merged sheet
## Create a pyexcel writer and write it to directory specified by user input
try:
	writer = pyexcel.Writer(directory)
	writer.write_reader(merged_sheet)
	writer.close()
except:
	print "...Unable to write to "+directory
print "...Finished"
