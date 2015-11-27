'''

 loops.py
 Richard Wen (init.r.w@gmail.com)
 
 Dependencies: Python 2.7
 Developed on: Windows 7 32-bit
 
===============================================================
 
 Loops example in Python
 
'''

# 1. For loop
## Loops through items in the variable "grocery_list"
## Adds the string " x 1" and displays the item
grocery_list = ["tomatoes","apples","milk","chicken","pasta","eggs"]
for item in grocery_list:
    print item+" x 1"

# 2. For loop indices
## Loops through the indice references for variable "user_list"
## Displays user id for each user name 
user_list = ["veronica", "bob", "joe", "george","bob","joe","joe"]
for index in range(len(user_list)):
    print "user id for "+user_list[index]+" is",index

# 3. While loop
## Loops code underneath while condition:
## This will loop until the condition is false (it will keep running if the condition is true)
## Careful when using this, as it can easily lead to unwanted infinite loops if the condition is never false
x = 1
while x<10:
    print x," is not 10 yet.."
    x+=1
print x, "is equal to 10 now!"