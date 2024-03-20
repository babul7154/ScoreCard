# -*-coding:utf-8 -*-
"""
@File    :   ppa5.py
@Time    :   2024/03/19 00:40:34
@Author  :   Babul Kumar
@License :   (C)Copyright 2020-2021, Babul Kumar
@Desc    :   Write a recursive function named palindrome that accepts a string word as argument and returns True if it is a palindrome and False otherwise.

You do not have to accept input from the user or print the output to the console. You just have to write the function definition.
=================================================
  Input    :   mom            | Output : True
  Input    :   random         | Output : False
  Input    :   None           | Output : None
=================================================
"""


def palindrome(word):
    """
    A recursive function to determine if a string is a palindrome.

    Parameters:
        word: string
    Return:
        result: bool
    """
    if len(word) == 0 or len(word) == 1:
        return True
    if word[0] == word[-1]:
        return palindrome(word[1:-1])
    return False


p = "mom"
print(palindrome(word=p))
