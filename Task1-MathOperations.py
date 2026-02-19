
"""
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
    o	Addition
    o	Subtraction
    o	Multiplication
    o	Division
3.  Displays the results of each operation on the screen.

"""

#get two numbers from users
num1=int(input("Emter the first number:"))
num2=int(input("Emter the second number:"))

add_result=num1+num2        #addtion
sub_result=num1-num2        #subtraction
mult_result=num1*num2       #multiplication/product
div_result=num1/num2        #division

#display the desired result on screen
print("Addition:",add_result)
print("Subtraction:",sub_result)
print("Multiplication:",mult_result)
print("Division:",div_result)
