# -*-coding:utf-8 -*-
"""
@File    :   grpa1.py
@Time    :   2024/03/22 18:30:04
@Author  :   Babul Kumar
@License :   (C)Copyright 2020-2021, Babul Kumar
@Desc    :   filename is a text file that contains a collection of words in lower case, one word on each line. Write a function named get_freq that accepts filename as argument. It should return a dictionary where the keys are distinct words in the file, the values are the frequencies of these words in the file.

For example, given the following file:

good
great
good
work
work
The dictionary returned should be:

{'good': 2, 'great': 1, 'work': 2}
The order in which the words are added to the dictionary doesn't matter.

(1) filename is a string variable that holds the name of the file. For example, in the first test case, it is filename = 'public_1.txt'.

(2) You do not have to accept input from the console or print the output to the console. You just have to write the function definition.
=================================================
  Input    :   None         | Output : None
  Input    :   None         | Output : None
  Input    :   None         | Output : None
=================================================
"""


def get_freq(filename):
    """
    Extract frequency information from the file

    Argument:
        filename: string, path to file
    Return:
        result: dictionary; keys are strings, values are integers
    """
    f = open(filename)
    file_content = f.read().splitlines()
    ndict = dict()
    for data in file_content:
        ndict.update({data: file_content.count(data)})
    return ndict


p = "location of file"
print(get_freq(filename=p))
