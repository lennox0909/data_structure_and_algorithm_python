'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

http://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png

Example:
    Input: "23"
    Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
    Although the above answer is in lexicographical order, your answer could be in any order you want.
'''

# 當迴圈數無法固定時，把迴圈放在def中，然後對def做recursion

# class Solution:
#     def letterCombinations(self, digits: str) -> list:
#         buttons = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
#         list_ = []
#         number = []
#         for a in digits:
#             number = int(a)
#             letter = buttons[number]
#             list_.append(letter)
#         for b in list_:
#             num = len(b)
#             number.append(num)
#         Len = len(number)
#         temp_result = []

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def check(combination:str, next_digit:str):

            if len(next_digit) == 0:
                output.append(combination)
            else:
                for letter in phone[next_digit[0]]:
                    check(combination + letter, next_digit[1:])
        output = []
        if digits:
            check('', digits)
        return output

# 最佳解
'''
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
                
        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map 
                # the next available digit
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])
                    
        output = []
        if digits:
            backtrack("", digits)
        return output
'''

digits = '249'
print(Solution().letterCombinations(digits))
