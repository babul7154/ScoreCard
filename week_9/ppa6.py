# -*-coding:utf-8 -*-
"""
@File    :   ppa6.py
@Time    :   2024/03/22 00:23:11
@Author  :   Babul Kumar
@License :   (C)Copyright 2020-2021, Babul Kumar
@Desc    :   A sequence of n terms(a1,a2,..,an) is called an Arithmetic progression (AP) if the difference between any two consecutive terms stays constant. That is:
a2-a1 = a3-a2 = ..... = an-an-1 = d
Some useful terms:

a1  is the first term of the AP.
d is called the common difference of the AP.
n is the total number of terms in the AP.
Write a function named write_AP that accepts the following arguments:

a_1: first term of the AP, integer.
d: common difference of the AP, integer.
n: number of terms in the AP, positive integer.
Within the function, create a file named out.txt and write the first
n terms of the AP to it, one term on each line, starting from the first term.
=================================================
  Input    :   1         | Output : 1
  Input    :   3         | Output : 4
  Input    :   5         | Output : 7
  Input    :   None      | Output : 10
  Input    :   None      | Output : 13
=================================================
"""


def write_AP(a_1, d, n):
    """
    Write the AP to a file

    Arguments:
        a_1: first term, integer
        d: common difference, integer
        n: number of terms, integer
    Return:
        None
    """
    f = open(
        "out.txt", "w"
    )  # file_path = "your_directory_path/new_file.txt" in 'out.txt' for specified location
    lst = list()
    for i in range(1, n + 1):
        arth = a_1 + (i - 1) * d
        lst.append(arth)
    for i in lst:
        f.write(str(i))
        f.write("\n")


print(write_AP(a_1=1, d=3, n=5))
# this code will create out.txt file in working directory ,to create out.txt in specified directory
# use file_path = "your_directory_path/new_file.txt"
#! Note:
# ? (difference between mode='w' and mode='r')
# The file is opened in write mode (‘w’) using f=open('out.txt','w').
# This means that if the file “out.txt” already exists, it will be overwritten with the new content.

# The file is opened in append mode (‘a’) using f=open('out.txt','a').
# This mode ensures that if the file “out.txt” already exists, the new content will be added to the end of the existing content.
