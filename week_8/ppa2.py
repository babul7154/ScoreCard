# -*-coding:utf-8 -*-
"""
@File    :   ppa2.py
@Time    :   2024/03/14 01:28:29
@Author  :   Babul Kumar
@License :   (C)Copyright 2020-2021, Babul Kumar
@Desc    :   The factorial of a positive integer n is defined as follows:
n!=1⋅2⋅3⋯n
Write a recursive function named factorial that accepts a positive integer n as argument and returns the factorial of n.

You do not have to accept input from the user or print the output to the console. You just have to write the function definition.
=================================================
  Input    :   3            | Output : 6
  Input    :   6            | Output : 120
  Input    :   None         | Output : None
=================================================
"""


def factorial(n):
    """
    Compute the factorial of n.

    Parameters:
        n: integer
    Return:
        result: integer
    """
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


p = 5
print(factorial(n=p))
