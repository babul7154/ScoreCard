# -*-coding:utf-8 -*-
"""
@File    :   ppa7.py
@Time    :   2024/03/22 02:03:08
@Author  :   Babul Kumar
@License :   (C)Copyright 2020-2021, Babul Kumar
@Desc    :   filename points to the name of some text file. Each line in this file is missing a period at the end of the line. Write a function named add_period that accepts filename as argument and creates a new file named out.txt. The function should copy the contents of filename into out.txt and add a period at the end of each line.

(1) filename is a string variable that holds the filename. For example, in the first test case, it is public_1.txt.

(2) You do not have to accept input from the console. You have to write the function definition and within the function, create a file named week9ppa7out.txt according to the required specification.
=================================================
  Input    :   None         | Output : None
  Input    :   None         | Output : None
  Input    :   None         | Output : None
=================================================
"""


def add_period(filename):
    """
    Add a period at the end of each line

    Argument:
        filename: string; path of the file
    Return:
        None
    """
    f = open(filename)
    file_content = f.read().splitlines()
    f1 = open("week9ppa7out.txt", "w")
    for data in file_content:
        f1.write(data + ".")
        f1.write("\n")


p = "filename\\week9ppa7.txt"
print(add_period(filename=p))
