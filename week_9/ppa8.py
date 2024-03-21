# -*-coding:utf-8 -*-
"""
@File    :   ppa8.py
@Time    :   2024/03/22 02:28:37
@Author  :   Babul Kumar
@License :   (C)Copyright 2020-2021, Babul Kumar
@Desc    :   The scores of a class of students in the online degree program is represented as a CSV file with the following header:

Name,Gender,CT,Python,PDSA
The name of the file is given by the variable filename. The first line will be the header.

Write a function named improvement which accepts the filename as argument. It should return the number of students whose scores have increased across the three courses. That is, the number of students whose scores are in this order: CT < Python < PDSA.

(1) filename is a string variable that holds the filename. For example, in the first test case, it is public_1.txt.

(2) You do not have to accept input from the console. You just have to write the function definition.
=================================================
  Input    :   None         | Output : None
  Input    :   None         | Output : None
  Input    :   None         | Output : None
=================================================
"""
import csv


def improvement(filename):
    """
    Find all students who have shown an improvement

    Argument:
        filename: string, path to file
    Return:
        count: integer
    """
    f = open(filename)
    file_content = csv.DictReader(f)
    # next(file_content)
    s = 0
    for data in file_content:
        if int(data["CT"]) < int(data["Python"]) < int(data["PDSA"]):
            s += 1
    return s


p = "location of file"
print(improvement(filename=p))
#! please note that data in DictReader is of string format,even the value is  integer type.
#! we can solve this problem using csv.reader with next(object)
