#arithmetic,Comparison, logical, assignment, bitwise, conditional

##ARITHMETIC - used with numeric values to perfom methmetical operations e.g addition, subtarction etc
#print(100 + 70) #addition
#print(100 - 70) #subtraction
#print(100 * 70) #multiplication
#print(100 / 70) #division function - returns float answer
#print(70 % 60) #modulus operation - gives off remaindser only
#print(100 // 70) #floor division - gives integer number without decimal points
#print(10 ** 7) #exponential function - raising to the power

##COMPARIOSON/RELATIONAL operators - compares 2 objects and returns booolean values true or false answers
#[==, !=, >, <, >=, <=	]- returns true or false		
#print( 3 == 3) #Equal to
#print( 2 != 3) #Not equal to
#print( 3 > 3) #Greater than
#print( 3 < 3) #Less than
#print( 3 <= 3) #Greater than or equal to	
#print( 3 >= 4) #Less than or equal to	

##LOGICAL Operators - used to combine conditional statements
#[and, or, not]
#print(5 == 5 and 10 == 10) #returns True if both statements are ture
#print(10 == 5 and 10 == 10) #returns false
#print(10 == 5 or 10 == 10)#returns True if one of the statements is true
#print(not True) #returns reverse of logical result

##ASSIGNMENT Operators - used to assign values to variables 
##[+=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=, :=] 
#x = 10
#x += 5
#print(x)

#x = 5
#x /= 2
#print(x)

#x = 5
#x %= 2
#print(x)

##IDENTITY Operators - used to compare if objects are the same, with the same memory location
#Is operator - Returns true if both variables are the same
#x = ["apple", "banana"]
#y = ["apple", "banana"]
#z = x

#print(x is z) # returns True because z is the same object as x
#print(x is y) # returns False because x is not the same object as y, even if they have the same content
#print(x == y) # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

# Is not 
#print(x is not z)# returns False because z is the same object as x
#print(x is not y)# returns True because x is not the same object as y, even if they have the same content
#print(x != y)# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

##MEMBERSHIP Operators - used to test if a sequence is presented in an object
#x = ["apple", "banana"]
#in
#print("banana" in x)# returns True because a sequence with the value "banana" is in the list
#not in
#print("pineapple" not in x)# returns True because a sequence with the value "pineapple" is not in the list

##BITWISE Operators - used to compare (binary) numbers
#[&, |, ^, ~, <<, >> ]
#x & y #AND	Sets each bit to 1 if both bits are 1		
#x | y #OR	Sets each bit to 1 if one of two bits is 1		
#x ^ y #XOR	Sets each bit to 1 if only one of two bits is 1	
#~x	#NOT	Inverts all the bits	
#x << 2	  #Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	
#x >> 2>> #Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	

##CONDITIONAL OPERATORS
#name = 'Pardon'
#print("False!" if name != "Pardon" else "True!")

#Operator Precedence - describes the order in which operations are performed.
#   Order of precedence
#   Operator	Description	
#   ()	        Parentheses	
#   **	        Exponentiation	
#   +x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
#   *  /  //  %	Multiplication, division, floor division, and modulus	
#   +  -	    Addition and subtraction	
#   <<  >>	    Bitwise left and right shifts	
#   &	        Bitwise AND	
#   ^	        Bitwise XOR	
#   |	        Bitwise OR	
#   ==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
#   not	        Logical NOT	
#   and	        AND	
#   or	        OR

