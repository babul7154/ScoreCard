# -*-coding:utf-8 -*-
"""
@File    :   grpa5.py
@Time    :   2024/03/23 00:15:15
@Author  :   Babul Kumar
@License :   (C)Copyright 2020-2021, Babul Kumar
@Desc    :   Write a function named num_to_words that accepts a square matrix of single digit numbers as argument. Within the function, create a file named words.csv. Write the matrix to the file by replacing the digits with their corresponding words. For example, num_to_words([[1, 2], [3, 4]]) should create the file words.csv with the following contents:

one,two
three,four
Note that the matrix will only have integers from 0 to 9, endpoints inclusive.

(1) You do not have to accept input from the user or print the output to the console. You just have to write the function definition. However, within the function, you have to create a file named words.csv and write to it.

(2) The last line of the file should not end with a '\n'. The last character of every other line in the file should end with a '\n'. This is a convention that we will be following in all questions that ask you to write to a file.
=================================================
  Input    :   None         | Output : None
  Input    :   None         | Output : None
  Input    :   None         | Output : None
=================================================
"""
import csv


def num_to_words(mat):
    """
    Convert matrix to file

    Argument:
        mat: list of lists
    Return:
        None
    """
    predef_dict = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        0: "zero",
    }
    f = open("words.csv", "w")
    file_content = csv.writer(f)
    for i in range(len(mat)):
        lst = list()
        for j in range(len(mat)):
            lst.append(predef_dict[mat[i][j]])
        file_content.writerow(lst)


mat = [[1, 2], [3, 4]]
print(num_to_words(mat=mat))
