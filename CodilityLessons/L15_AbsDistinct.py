"""
# AbsDistinct

A non-empty array A consisting of N numbers is given. The array is sorted in non-decreasing order. The absolute distinct count of this array is the number of distinct absolute values among the elements of the array.

For example, consider array A such that:

  A[0] = -5
  A[1] = -3
  A[2] = -1
  A[3] =  0
  A[4] =  3
  A[5] =  6
The absolute distinct count of this array is 5, because there are 5 distinct absolute values among the elements of this array, namely 0, 1, 3, 5 and 6.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N numbers, returns absolute distinct count of array A.

For example, given array A such that:

  A[0] = -5
  A[1] = -3
  A[2] = -1
  A[3] =  0
  A[4] =  3
  A[5] =  6
the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647];
array A is sorted in non-decreasing order.
Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited
"""

def solution(A):
    A = [a*a for a in A]
    A = list(set(A))
    return len(A)

def solution(A):
    c = 1
    mymax = max(abs(A[0]), abs(A[-1]))
    index_head = 0
    index_tail = len(A) -1
    while index_head<=index_tail:
        head = abs(A[index_head])
        if head ==mymax :
            index_head += 1
            continue
        tail = abs(A[index_tail])
        if tail == mymax:
            index_tail -= 1
            continue
        if head>=tail:
            mymax = head
            index_head += 1
        else:
            mymax = tail
            index_tail -= 1
        c += 1
    return c


A = [-5,-3,-1,0,3,6]
print(solution(A)) # 5