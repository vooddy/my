# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

Fin = open ( "D:\Программы на python\input.py.txt" ) 

Fout = open ( "D:\Программы на python\output.txt", "w" ) 

str = Fin.readline().split()

x, y = int(str[0]), int(str[1])

Fout.close() 
Fin.close()