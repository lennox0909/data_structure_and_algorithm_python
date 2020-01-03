'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
    Input: "()"
    Output: true
Example 2:
    Input: "()[]{}"
    Output: true
Example 3:
    Input: "(]"
    Output: false
Example 4:
    Input: "([)]"
    Output: false
Example 5:
    Input: "{[]}"
    Output: true
'''

# Runtime: 24 ms, faster than 90.20% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Valid Parentheses.

class Solution:
    def isValid(self, s):
        bracket_map = {"(": ")", "[": "]",  "{": "}"}
        open_par = set(["(", "[", "{"])
        stack = []
        for i in s:
            if i in open_par:
                stack.append(i)
            elif stack and i == bracket_map[stack[-1]]:
                    stack.pop()
            else:
                return False
        return stack == []



# Runtime: 40 ms, faster than 12.09% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Valid Parentheses.
'''
class Solution:
    def isValid(self, s: str) -> bool:
        c = -1
        while True:
            s = s.replace('()', '')
            s = s.replace('[]', '')
            s = s.replace('{}', '')
            Len = len(s)
            if c == Len:
                break
            c = Len

        s_list = list(s)
        if self.isListValid(s_list) == 1:
            return True
        else:
            return False

    def isListValid(self, s_list):
        valid_dict = {'(': ')', '[': ']', '{': '}'}
        if len(s_list) == 0:
            return 1
        elif len(s_list) == 1:
            return 0
        elif s_list[0] == ')' or s_list[0] == ']' or s_list[0] == '}':
            return 0
        elif valid_dict[s_list[0]] not in s_list:
            return 0
        elif valid_dict[s_list[0]] == s_list[1]:
            s_list = s_list[2:]
            return self.isListValid(s_list)
        elif valid_dict[s_list[0]] == s_list[-1]:
            s_list = s_list[1:-1]
            return self.isListValid(s_list)
        else:
            for i in range(3, len(s_list),2):
                if valid_dict[s_list[0]] == s_list[i]:
                    del s_list[i]
                    s_list = s_list[1:]
                    return self.isListValid(s_list)
                else:
                    return 0
'''






Input1 = "()"  # True
Input2 = "()[]{}"  # True none
Input3 = "(]"  # False
Input4 = "([)]"  # False
Input5 = "{[]}"  # True none
Input6 = ""  # True
Input7 = "([)"  # False
Input8 = "([]){}"  # True
Input9 = "[([]])"  # False

# print(Solution().isValid(Input1))
# print(Solution().isValid(Input2))  # none
# print(Solution().isValid(Input3))
# print(Solution().isValid(Input4))
# print(Solution().isValid(Input5))
# print(Solution().isValid(Input6))
# print(Solution().isValid(Input7))
# print(Solution().isValid(Input8))
print(Solution().isValid(Input9))
# print()
# print(Solution().isListValid(Input1))
# print(Solution().isListValid(Input2))
# print(Solution().isListValid(Input3))
# print(Solution().isListValid(Input4))
# print(Solution().isListValid(Input5))
# print(Solution().isListValid(Input6))
# print(Solution().isListValid(Input7))