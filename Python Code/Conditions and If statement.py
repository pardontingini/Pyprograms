#Conditional Statements -runs the code when the if statement is true...or else and elif
#Python supports the usual logical conditions from mathematics:
#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b

age = int(input("enter your age:  "))
print("Your age is", age, )
herage = int(input("what is her age?:  "))

#if herage < age-5:
    #print("She might be too young for you buddy!")
#elif herage > age+2:
    #print("might be too old for ya kiddo! ")
#else:
    #print("She might be your soulmate, mate :-))")

#Ternary Operations/ Conditional Expressions - for if...else statement
#print("she is a baby" if herage < age-5 else "try it out man, who knwows!")

#One line multiple conditions
#print("too young") if herage < age-5 else print("too old") if herage > age+2 else print("Soulmate!!")

#Using Logical operators
#if herage < age-5 or herage > age+2:
    #print("not fo you bro!")

#if not herage < age-5 and herage > age+2:
    #print("might fo you bro!")

#Nested IF statements
#if herage < 18:
    #print("underage man!")
    #if not herage < age-5 or herage > age+2:
        #print("not for you bro!")
    #else:
        #print("thats your woman right there!")
#The Pass Statement - used when your if statement has no content
#a = 33
#b = 200
#if b > a:
    #pass