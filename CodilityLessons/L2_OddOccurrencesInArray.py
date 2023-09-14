"""
# OddOccurrencesInArray

A non-empty array A consisting of N integers is given.
The array contains an odd number of elements, and
each element of the array can be paired with another element that has the same value,
except for one element that is left unpaired.

For example, in array A such that:
  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9

        the elements at indexes 0 and 2 have value 9,
        the elements at indexes 1 and 3 have value 3,
        the elements at indexes 4 and 6 have value 9,
        the element at index 5 has value 7 and is unpaired.

Write a function:

    def solution(A)

that, given an array A consisting of N integers fulfilling the above conditions,
returns the value of the unpaired element.

For example, given array A such that:
  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9

the function should return 7, as explained in the example above.

Write an efficient algorithm for the following assumptions:

        N is an odd integer within the range [1..1,000,000];
        each element of array A is an integer within the range [1..1,000,000,000];
        all but one of the values in A occur an even number of times.

Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""

def solution(A):
    """Find the value that does not have a match in an odd sized array.

    :param A: [[int]] an array of integers with an odd number of elements.
    :param N: [int] length of the array.
    :return: The value which does not have a duplicate.

    * With a collection to accumlate unmatched values, step through the array.
    * Remove the value from the unmatched collection.
    * If that fails, add it to the unmatched collection.
    * At the end of the list, there should be one unmatched value in the collection.
    * The 'collection' can be either a set, or a dictionary (with the value as the key and a boolean as the value).
      The dictionary is slightly faster; I guess finding a value in a set is more work than indexed dict keys,
      but imho the set is faintly more elegant.
    """
    unmatched = set()
    for element in A:
        try:
            unmatched.remove(element)
        except KeyError:
            unmatched.add(element)
    return unmatched.pop()

A = [9,3,9,3,9,7,9]
print(solution(A)) #7