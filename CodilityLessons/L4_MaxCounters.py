"""
# MaxCounters

Calculate the values of counters after applying all alternating operations:
increase counter by 1; set value of all counters to current maximum.

You are given N counters, initially set to 0, and you have two possible
operations on them:

    * increase(X) - counter X is increased by 1,
    * max counter - all counters are set to the maximum value of any counter.

A non-empty array A of M integers is given.
This array represents consecutive operations:

    * if A[K] = X, such that 1 <= X <=  N, then operation K is increase(X),
    * if A[K] = N + 1 then operation K is max counter.

For example, given integer N = 5 and array A such that:
    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4

the values of the counters after each consecutive operation will be:
    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)

The goal is to calculate the value of every counter after all operations.

Write a function:

    def solution(N, A)

that, given an integer N and a non-empty array A consisting of M integers,
returns a sequence of integers representing the values of the counters.

Result array should be returned as an array of integers.

For example, given:
    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4

the function should return [3, 2, 2, 4, 2], as explained above.

Write an efficient algorithm for the following assumptions:

        N and M are integers within the range [1..100,000];
        each element of array A is an integer within the range [1..N + 1].

Copyright 2009–2023 by Codility Limited. All Rights Reserved.
Unauthorized copying, publication or disclosure prohibited.
---

# My Notes

The straight-forward solution, of updating all the counters every time
there is a 'max counter' instruction, only gets you a 60% score. If every
instruction is a max-counter it will pass over the whole counter array M
times! O(n*m)

For 100%, optimize the max-counter operation by, to use a tidal analogy,
tracking the "low" and "high" "water" marks across all the counters.

With each counter update, check the low-water mark and, if necessary,
raise this counter to it. Now increment. And, before you leave, if necessary,
reset the high water mark.  This way, you maintain context of what is happening
in all the counters, without needing to visit them repeatedly.

Before sending back the results, a final pass over the counters is necessary to
ensure the low-water mark applies to any counters which have not been in focus
since it last changed.

Thus the solution requires just two passes over the whole array of counters. O(n+m)
"""

def solution(N, A):
    list_numbers = [0] * N
    max_counter = 0
    max_value = 0
    for v in A:
        if v <= N:
            list_numbers[v-1] = max(max_counter, list_numbers[v-1]) + 1
            max_value = max(list_numbers[v-1], max_value)
        else:
            max_counter = max_value
    return list(map(lambda x: max(max_counter, x), list_numbers))

A = [3,4,4,6,1,4,4]
print(solution(5, A))
