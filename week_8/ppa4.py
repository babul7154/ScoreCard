# -*-coding:utf-8 -*-
"""
@File    :   ppa4.py
@Time    :   2024/03/19 00:23:41
@Author  :   Babul Kumar
@License :   (C)Copyright 2020-2021, Babul Kumar
@Desc    :   Consider a positive integer x that is a power of 2. The logarithm of x to the base 2 is the number of times 2 has to be multiplied with itself so getx, and is denoted by log2 (x). For example, log2(4)=2 . Note that log2(1)=0 .

Write a recursive function named logarithm that accepts this positive integer x as argument
and returns log2(x).

(1) Each test case will be a power of 2.

(2) Use of Python's standard libraries is not allowed for this problem.

(3) You do not have to accept input from the user or print the output to the console. You just have to write the function definition.

(4) Note that the logarithm is also defined for numbers which are not powers of 2
2. We have restricted it to powers of 2 so as to keep things simple.
=================================================
  Input    :   4           | Output : 2
  Input    :   16          | Output : 4
  Input    :   None        | Output : None
=================================================
"""


def logarithm(x):
    """
    A recursive function to compute the log of x

    Parameters:
        x: integer
    Result:
        result: integer
    """
    if x == 1:
        return 0
    else:
        return 1 + logarithm(x // 2)


p = 4
print(logarithm(x=p))
