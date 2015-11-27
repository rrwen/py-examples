'''

 sample_multi_xls.py
 Richard Wen (init.r.w@gmail.com)
 
 Dependencies: Python 2.7
 Developed on: Windows 8 64-bit
 
===============================================================
 
 A simple script to demonstrate dealing with
 multiple sheets in an excel spreadsheet
 
'''

# =============================================================
# A. Modules
# =============================================================
import pyexcel, pyexcel.ext.xls, os

# =============================================================
# B. Settings
# =============================================================
current_directory = os.getcwd()
sample_multi_ss = os.path.join(current_directory,"input\\sample_multi_ss.xls")
multi_ss = os.path.join(current_directory,"output\\multi_ss.xls")

# =============================================================
# C. Multiple Sheets in xls
# =============================================================

# 1. Read xls
## Read the sample_ss data at input\\sample_ss.xls into variable 'sheet'
book = pyexcel.get_book(file_name=sample_multi_ss)

# 2. Get Sheets and delete sheet 2
sheet1 = book[0]
sheet2 = book[1]
del book[1]

# 3. Save multiple sheet xls with changes
## Use save_book_as if multiple sheets
book.save_as(multi_ss)
