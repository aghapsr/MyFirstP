# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 09:34:36 2026

@author: Admin
"""
while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter operation (+ - * /): ")

    if op == "+":
        result= num1 + num2
        print(f"Result: {result}")
    
    elif op == "-":
        result = num1 - num2
        print(f"Result: {result}")
    elif op == "*":
        result = num1 * num2
        print(f"Result: {result}")
            
    elif op == "/":
        if num2 !=0:
            result = num1 / num2
            print(f"Result: {result}")
        else:
            print("I can't do that :(")
    else:
            print("Invalid operation")
    again = input("Do you want to continue? (yes/no): ")
    if again == "no":
        print("Goodbye!")    
        break
        
