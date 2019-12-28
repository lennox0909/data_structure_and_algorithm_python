'''
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example 1:
    Input: "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.

Example 2:
    Input: "cbbd"
    Output: "bb"

'''

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         new_s = ''
#         for i in range(n):
#             new_s = new_s + s[i] + ' '
#         new_s = new_s[:2*n-1]
#
#         return new_s
#
# s = "cbbd"
# S = Solution()
# ans = S.longestPalindrome(s)
# print(ans)
# print(len(ans))


# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         sLen = len(s)
#         dict = {}  # {i:pLen}
#
#         if sLen > 1000:
#             print('Should contain input string length within 1000.')
#         else:
#             for i in range(sLen):  # set i as Palindrome central index
#                 right_Len = sLen - i
#                 roof = min(i+1, right_Len)
#                 for j in range(roof):
#                     try:
#                         if s[i-j] == s[i+1+j]:  # 偶數迴文
#                             pLen = 2 + 2*j
#                             dict[i] = pLen
#                         else:
#                             break
#                     except:
#                         break
#
#                 try:
#                     for k in range(1, roof):
#                         if s[i-k] == s[i+k]:  # 基數迴文
#                             pLen = 2*k +1
#                             dict[i] = pLen
#                         else:
#                             break
#                 except:
#                     dict[0] = 1
#
#         pLen_list = list(dict.values())
#         pLen_max = max(pLen_list)
#         idx = pLen_list.index(pLen_max)
#         if pLen_max % 2 == 0:
#             start = idx - pLen_max/2 + 1
#             result_str = s[start : start + pLen_max]
#         elif pLen_max % 2 == 1:
#             start = idx - pLen_max//2
#             result_str = s[start: start + pLen_max]
#
#         return result_str
#
# s = "cbbd"
# S = Solution()
# ans = S.longestPalindrome(s)
# print(ans)


##########
# 以下正解
##########

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_ = [1]*len(s)
        for i in range(len(s)):
            count1 = count2 = 1

            # 偶數迴文
            if i+1<len(s) and s[i] == s[i+1]:
                mid = 1  # 確認下一步是否也迴文的進位量
                count1 = 2  # 目前最大回文長度
                # while條件式：確認兩個字母是否相同＆確認兩個字母都沒有超過range
                while i-mid>=0 and i+1+mid<len(s) and s[i-mid] == s[i+1+mid]:
                    count1 += 2
                    mid += 1
            # 基數迴文
            if i-1>=0 and i+1<len(s) and s[i-1] == s[i+1]:
                mid = 1  # 確認下一步是否也迴文的進位量
                count2 = 1  # 目前最大回文長度
                # while條件式：確認兩個字母是否相同＆確認兩個字母都沒有超過range
                while i-mid>=0 and i+mid<len(s) and s[i-mid] == s[i+mid]:
                    count2 += 2
                    mid += 1
            # 第i個idx中最長的迴文，記錄list到裡面
            list_[i] = max(count1,count2)



        max_ = index = 0
        # 找出list中的max以及他的index
        for j in range(len(list_)):
            if max_ < list_[j]:
                max_ = list_[j]
                index = j
        if max_ % 2 == 0:
            # 回傳偶數迴文
            return s[index-max_//2+1:index+1+max_//2]
        else:
            # 回傳基數迴文
            return s[index-(max_+1)//2+1:index+(max_+1)//2]

s = "cbbd"
S = Solution()
ans = S.longestPalindrome(s)
print(ans)