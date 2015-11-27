'''

 raw_input.py
 Richard Wen (init.r.w@gmail.com)
 
 Dependencies: Python 2.7
 Developed on: Windows 7 32-bit
 
===============================================================
 
 Basic example for user input as strings
 
'''

# 1. Prompt User Input
# Declares the variable 'from_user' as a string with a value equal to what the
# user entered once prompted
from_user = raw_input("--Enter something: ")

# 2. Display User Input
# Prints what the user entered along with the type of variable it is
## Notice that this is always a string
print "You entered: "+from_user+" "+str(type(from_user))
