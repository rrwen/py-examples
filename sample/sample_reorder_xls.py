'''

 sample_reorder_xls.py
 Richard Wen (init.r.w@gmail.com)
 
 Dependencies: Python 2.7
 Developed on: Windows 8 64-bit
 
===============================================================
 
 A simple script to reorder excel spreadsheet data
 
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
reorder_ss = os.path.join(current_directory,"output\\reorder_ss.xls")

# =============================================================
# C. Reorder xls
# =============================================================

# 1. Read xls
## Read the sample_ss data at input\\sample_ss.xls into variable 'sheet'
sheet = pyexcel.get_sheet(file_name=sample_ss)

# 2. Reorder Columns
## Swap column 0 with column 3
orig_col = range(0,sheet.number_of_columns())
orig_col[0] = sheet.column[0]
orig_col[3] = sheet.column[3]
sheet.column[3] = orig_col[0]
sheet.column[0] = orig_col[3]
del orig_col

# 3. Reorder Rows
## Swap second and last row
orig_row_first = sheet.row[1]
orig_row_last = sheet.row[sheet.number_of_rows()-1]
sheet.row[1] = orig_row_last
sheet.row[sheet.number_of_rows()-1] = orig_row_first
del orig_row_first
del orig_row_last

# 3. Save xls with changes
sheet.save_as(reorder_ss)
