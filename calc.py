#!/usr/bin/python

# Lab 13
# Physics 91SI
# Spring 2016

import sys
import re

def main():
    """Join command-line arguments and pass them to unitcalc(), then print."""
    calculation = ''.join(sys.argv[1:])
    print calc(calculation)
    
#given two numbers and a calculation, returns the appropriate output    
def intermediate_result(num1, num2, operation):
        if operation=='+':
            return float(num1)+float(num2)
        elif operation=='-':
            return float(num1)-float(num2)
        elif operation=='*':
            return float(num1)*float(num2)
        elif operation=='/':
            return float(num1)/float(num2)    
def calc(s):
    """Parse a string describing an operation on quantities with units."""
    
    nums = []
    operations = []
    curr_index = 0
    while curr_index < len(s):
        if (not s[curr_index].isdigit()):
            nums.append(float(s[0:curr_index]))
            operations.append(s[curr_index])
            s = s[curr_index+1:len(s)]
            curr_index = 0
        curr_index += 1
    nums.append(float(s))        

    #at this point the lists nums and operations are populated with all the numbers and operations entered
    
    #checks for syntax
    assert(len(nums) >= 2)
    assert(len(operations) >= 1)
        
    #This does not take into account order of operations but instead just does the computations in the order they are written
    result = intermediate_result(nums[0], nums[1], operations[0])
    for i in range(2, len(nums)):
        result = intermediate_result(result, nums[i], operations[i-1])
        
    print(result)
     
        
if __name__ == "__main__": main()
