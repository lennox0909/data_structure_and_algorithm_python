'''

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
    Input: ["flower","flow","flight"]
    Output: "fl"
Example 2:
    Input: ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.
Note:
    All given inputs are in lowercase letters a-z.
https://leetcode.com/articles/longest-common-prefix/
'''

'''
class Solution:
    def comparePrefixOfTwqStrings(self,str1, str2):
        if len(str1) <= len(str2):
            min_ = len(str1)
        else:
            min_ = len(str2)

        for i in range(min_):
            n = 0
            while str1[n] == str2[n]:
                n += 1
        ans = str1[:n]
        return ans

    def comparePrefixOfTwqStrings_error(self,str1, str2):
        try:
            Com = self.comparePrefixOfTwqStrings(str1, str2)
        except TypeError:
            Com = ''
        return Com

    def longestCommonPrefix(self, strs: list) -> str:
        Com = self.comparePrefixOfTwqStrings_error(strs[0], strs[1])
        for i in range(2,len(strs)):
            Com = self.comparePrefixOfTwqStrings_error(Com, strs[i])
        return Com
'''

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        if len(strs) == 1: return strs[0]

        strs.sort()  # list.sort()
        p = ""
        a = strs[0]
        b = strs[-1]
        for x, y in zip(a,b):
            if x == y:
                p += x
            else:
                break
        return p


strs = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))
print(Solution().longestCommonPrefix(''))
print(Solution().longestCommonPrefix([]))
print(Solution().longestCommonPrefix({}))

zzip = zip('flight', 'flow')
print(zzip)  # <zip object at 0x1034334c8>
print(list(zzip))  # [('f', 'f'), ('l', 'l'), ('i', 'o'), ('g', 'w')]

