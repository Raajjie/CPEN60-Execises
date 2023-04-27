# -*- coding: utf-8 -*-
"""10.25.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Wa-RHnY1-eKQUuApGWPqFI-Yz4mMKpg_
"""

#25. Write a program that finds all integer solutions to Pell’s equation x^2 − 2y^2 = 1, where x and y are between 1 and 100.

for x in range(1, 101):
    for y in range(1, 101):
        if x**2 - 2*y**2 == 1:
            print(f"x = {x}, y = {y}")