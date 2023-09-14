"""
A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
we can find two equi leaders:

0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
The goal is to count the number of equi leaders.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

For example, given:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    def get_dominator(A):
        # Implement your solution here
        copy_a = A.copy()
        copy_a.sort()
        middle = len(A)//2
        element_candidate = copy_a[middle]
        count = 0
        for a in copy_a:
            if a == element_candidate:
                count += 1
            elif a > element_candidate:
                break
        if count > middle:
            return element_candidate, count
        else:
            return None, None
    equi_leader = 0
    dominator1 = dominator2 = count1 = count2 = None
    size_a = len(A)
    for i in range(1, size_a):
        value = A[i-1]
        if dominator1 == value:
            count1 += 1
        if count1 is None or count1 <= i//2:
            dominator1, count1 = get_dominator(A[:i])
        if dominator2 == value:
            count2 -= 1
        if count2 is None or count2 <= (size_a-i)//2:
            dominator2, count2 = get_dominator(A[i:])
        if dominator1!=None and dominator1 == dominator2:
            equi_leader += 1
    return equi_leader

print(solution([4,3,4,4,4,2]))
