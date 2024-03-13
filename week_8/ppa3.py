# -*-coding:utf-8 -*-
"""
@File    :   ppa2.py
@Time    :   2024/03/14 01:32:55
@Author  :   Babul Kumar
@License :   (C)Copyright 2020-2021, Babul Kumar
@Desc    :   Write a recursive function named multiply accepts two positive integers a and
b as argument and returns their product. You can only use + and - operators. You are not allowed to use the * symbol anywhere in your code!
=================================================
  Input    :   2            | Output : 6
  Input    :   3            | Output : None
  Input    :   None         | Output : None
=================================================
"""


def multiply(a, b):
    """
    A recursive function to compute the product of two numbers

    Parameters:
        a, b: integers
    Return:
        result: integer
    """
    if b == 1:
        return a
    else:
        return a + multiply(a, b - 1)


p = 2
m = 3
print(multiply(a=p, b=m))
