'''

Example 1:

    Input: "42"
    Output: 42
Example 2:

    Input: "   -42"
    Output: -42
    Explanation: The first non-whitespace character is '-', which is the minus sign.
                 Then take as many numerical digits as possible, which gets 42.
Example 3:

    Input: "4193 with words"
    Output: 4193
    Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

    Input: "words and 987"
    Output: 0
    Explanation: The first non-whitespace character is 'w', which is not a numerical
                 digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

    Input: "-91283472332"
    Output: -2147483648
    Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
                 Thefore INT_MIN (−2^31) is returned.

'''

'''
chr()
Format: chr(i), i: integer
傳入參數int[0..255] 的ASCII code編碼，回傳對應的ASCII code字元。
>>> chr(97)
'a'
 
unichr()
Format: unichr(i), i: integer
傳入參數Unicode編碼(包含ACSII code編碼)，回傳對應的Unicode字元。
>>> unichr(97)
u'a'
 

ord()
Format: ord(c), c: character
傳入字元，回傳對應的Unicode字元。
>>> ord('a')
97
'''


class Solution:
    def myAtoi(self, str: str) -> int:
        digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        result_str = str.strip(" ")
        if len(result_str) == 0: return 0

        MAX_INT = 2 ** 31 - 1
        MIN_INT = 2 ** 31

        sign = 1
        start_idx = 1
        if result_str[0] == "-":
            sign = -1
        elif result_str[0] == "+":
            pass
        elif result_str[0] not in digits:
            return 0
        else:
            start_idx = 0

        result = 0
        for c in result_str[start_idx:]:
            if c not in digits:
                break
            result = 10 * result + (ord(c) - ord('0'))
            if sign == 1 and result >= MAX_INT:
                result = MAX_INT
                break
            elif sign == -1 and result >= MIN_INT:
                result = MIN_INT
                break

        return sign * (result)


str_ = "4193 with words"
ans = Solution().myAtoi(str_)
print(ans)






# class Solution:
#     def myAtoi(self, str: str) -> int:
#         digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
#         result_str = str.strip(" ")
#         if len(result_str) == 0: return 0
#
#         MAX_INT = 2 ** 31 - 1
#         MIN_INT = 2 ** 31
#
#         sign = 1
#         start_idx = 1
#         if result_str[0] == "-":
#             sign = -1
#         elif result_str[0] == "+":
#             pass
#         elif result_str[0] not in digits:
#             return 0
#         else:
#             start_idx = 0
#
#         result = 0
#         for c in result_str[start_idx:]:
#             if c not in digits:
#                 break
#             result = 10 * result + (ord(c) - ord('0'))
#             if sign == 1 and result >= MAX_INT:
#                 result = MAX_INT
#                 break
#             elif sign == -1 and result >= MIN_INT:
#                 result = MIN_INT
#                 break
#
#         return sign * (result)