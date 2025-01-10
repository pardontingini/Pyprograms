#Tuple - used to store multiple items in a single variable
#tuples are ordered and unchangeable. Allows duplicate members. They are Indexed
# create a tuple
players = ('Foden', 'Lewis', 'Bobb', 'McAtee') #use round brackets
players2 = 'Edeson', 'Ortega' #brackets are optional
#print(players)
#print(players2)

#create a tuple with 1 item- add a comma after
players3 = 'Edeson',
#print(players3) 

#can use the tuple() constructor
players4 = tuple(('Edeson', 'Ortega', 'Carson', 'Steffen'))#note double round brackets
print(players4)

#List inside tuple
#mixed = ('food', [8, 1, 8])
#print(mixed)

#access item - use indexing. can also use negative indexing to start from the end
#print(mixed[1])
#print(mixed[0 : 2])
#Remember that the last item has the index -1,

#check if item is presnt in a tuple - use in function
if "Lewis" in players:
 print('Yes, Lewis is a great player')

#update tuple items - tuples are unchangeable/immutable
#You can convert the tuple into a list, change the list, and convert the list back into a tuple.
goalkeepers = list(players2)
goalkeepers.append('Carson')
print(goalkeepers)

players2 = tuple(goalkeepers)
print(players2)

#tuple concatenation
mancity = players + players2
print(mancity)

#Unpacking a tuple: extracting values back into variables.
#(Ederson_M, S_Ortega, S_Carson, Z_Steffen) = players4
#print(Ederson_M)
#print(S_Ortega)
#print(S_Carson)
#print(Z_Steffen)
#NB: If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list

#Loop Through a Tuple - You can loop through the tuple items by using a for loop.
#for club in mancity:
 #print(club)
#You can also loop through the tuple items by referring to their index number.
#for club in range(len(mancity)):
 #print(mancity[club])
#Using a While Loop
club = 0
while club < len(goalkeepers):
 print(goalkeepers[club])
 club = club + 1

#Tuple Methods
#1 count() - returns the number of times a specified value occurs in a tuple
#2 index() - searches the tule for a specified value and retyrsns the position of where it was found
