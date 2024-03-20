# -*-coding:utf-8 -*-
"""
@File    :   ppa1.py
@Time    :   2024/03/19 20:33:38
@Author  :   Babul Kumar
@License :   (C)Copyright 2020-2021, Babul Kumar
@Desc    :   Write a function named read_file that accepts a text file named filename as argument. Within the function, read the file and print each line of the file on a separate line in the console. You shouldn't print any extra characters at the end of a line. There shouldn't be an empty line between any two consecutive lines.

(1) filename is a string variable that holds the name of the file. For example, in the first test case, it is filename = 'public_1.txt'.

(2) You do not have to accept input from the console. You have to write the function definition and print the contents of the file within the function.
=================================================
  Input    :   None         | Output : None
  Input    :   None         | Output : None
  Input    :   None         | Output : None
=================================================
"""


def read_file(filename):
    """
    Read the file and print each line

    Argument:
        filename: string, name of the file to be read
    Return:
        None
    """
    f = open(filename, "r")
    file = f.read()
    print(file)


p = "filename_location"
print(read_file(filename=p))
