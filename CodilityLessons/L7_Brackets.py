"""
A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

class Solution { public int solution(String S); }

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..200,000];
string S is made only of the following characters: '(', '{', '[', ']', '}' and/or ')'.
"""
def solution(S):
    s_stack = []
    dict_pair_chairs = {'{':'}', '[': ']', '(': ')'}
    for char in S:
        try:
            if char in dict_pair_chairs.keys():
                s_stack.append(char)
            else:
                last_open_char = s_stack[-1]
                if dict_pair_chairs[last_open_char] == char :
                    s_stack.pop()
        except Exception as e:
            return 0
    return 1 if len(s_stack)== 0 else 0
