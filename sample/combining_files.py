'''

 combining_files.py
 Richard Wen (init.r.w@gmail.com)
 
 Dependencies: Python 2.7
 Developed on: Windows 7 32-bit
 
===============================================================
 
 Basic file read and write example in Python
 
'''

# 0. Get the current directory
import os
current_directory = os.getcwd()

# 1. Part 1 Data
# Creates a variable 'part1' containing the first part text file to be combined
## Read the contents into variable 'part1_data'
part1_directory = os.path.join(current_directory, 'input\\part1.txt')
with open(part1_directory,'r') as part1:
    part1_data = part1.readlines()

# 2. Part 2 Data
# Creates a variable 'part2' containing the second part text file to be combined
## Read the contents into variable 'part2_data'
part2_directory = os.path.join(current_directory, 'input\\part2.txt')
with open(part2_directory,'r') as part2:
    part2_data = part2.readlines()

# 3. Missing Data
# Creates a variable 'missing' to include in the final file
missing = "http://www.censusindia.gov.in/2011census/C-series/c-13/DDW-1900C-13.xls"

# 4. Combine Parts and Missing Data
## Combine part1 and part2 list to variable 'combined_data'
## Append the string variable 'missing' to 'combined_data'
## Notice how there are no newlines at the ends of the files, we need to add them there
part1_data.append('\n')
part2_data.append('\n')
combined_data = part1_data + part2_data
combined_data.append(missing)

# 5. Write to File
# Creates a variable 'combined' containing an empty text file for writing
# and writes to the file
output_directory = os.path.join(current_directory, 'output//combined.txt')
with open(output_directory,'w') as combined:
    for line in combined_data:
        combined.write(line)
