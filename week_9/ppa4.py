# -*-coding:utf-8 -*-
"""
@File    :   ppa4.py
@Time    :   2024/03/21 02:34:56
@Author  :   Babul Kumar
@License :   (C)Copyright 2020-2021, Babul Kumar
@Desc    :   filename points to a CSV file that has two columns. The first column is the name of a student, the second column is this student's age. The first line of the file will always be the header. A sample file is given below for your reference:

Name,Age
Arti,20
Kalam,60
Atul,25
Krishnan,24
Sahana,20
Write a function named get_dict that accepts the filename as argument and returns a dictionary where the keys are the student names and the values are the corresponding ages of the students.

(1) filename is a string variable that holds the name of the file. For example, in the first test case, it is filename = 'public_1.txt'.

(2) You do not have to accept input from the console or print the output. You have to write the function definition.
=================================================
  Input    :   None         | Output : None
  Input    :   None         | Output : None
  Input    :   None         | Output : None
=================================================
"""
import csv


def get_dict(filename):
    """
    Convert the contents of the file into a dict

    Argument:
        filename: string, path of the file
    Return:
        result: dict; keys are strings, values are integers
    """
    f = open(filename)
    file_content = csv.reader(f)
    next(file_content)
    ndict = dict()
    for row in file_content:
        ndict.update({row[0]: int(row[1])})
    return ndict


file_1 = "location of file"
print(get_dict(filename=file_1))
