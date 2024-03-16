# -*-coding:utf-8 -*-
"""
@File    :   week8 que2.py
@Time    :   2024/03/16 20:21:59
@Author  :   Babul Kumar
@License :   (C)Copyright 2020-2021, Babul Kumar
@Desc    :   Write a recursive function named count that accepts the following arguments:

L: list of words
word: a word, could be any string
This function should return the number of occurrences of word in L.

(1) You cannot use the built-in count method for lists in this problem.

(2) All words will be in lower case.

(3) You do not have to accept input from the user or print the output to the console. You just have to write the definition of both the functions.
=================================================
  Input    :   ["good", "string", "good", "again", "good"] | Output : 3
  Input    :   None                                        | Output : None
  Input    :   None         | Output : None
=================================================
"""


def count(L, word):
    """
    A recursive function to compute the frequency of occurrences of word in L

    Arguments:
        L: list of words
        word: string
    Return:
        result: integer
    """
    if len(L) == 0:
        return 0
    elif L[-1] == word:
        return 1 + count(L[:-1], word)
    else:
        return count(L[:-1], word)


p = ["good", "string", "good", "again", "good"]
m = "good"
print(count(L=p, word=m))
