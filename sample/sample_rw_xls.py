'''

 sample_rw_xls.py
 Richard Wen (init.r.w@gmail.com)
 
 Dependencies: Python 2.7
 Developed on: Windows 8 64-bit
 
===============================================================
 
 A simple script to read and write excel spreadsheets
 
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
write_ss = os.path.join(current_directory,"output\\write_ss.xls")

# =============================================================
# C. Read and Write xls
# =============================================================

# 1. Read xls
## Read the sample_ss data at input\\sample_ss.xls into variable 'sheet'
## You may reference by letter/number or by row/col numbers
## The very first cell is A1 for letter/number
## The very first cell is [0,0] for row/col numbers
sheet = pyexcel.get_sheet(file_name=sample_ss)
print "Value at A1: " + sheet['A1']
print "Value at [0,0]: " + sheet[0,0]
print "Value at B1: " + sheet['B1']
print "Value at [0,1]: " + sheet[0,1]

# 2. Write xls 
sheet.save_as(write_ss)
