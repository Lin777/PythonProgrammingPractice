"""
# TapeEquilibrium

Minimize the value |(A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1])|.

A non-empty array A consisting of N integers is given.
Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts:
A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of:
|(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part
and the sum of the second part.

For example, consider array A such that:
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3

We can split this tape in four places:

        P = 1, difference = |3 − 10| = 7
        P = 2, difference = |4 − 9| = 5
        P = 3, difference = |6 − 7| = 1
        P = 4, difference = |10 − 3| = 7

Write a function:

    def solution(A)

that, given a non-empty array A of N integers, returns the minimal difference
that can be achieved.

For example, given:
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3

the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [2..100,000];
        each element of array A is an integer within the range [−1,000..1,000].

Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""

def solution(A):
    """Minimize the value |(A[0] + ... + A[P-1]) = (A[P] + ... + A[N-1])|.

    :param A: list[int]: A non-empty list of integers.
    :return: [int]: The index value where the smallest difference begins.

    * Establish two tallys:
        sum_of_left for the sum of all the numbers to the left and
        sum_of_right for the sum of all the numbers to the right.
    * Initially the position P is 0, so
        sum_of_left is 0 and
        sum_of_right is the sum of all the numbers in the given array (O(n)).
    * Visit every P from left to right O(n):
        * With each new number:
            * add the value to the sum to the left
            * subtract the value from the sum to right
        * Calculate the difference between the left and right sums.
        * Update the smallest difference seen.
    """

def solution(A):
    sumR = sum(A)
    sumL = 0
    min_diff = max(1e9,sumR)
    for a in A[:-1]:
        sumR = sumR - a
        sumL = sumL + a
        diff = abs(sumR - sumL)
        min_diff = min(diff, min_diff)
    return min_diff

A = [-1000, 1000]
print(solution(A))
