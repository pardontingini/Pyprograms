##Lists - used to store multiple items in a single variable.
#List items are ordered, changeable, and allow duplicate values.

#Create a list
#players = ['Ronaldo', 'Messi', 'Salah', 'Mane', 'Ronaldo', 'KDB', 12, 2.5]
#print(players)
#List can contain any data type

#To determine how many items a list has, use the len() function:
#print( 'this list has', len(players), ', players')

#lists are defined as objects with the data type 'list'

#It is also possible to use the list() constructor when creating a new list.
fruits = list(("apple", "banana", "cherry")) # note the double round-brackets
print(fruits)

#can use index number to access an item in a list
#print(thislist[0])
#print(thislist[0 : 2])

#change item by indexing
fruits[2] = 'avocado'
print(fruits)

#add using append fucntion
fruits.append("guava")
print(fruits)

#Dleteing an index item
del fruits[3]
print(fruits)