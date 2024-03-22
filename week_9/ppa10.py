# -*-coding:utf-8 -*-
"""
@File    :   ppa10.py
@Time    :   2024/03/22 17:32:23
@Author  :   Babul Kumar
@License :   (C)Copyright 2020-2021, Babul Kumar
@Desc    :   Write a function named number_grid that accepts two positive integers m & n as arguments. Within the function, create a file named numgrid.csv. Write the first mn positive integers to the file in the
following way:

Each line should be a sequence of n comma-separated integers.

There should be a total of m lines in the file.

For example, for the case of m=5,n=3, the file should be:

1,2,3
4,5,6
7,8,9
10,11,12
13,14,15
=================================================
  Input    :   None         | Output : None
  Input    :   None         | Output : None
  Input    :   None         | Output : None
=================================================
"""
import csv


def number_grid(m, n):
    """
    Write a number grid to a file

    Arguments:
        m, n: positive integers
    Return:
        None
    """
    f = open("numgrid.csv", "w")
    file_content = csv.writer(f)
    newlst = list()
    p = 0
    for i in range(1, m + 1):
        lst = list()
        for j in range(1, n + 1):
            p += 1
            lst.append(str(p))
        file_content.writerow(x for x in lst)


print(number_grid(m=5, n=3))
