# -*-coding:utf-8 -*-
"""
@File    :   ppa2.py
@Time    :   2024/03/19 21:22:34
@Author  :   Babul Kumar
@License :   (C)Copyright 2020-2021, Babul Kumar
@Desc    :   Write a function named read_line that accepts a text file named filename and a positive integer n as arguments. Within the function, read the file and return the nth line of the file. If the file has fewer than n lines, return the string 'None'.

(1) filename is a string variable that holds the name of the file. For example, in the first test case, it is filename = 'public_1.txt'.

(2) You do not have to accept input from the console or print the output. You have to write the function definition.
=================================================
  Input    :   None         | Output : None
  Input    :   None         | Output : None
  Input    :   None         | Output : None
=================================================
"""


def read_line(filename, n):
    """
    Read the nth line of the file

    Argument:
        filename: string, name of the file to be read
    Return:
        string: return nth line of the file
    """
    f = open(filename)
    file_content = f.read().splitlines()
    if len(file_content) < n:
        return "None"
    else:
        return file_content[n - 1]


p = "location of file"


print(read_line(filename=p, n=3))
