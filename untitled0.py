# -*- coding: utf-8 -*-
"""
Created on Thu May 21 16:53:13 2026

@author: Admin
"""

age = int(input("How old are you?"))

if age >= 18:
    print("You are an adult")
else:
    print("You are NOT adult")
    
    
number = int(input("Enter a number: "))

if number > 10:
    print("Big number")
elif number >= 5 and number <=10:    # این یعنی بین 5 تا 10 (چون bigger than 10 قبلاً گرفته شده)
    print("Medium number")
else:                # else بدون شرط
    print("Small number")
    
    
number = int(input("Enter a number:"))
if number >= 18 and number <=50:
    print("Shoma mashmol khedmat sarbazi hastid")
elif number >= 1 and number <=17:
    print("Shoma hanoz mashmol nashodid")
else:
    print("Shoma moaf sodid")