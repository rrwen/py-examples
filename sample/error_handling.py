'''

 error_handling.py
 Richard Wen (init.r.w@gmail.com)
 
 Dependencies: Python 2.7
 Developed on: Windows 7 32-bit
 
===============================================================
 
 Basic error handling with try/except example in Python
 
'''

# 1. Try to combine strings
## This works with no error messages
try:
    print "Combining strings " + " work!"
except:
    print "This message will not appear because the try statement will always work"

# 2. Try to combine a string and a number
## This does not work, and will display an error message
## The program will still keep running and see it as an exception
## If error handling was not implemented, the program will stop
try:
    print "a string" + 50
except:
    print "Error: String and numbers can not be combined"
print "Program continues to run here"
