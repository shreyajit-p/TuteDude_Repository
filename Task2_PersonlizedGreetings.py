"""
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
"""
#Get firstname and last name from the user
fname=input("Enter your first name:")
lname=input("Enter your last name:")

#concatinate them to make a full name
name=fname+" "+lname+"!"

#display the result
print("Hello",name,"Welcome to the Python program.")