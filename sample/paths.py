'''

 paths.py
 Richard Wen (init.r.w@gmail.com)
 
 Dependencies: Python 2.7
 Developed on: Windows 7 32-bit
 
===============================================================
 
 Basic path example in Python
 
'''

# 1. Modules
# Import the os module
import os

# 2. Create Directory
# Create a directory using a relative path associated to this file
this_file = os.getcwd()
new_folder = this_file + "\\output\\new folder"

# 3. Create Folder
# Create a folder inside the output folder if it does not exist
if not os.path.exists(new_folder):
    os.makedirs(new_folder)
