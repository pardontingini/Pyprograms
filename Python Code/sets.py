#sets are used to store multiple items ina single variable.
#collection which is unodered and unindexed - can remove and add items.
nameset = {'Pardon', 'Nodrap', 'Tinglar'}
print(nameset)
exset = set (('ashy', 'bev', 'clar','diana' )) #use set() constructor - double round brackets 
print(exset)

#accessing items

for x in exset:
    print(x) #can use a for loop to access items

print("bev" in exset) # can use in keyword to check if available.

#adding items
exset.add("natty")
print(exset)
nameset.update(exset) # adds items from another iterable source(tuples, lists, dictionaries etc)
print(nameset)

#removing
nameset.remove('Tinglar')
print(nameset)

exset.discard('ashy')
print(exset)

x = exset.pop() #randomly removes an item since they are unordered
print(x)
print(exset)

nameset.clear()

del nameset

#Joining Sets
#The union() and update() methods joins all items from both sets.
#The intersection() method keeps ONLY the duplicates.
#The difference() method keeps the items from the first set that are not in the other set(s).
#The symmetric_difference() method keeps all items EXCEPT the duplicates.
allnameset = exset.union(nameset)
allnameset = exset | nameset

allnameset = exset.intersection(nameset)
allnameset = exset & nameset

allnameset = exset.difference(nameset)
allnameset = exset - nameset

allnameset = exset.symmetric_difference(nameset)
allnameset = exset ^ nameset

#Method	Shortcut	Description
#add()	 	Adds an element to the set
#clear()	 	Removes all the elements from the set
#copy()	 	Returns a copy of the set
#difference()	-	Returns a set containing the difference between two or more sets
#difference_update()	-=	Removes the items in this set that are also included in another, specified set
#discard()	 	Remove the specified item
#intersection()	&	Returns a set, that is the intersection of two other sets
#intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
#isdisjoint()	 	Returns whether two sets have a intersection or not
#issubset()	<=	Returns whether another set contains this set or not
# 	        <	Returns whether all items in this set is present in other, specified set(s)
#issuperset()	>=	Returns whether this set contains another set or not
# 	        >	Returns whether all items in other, specified set(s) is present in this set
#pop()	 	Removes an element from the set
#remove()	 	Removes the specified element
#symmetric_difference()	^	Returns a set with the symmetric differences of two sets
#symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
#union()	|	Return a set containing the union of sets
#update()	|=	Update the set with the union of this set and others