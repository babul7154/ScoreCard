# -*-coding:utf-8 -*-
"""
@File    :   ppa5.py
@Time    :   2024/03/21 21:46:51
@Author  :   Babul Kumar
@License :   (C)Copyright 2020-2021, Babul Kumar
@Desc    :   filename points to a file that contains a nxn matrix. The ith  line of the file represents the (i-1)th  row of the matrix as a sequence of comma separated integers, where 1≤i≤n. We have used zero-based indexing here. This file doesn't have a header and has exactly n lines. A sample file is given for your reference:
1,2,3
4,5,6
7,8,9
Your task is to return the matrix [[1, 2, 3], [4, 5, 6], [7, 8, 9]].

Write a function named get_matrix that accepts the filename as argument. It should return the matrix as a list of lists. Each cell of the matrix should be an integer and not a string.

(1) filename is a string variable that holds the name of the file. For example, in the first test case, it is filename = 'public_1.txt'.

(2) You do not have to accept input from the console or print the output. You have to write the function definition.
=================================================
  Input    :   None         | Output : None
  Input    :   None         | Output : None
  Input    :   None         | Output : None
=================================================
"""
import csv


def get_matrix(filename):
    """
    Convert the contents of the file into a matrix

    Argument:
        filename: string
    Return:
        matrix: list of lists
    """
    f = open(filename)
    file_content = csv.reader(f)
