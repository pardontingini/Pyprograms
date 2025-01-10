#Can execute a set of statements as long as condition is true
#NB - positioning increment is crucial !
"""""
#Print i as long as i is less than 6
i = 1 #while loop requires relevant indexing variables to be defined i.e i = 1
 while i < 6:
    print(i)
    i += 1 #increments i so that the loop will not continue forever
"""
#The break statement - stops the loop even if the while condition is true:
"""i = 1 
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
"""
"""
#Continue statement -stops the current iteration, and continue with the next
i = 1 
while i < 6:
    print(i)
    if i == 3:
        continue
    i += 1
"""
#Use the else statement
i = 1 
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6") 