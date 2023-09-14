"""
# Missing Integer
Find the smallest positive integer that does not occur in a given sequence.

Write a function:

    def solution(A)

that, given an array A of N integers, returns the smallest positive integer
(greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

    N is an integer within the range [1..100,000];
    each element of array A is an integer within the range [−1,000,000..1,000,000].

Copyright 2009–2023 by Codility Limited. All Rights Reserved.
Unauthorized copying, publication or disclosure prohibited.
"""


def solution(A):
    """
    :param A: list[int] A non-empty list of integers.
    :return: [int] The smallest positive integer that is missing.

    Sort the array and walk through it until we find the missing item.
    I wonder if this is a mistake: allowing us to sort the array first?
    """
    missing = 1
    A.sort()
    for elem in A:
        if elem == missing:
            missing += 1
        if elem > missing:
            break
    return missing
