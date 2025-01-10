#functions help you not to repeat defining a
#A function is a block of code which only runs when it is called.
#You can pass data, known as parameters, into a function.
#A function can return data as a result.

"""
def main(): #use a def keyword to define a function
    name = input("Whats your name? ")
    hello()

def hello(name):
    print("hello,", )

main() # calling the function
"""
"""
#parity 
def main():
    x = int(input("Enter X: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

#Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. 
# You can add as many arguments as you want, just separate them with a comma.
# Arguments are often shortened to args in Python documentations.

def is_even(n):
    if n % 2 == 0:
        return True #boolean type
    else:
        return False

main()

def main():
    x = int(input("Enter X: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

#Improving the code
def is_even(n):
    return n % 2 == 0 #since booleaan is straight forward you can just return 

main()
"""
#The terms parameter and argument can be used for the same thing: 
# information that are passed into a function.
# From a function's perspective:
    # A parameter is the variable listed inside the parentheses in the function definition.
    # An argument is the value that is sent to the function when it is called.
#by default a function must be called with the correct number of arguments.
#NB use * if the number of arguments is unknown!

#List as a parameter

def players(mid):
    for p in mid:
        print(p)
great_players = ["modric", "zidane", "Lampard", "Iniesta", "KDB"]
players(great_players)