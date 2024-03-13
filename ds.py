# -*-coding:utf-8 -*-
"""
@File    :   ds.py
@Time    :   2024/03/13 02:31:15
@Author  :   Babul Kumar
@License :   (C)Copyright 2020-2021, Babul Kumar
@Desc    :   The function minor_matrix takes three arguments: a square matrix M, and two non-negative integers i and j. The function’s purpose is to return a new matrix that is formed by removing the ith row and the jth column from the original matrix M.

The function works as follows:

First, it goes through each row in the matrix M.
If the current row’s index is not i, it includes this row in the new matrix. This way, the ith row is excluded from the new matrix.
Then, for each row in the new matrix, it goes through each element in the row.
If the current element’s index is not j, it includes this element in the current row. This way, the jth column is excluded from the new matrix.
The function finally returns the new matrix.

Please note that the indexing is zero-based, which means the indices start from 0. If the matrix M is of dimensions nxn, then i and j can be any integer from 0 to n-1.

Also, it’s assumed that the number of rows in M will be at least 3 in each test case. The function does not need to accept input from the user or print the output to the console. It simply returns the new matrix.
=================================================
  Input    :   3         | Output : 4,6
  Input    :   1,2,3     | Output : 7,9
  Input    :   4,5,6     | Output : None
  Input    :   7,8,9     | Output : None
  Input    :   0         | Output : None
  Input    :   1         | Output : None
=================================================
"""


def minor_matrix(M, i, j):
    """
    Compute the "minor matrix"

    Arguments:
        M: list of lists
        i: integer
        j: integer
    Return:
        M_ij: list of lists
    """
    new = list()
    for x in range(len(M)):
        if x == i:
            M.remove(M[i])
            for y in M:
                del y[j]
    return M


n = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(minor_matrix(M=n, i=0, j=1))
