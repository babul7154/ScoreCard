# -*-coding:utf-8 -*-
"""
@File    :   grpa2.py
@Time    :   2024/03/22 19:26:12
@Author  :   Babul Kumar
@License :   (C)Copyright 2020-2021, Babul Kumar
@Desc    :   ou are given two non-empty text files file1 and file2 that have f1 and f2 lines respectively. Each file is a collection of ten-digit phone numbers, one number per line. It is also known that 0<f1<f2.


The following relations are defined on these two files:

Subset: file1 is a subset of file2 if the phone number in the ith line of file1 is equal to the number in the ith line of file2, for 1 ≤ i ≤ f1<f2.

Equal: file1 is equal to file2 if the phone number in the ith line of file1 is equal to the number in the ith
line of file2 for 1≤i≤f and f1=f2.

Write a function named relation that accepts these two text files as arguments. It should return the string Subset if file1 is a subset of file2. It should return Equal if file1 is equal to file2. If both these conditions are not satisfied, it should return the string No Relation.

(1) file1 and file2 are string variables that hold the names of the two files. For example, in the first test case, it is file1 = 'public_1_1.txt' and file2 = 'public_1_2.txt'.

(2) You do not have to accept input from the console or print the output to the console. You just have to write the function definition.

(3) The strings '9876543210' and '9876543210\n' are not the same, though the phone numbers are the same. So, strip the strings of all new lines using the strip method before checking for equality of two lines across the files
=================================================
  Input    :   None         | Output : None
  Input    :   None         | Output : None
  Input    :   None         | Output : None
=================================================
"""


def relation(file1, file2):
    """
    Determine the relationship between two files

    Arguments:
        file1, file2: strings, paths to two files
    Return:
        string: 'Equal', 'Subset' or 'No Relation'
    """
    f = open(file1)
    f_cont = f.read().strip()
    f1 = open(file2)
    f_cont1 = f1.read().strip()
    for i in range(len(f_cont)):
        for j in range(len(f_cont1)):
            if f_cont[i] == f_cont1[j] and i == j:
                if len(f_cont) == len(f_cont1):
                    return "Equal"
                else:
                    return "Subset"
            else:
                return "No Relation"


p = "location of file1"
m = "location of file2"
print(relation(file1=p, file2=m))
