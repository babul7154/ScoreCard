# -*-coding:utf-8 -*-
"""
@File    :   ppa3.py
@Time    :   2024/03/21 02:06:53
@Author  :   Babul Kumar
@License :   (C)Copyright 2020-2021, Babul Kumar
@Desc    :   Write a function named get_max_line that accepts a text file named filename as argument. Each line in this file contains an integer. The function should return the line number that houses the maximum integer in the file. If multiple lines have the same maximum number, return the smaller of the two. Line numbers start from one and not zero.

(1) filename is a string variable that holds the name of the file. For example, in the first test case, it is filename = 'public_1.txt'.

(2) You do not have to accept input from the console or print the output. You have to write the function definition.
=================================================
  Input    :   None         | Output : None
  Input    :   None         | Output : None
  Input    :   None         | Output : None
=================================================
"""


def get_max_line(filename):
    """
    Get the line that houses the maximum value

    Argument:
        filename: string, path to the file
    Return:
        result: integer
    """
    f = open(filename)
    file_content = f.read().splitlines()
    maxi = max(file_content)
    dct = dict()
    # max_no=list()
    for i in range(len(file_content)):
        if file_content[i] == maxi:
            dct.update({i + 1: maxi})
    lst = list(dct.keys())[0]
    return lst


p = "loction of file"
print(get_max_line(filename=p))
