# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 22:26:06 2020

@author: Mbongiseni Dlamini
"""

# let's practice some strings and assignments

name = "Senzo"
surname = "Zulu"
print(name,surname)


"""
let's refresh conditional statements
let's recall functions
"""
def odd(x):
    """Returns "yes" if x is odd and no otherwise"""
    if x % 2 == 1:
        print("Yes")
    else:
        print("No")
        
def sum(y):
    """returns the sum of the first x numbers staring from 1"""
    sum = 0
    for count in range(1,y):
        sum += count # add sum to count and store in sum
    print(sum ) 

def sum_of_inputs():
    s=0
    while True:
        data = input("enter a number or q to quit: ")
        if data == "q":
            break
        s+= float(data) #add s to count and store in s
    print("Sum was: ", s)
        
def main():
    """ main function """


    """
    input() function gets user input and float() converts user input to-
    be a floating point number.
    """
    radius = float(input("Enter a radius:"))  
    print(radius) # prints out stuff
    
    """
    let's play with the math module
    """
    import math
    area = math.pi*math.sqrt(radius)
    print("Area is: ",area)
    print(math.log(2))
    print(math.pow(3,3))
    
    r = int(input("Enter a number: ")) #convert input to int
    print("Is ", r, " odd? " )
    odd(r)
    sum_of_inputs()
    t = int(input("Enter a number: ")) #convert input to int
    sum(t)


main()        