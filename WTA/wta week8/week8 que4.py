# -*-coding:utf-8 -*-
"""
@File    :   week8 que4.py
@Time    :   2024/03/16 21:15:52
@Author  :   Babul Kumar
@License :   (C)Copyright 2020-2021, Babul Kumar
@Desc    :   Write a recursive function named uniq that accepts a non-empty list L as argument and returns a new list after removing all duplicates from it. Your function must retain the last occurrence of each distinct element in the list.

You do not have to accept input from the user or print the output to the console. You just have to write the function definition.
=================================================
  Input    :   [1, 2, 3, 2, 1, 4]    | Output : [3, 2, 1, 4]
  Input    :   None                  | Output : None
  Input    :   None         | Output : None
=================================================
"""


def uniq(L):
    """
    A recursive function to get unique elements from the list

    Argument:
        L: list
    Return:
        result: list
    """
    if len(L) == 1:
        return L
    elif L[0] in L[1:]:
        return uniq(L[1:])
    else:
        return [L[0]] + uniq(L[1:])


p = [1, 2, 3, 2, 1, 4]
print(uniq(L=p))
