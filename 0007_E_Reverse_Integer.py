'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
    Input: 123
    Output: 321
Example 2:
    Input: -123
    Output: -321
Example 3:
    Input: 120
    Output: 21
Note:
Assume we are dealing with an environment which could only store integers
within the 32-bit signed integer range:
[−2^31,  2^31 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

'''


class Solution:
    def overflow(self, x: int) -> int:
        if x > -(2**31) and x < 2**31-1:
            return x
        else:
            return 0

    def reverse(self, x: int) -> int:
        x = self.overflow(x)
        if x == 0:
            ans = x
        elif x > 0:
            list_ = []
            len_ = len(str(x))
            i = 0
            while i < len_:
                left, out = divmod(x, 10)
                list_.append(str(out))
                x = left
                i += 1
            list_str = ''.join(list_)
            ans = int(list_str)
            ans = self.overflow(ans)
        else:
            x *= -1
            list_ = []
            len_ = len(str(x))
            i = 0
            while i < len_:
                left, out = divmod(x, 10)
                list_.append(str(out))
                x = left
                i += 1
            list_str = ''.join(list_)
            ans = int(list_str) * -1
            ans = self.overflow(ans)
        return ans


INT = 1534236469
S = Solution()
ans = S.reverse(INT)
print(ans)