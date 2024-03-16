# -*-coding:utf-8 -*-
"""
@File    :   week8 que3.py
@Time    :   2024/03/16 20:45:28
@Author  :   Babul Kumar
@License :   (C)Copyright 2020-2021, Babul Kumar
@Desc    :   Write a recursive function named non_decreasing that accepts a non-empty list L of integers as argument and returns True if the elements are sorted in non-decreasing order from left to right, and False otherwise.

You do not have to accept input from the user or print the output to the console. You just have to write the function definition.
=================================================
  Input    :   [1, 10, 100, 1000]         | Output : True
  Input    :   [10, 1, 100, 1000, 10000]  | Output : False
  Input    :   None         | Output : None
=================================================
"""


def non_decreasing(L):
    """
    A recursive function that determines if L is sorted in non-decreasing order

    Argument:
        L: list of integers
    Return:
        result: bool
    """
    if len(L) <= 1:
        return True
    elif L[-2] > L[-1]:
        return False
    else:
        return non_decreasing(L[:-1])


p = [10, 1, 100, 1000, 10000]
print(non_decreasing(L=p))
