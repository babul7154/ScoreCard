# -*-coding:utf-8 -*-
"""
@File    :   week8 que1.py
@Time    :   2024/03/16 21:44:59
@Author  :   Babul Kumar
@License :   (C)Copyright 2020-2021, Babul Kumar
@Desc    :   Write two functions named spiral_iterative and spiral_recursive, each of which accepts three arguments:

left: x-coordinate of the point P0
right: x-coordinate of the point P1
n: the number of arms in the spiral
Both functions should return the the x-coordinate of Pn , the point at which the ℎ nth  arm of the spiral ends.
=================================================
  Input    :   0,1,4         | Output : 0.625
  Input    :   None          | Output : None
  Input    :   None          | Output : None
=================================================
"""


def spiral_iterative(left, right, n):
    """
    An iterative function to compute the x-coordinate of the nth arm of the spiral

    Arguments:
        left: integer
        right: integer
        n: integer
    Return:
        result: float
    """
    if n == 0:
        return left
    if n == 1:
        return right
    p = 0
    for i in range(n - 1):
        left = right
        right = (left + right) // 2
    return right


def spiral_recursive(left, right, n):
    """
    An recursive function to compute the x-coordinate of the nth arm of the spiral

    Arguments:
        left: integer
        right: integer
        n: integer
    Return:
        result: float
    """
