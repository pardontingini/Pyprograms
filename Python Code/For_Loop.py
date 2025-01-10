"""
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
"""
boys = ["nodrap","Jay Vee", "Klag", "Stabz", "Willie"]
for guys in boys:
    print(guys)
    if guys == "Klag":
        break # if there is a break statement, the else statement will not be executed
    else:
        print("Completed process")
