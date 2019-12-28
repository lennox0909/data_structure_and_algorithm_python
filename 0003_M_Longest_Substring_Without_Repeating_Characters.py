'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:
    Input: "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
'''

s = "abcaadbcdbb"


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         len_record = []
#         dict = {}
#         l = len(s)
#         for i in range(l):
#             for j in range(i, l):
#                 if s[j] not in dict.values():
#                     dict[j] = s[j]
#                 else:
#                     a = len(dict)
#                     len_record.append(a)
#                     dict.clear()
#         m = max(len_record)
#         print(len_record)
#         return m


# ans = Solution().lengthOfLongestSubstring(s)
# print(ans)

class Solution:
    def lengthOfLongestSubstring(self, s):
        dct = {}
        max_so_far = curr_max = start = 0
        for index, i in enumerate(s):
            if i in dct and dct[i] >= start:
                max_so_far = max(max_so_far, curr_max)
                curr_max = index - dct[i]  # 距離上一個相同字母的距離
                start = dct[i] + 1  # 由於出現重複字母，substring起始點位置加1
            else:
                curr_max += 1
            dct[i] = index  # update index只留下不重複字母
        return max(max_so_far, curr_max)

ans = Solution().lengthOfLongestSubstring(s)
print(ans)

