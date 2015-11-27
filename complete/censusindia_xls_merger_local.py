'''

 censusindia_xls_merger_local.py
 Richard Wen (init.r.w@gmail.com)
 
 Dependencies: Python 2.7
 Developed on: Windows 8 64-bit
 
===============================================================
 
 A script to get census india data locally and merge it together
 
'''

# =============================================================
# A. Modules
# =============================================================
import pyexcel, pyexcel.ext.xls, os, glob

# =============================================================
# B. Settings
# =============================================================

# B0. Introduction
print("\n==================================================\nPython Census India Local Excel Spreadsheet Merger\n==================================================\n")

# B1. Folder
# The folder contains a a number of census india .xls files to be merged
folder = raw_input('--Enter the folder path with only census india spreadsheets (e.g input): ')
folder_path = os.path.join(folder,"*.xls")
xls_files = glob.glob(folder_path)

# B2. Directory
# The directory to download all the files to
directory = raw_input('--Enter the merged file name (e.g output\\\local_merged.xls): ')

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
print '\n--Merging the following:\n'+'\n'.join(xls_files)
if len(xls_files) == 0:
	print "\n...No .xls Files Found"

# 1. Read url list
for xls in xls_files:
	
	# 1.1 Obtain sheet from link
	## rstrip for removing newline characters
	try:
		# 1.1.1 Get sheet object
		sheet = pyexcel.get_sheet(file_name=xls)
		
		# 1.1.2 Check column length for each row
		num_of_col_for_sheet = len(sheet.row[0])
		if num_of_col_for_sheet != num_of_col:
			print "..Warning: "+xls+" has",num_of_col_for_sheet,"but expected",num_of_col,"columns"
	except:
		print "..Unable to read "+xls+"..."
	
	# 1.2 Merge sheet by row
	try:
		del sheet.row[0:7]
		merged_sheet.row += sheet
	except:
		print "..Unable to merge "+xls+"..."	
	
# 2. Write merged sheet
## Create a pyexcel writer and write it to directory specified by user input
try:
	writer = pyexcel.Writer(directory)
	writer.write_reader(merged_sheet)
	writer.close()
except:
	print "...Unable to write to "+directory
print "...Finished"
