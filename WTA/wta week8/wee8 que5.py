# -*-coding:utf-8 -*-
"""
@File    :   wee8 que5.py
@Time    :   2024/03/16 22:00:00
@Author  :   Babul Kumar
@License :   (C)Copyright 2020-2021, Babul Kumar
@Desc    :   Write a recursive function named search that accepts the following arguments:

(1) L: a sorted list of integers

(2) k: integer

The function should return True if k is found in the list L, and False otherwise.
=================================================
  Input    :   [1, 2, 3, 4]         | Output : True
  Input    :   2                    | Output : None
  Input    :   None                 | Output : None
=================================================
"""


def search(L, k):
    """
    A recursive function that searches for an element k in L

    Arguments:
        L: list
        k: int
    Return:
        bool
    """
    if len(L) == 0:
        return False
    mid = len(L) // 2
    if L[mid] == k:
        return True
    elif L[mid] < k:
        return search(L[mid + 1 :], k)
    else:
        return search(L[:mid], k)


p = [1, 2, 3, 4]
m = 2
print(search(L=p, k=m))
