import unittest
import random

"""
Quitting will exit you from this test without submitting any solutions for evaluation. You may re-enter this test again, but the timer will continue to countdown from your initial entry.
-- GetYourGuide Application
"""
def solution(A):
    """
    Given an array of N integers, returns the maximum sum of two numbers whose digits
    add up to an equal sum. If there are no whose digits returns -1
    :param A:
    :return: max_sum

    SOLUTION:
    first is most posible to have bigger sums if the list is sorted in descending order
    num_keys -> will save all the digits sum of a specific number (I'm using dicts because they are faster for the hash)
    the journey is made all against all, keeping the maximum sum
    """

    def get_sum(n):
        """
        This function receives a number and sum their digits
        :param n: int
        :return: int sum_digits
        """
        sum = 0
        for digit in str(n):
            sum += int(digit)
        return sum

    A.sort(reverse=True)
    num_keys = dict()
    max_sum = 0
    for i, a in enumerate(A[:-1]):
        num_keys[a] = num_keys.get(a, get_sum(a))
        for b in A[i+1:]:
            num_keys[b] = num_keys.get(b, get_sum(b))
            if num_keys[a] == num_keys[b]:
                max_sum = max(max_sum,a + b)
    return max_sum if max_sum>0 else -1


class TestEvaluation(unittest.TestCase):

    def test_sample_generation(self):
        self.assertEqual(solution([51,71,17,42]), 93)
        self.assertEqual(solution([42,33,60]), 102)
        self.assertEqual(solution([51,32,43]), -1)
        self.assertEqual(solution([51, 41, 33, 50]), 91)
        self.assertEqual(solution([51, 41, 33, 50,10000000, 100]), 10000100)

    def test_empty(self):
        self.assertEqual(solution([]), -1)


if __name__ == '__main__':
    unittest.main()