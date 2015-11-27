'''

 if_else.py
 Richard Wen (init.r.w@gmail.com)
 
 Dependencies: Python 2.7
 Developed on: Windows 7 32-bit
 
===============================================================
 
 Conditional statements example in Python
 
'''

# 1. If statement
## If statements run code underneath it when its logic is true
if 1==1:
    print "This message appears, because 1 is equal to 1"
    
# 2. Else statement
## Else statements are useful to run code for all other conditions not mentioned
if 1==2:
    print "This message wil not appear, 1 is never equal to 2"
else:
    print "This message appears since the if statement above it is not met"

# 3. Else if statement
## Else if statements are useful to reduce if checks, and to run code when
## certain if statements above it are not met
if 1==2:
    print "This message wil not appear, 1 is never equal to 2"
elif 2==2:
    print "This message appears since the if statement above it is not met and 2 is equal to 2"
