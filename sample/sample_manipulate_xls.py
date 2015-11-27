'''

 sample_manipulate_xls.py
 Richard Wen (init.r.w@gmail.com)
 
 Dependencies: Python 2.7
 Developed on: Windows 8 64-bit
 
===============================================================
 
 A simple script to demonstrate excel spreadsheet manipulation
 
'''

# =============================================================
# A. Modules
# =============================================================
import pyexcel, pyexcel.ext.xls, os

# =============================================================
# B. Settings
# =============================================================
current_directory = os.getcwd()
sample_ss = os.path.join(current_directory,"input\\sample_ss.xls")
manipulate_ss = os.path.join(current_directory,"output\\manipulate_ss.xls")

# =============================================================
# C. Manipulate xls
# =============================================================

# 1. Read xls
## Read the sample_ss data at input\\sample_ss.xls into variable 'sheet'
sheet = pyexcel.get_sheet(file_name=sample_ss)


# 2. Change xls
## Change st_code to state code
## Change row 5 values, notice the unicode to match its original file contents
## Delete the population column located at column 4
## Add a new row
sheet.row[5] = [u'C3713', u'33', u'000', u'State - TAMIL NADU (33)', 72.0, 86980.0, 70889.0]
del sheet.column[5]
sheet.row += [u'C1300', u'00', u'000', u'India', 48.0, 5568554.0, 6081038.0]
## Add some unique ids
ids = range(1,51)
ids.insert(0,u'id')
sheet.column += ids

# 3. Save xls with changes
sheet.save_as(manipulate_ss)
