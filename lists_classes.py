# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 20:38:14 2020

@author: Mbongiseni Dlamini
"""
def sums(list1):
    """ prints the sum of the items in the list"""
    su = 0
    for element in list1:
        su+=element
        
    return su

def has_duplicates(list2):
    """checks if list has duplicates"""
    for count in range(0,len(list2)-1):
        if list2[count] in list2[count+1:len(list2)-1]:
            print("Has duplicate value ",list2[count])
            
        else:
            print("no duplicates!")
"""
CLASSES
"""            
class Employee: #define a class

    raise_amount = 1.06 # class variable
    
    def __init__(self,fname,lname,pay): #constructor, sets our attributes
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + "." + lname + "@company.com"
        
    def __str__(self): #builds string version of an object's state
        return self.lname + " " + self.fname
    def appply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        

class developer(Employee): # create a subclass of employee
    """ inherits all the functionality of Employee"""
    def __init__(self,fname,lname,pay,prog_lang): # redefine the init method for this subclass
        super().__init__(fname, lname, pay) #call superclass's init method to contruct the names and pay
        self.prog_lang = prog_lang #construct programing language

def main():
    """ main function for this script"""
    my_list = [1,2,3,4,5,5,4,6] # create a list
    my_list.append(1) # enter element 1 into the first position in  the list
    print(my_list)
    list_2 = [9,10,111,12]
    my_list.extend(list_2) # add a list to the end of current list
    print(my_list)
    print(sums(my_list))
    has_duplicates(my_list)
    
    emp_1 = Employee('Sam','Peterson',4000)   # define an instance of the class
    emp_2 = Employee('Themba','Dlamini',8000)
    print(emp_1) #we check if emp1 is an instance of Employee
    print(emp_2)
    print(emp_1.pay) #excess the pay attribute
    emp_1.appply_raise() 
    print(emp_1.pay) #excess the pay attribute
    print(emp_2.__dict__) # tells us details about emp_2
    
    dev1 = developer('Mike','Johnson',8000,'python') # call an instance of developer
    print(dev1.__dict__)
    
 
    
main()    
