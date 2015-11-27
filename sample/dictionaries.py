'''

 dictionaries.py
 Richard Wen (init.r.w@gmail.com)
 
 Dependencies: Python 2.7
 Developed on: Windows 7 32-bit
 
===============================================================
 
 Basic example for creating and using dictionaries
 
'''

# Declares the variable 'adictionary' as a dictionary data structure
## The first print statement shows the value for key1
## The second statement after that, adds key3 with a value of 3 to 'adictionary'
## The last statement prints the entire dictionary to show the changes
adictionary = {'key1' : 'value', 'key2': 20}
print adictionary['key1']
adictionary['key3'] = 3
print adictionary
