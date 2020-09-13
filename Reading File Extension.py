# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 10:32:43 2020

@author: user
"""

a = input("Input the Filename: ")
s = a.split('.')

if(s[1]=="py"):
    print("The extension of file is :" + "Python")
elif(s[1]=="java"):
     print("The extension of file is :" + "Java")
elif(s[1]=="js"):
     print("The extension of file is :" + "Javascript")
elif(s[1]=="txt"):
     print("The extension of file is :" + "text")
else:
    print("File Extension Not Found")
    
    
