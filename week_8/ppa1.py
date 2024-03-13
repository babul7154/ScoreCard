# -*-coding:utf-8 -*-
"""
@File    :   ppa1.py
@Time    :   2024/03/13 23:58:43
@Author  :   Babul Kumar
@License :   (C)Copyright 2020-2021, Babul Kumar
@Desc    :   Write a recursive function named triangular that accepts a positive integer n as argument and returns the sum of the first n positive integers.
You do not have to accept input from the user or print the output to the console. You just have to write the function definition.
=================================================
  Input    :   5            | Output : 15
  Input    :   10           | Output : 55
  Input    :   None         | Output : None
=================================================
"""


def triangular(n):
    """
    Compute the sum of the first n positive integers.

    Parameters:
        n: integer
    Return:
        result: integer
    """
    if n == 1:
        return 1
    else:
        return n + triangular(n - 1)


print(triangular(n=5))
