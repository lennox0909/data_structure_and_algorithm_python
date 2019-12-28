'''
Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.
'''


class Solution:
    def romanToInt(self, s: str) -> int:
        div_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        rom_list = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        ans = 0
        for i in range(len(rom_list)):
            check_word = rom_list[i]
            check_len = len(check_word)
            while s[:check_len] == check_word:
                ans = ans + div_list[i]
                s = s[check_len:]
        if not (ans >= 1 and ans <= 3999): return 'Exceed Range'
        else: return ans


rom = 'MCMLXXXIII'
ans = Solution().romanToInt(rom)
print(ans)