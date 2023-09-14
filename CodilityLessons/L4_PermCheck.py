"""
# PermCheck
Check whether array A is a permutation.

A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2

is a permutation, but array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3

is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

    def solution(A)

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2

the function should return 1.

Given array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3

the function should return 0.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [1..1,000,000,000].

Copyright 2009–2023 by Codility Limited. All Rights Reserved.
Unauthorized copying, publication or disclosure prohibited.
"""


def solution(A):
    """
    :param A: a list of integers
    :return: true if the list is a permutation (sequence from 1 to N)

    One-by-one, add each value to a set.
        Abort if the value is not valid for the permutation
        Abort if the value is a duplicate
    It is a permutation.
    """
    if not len(A):
        return 0  # An empty list is not a permutation.

    A.sort()
    for i, a in enumerate(A):
        if a != i+1:
            return 0
    return 1

print(solution([4,1,3,2])) #1
print(solution(4,1,3)) #0