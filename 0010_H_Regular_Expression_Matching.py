'''

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element. ==> * wildcard 萬用字元
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

    Input:
    s = "aa"
    p = "a"
    Output: false
    Explanation: "a" does not match the entire string "aa".
Example 2:

    Input:
    s = "aa"
    p = "a*"
    Output: true
    Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

    Input:
    s = "ab"
    p = ".*"
    Output: true
    Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

    Input:
    s = "aab"
    p = "c*a*b"
    Output: true
    Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

    Input:
    s = "mississippi"
    p = "mis*is*p*."
    Output: false

'''

# Without a Kleene star *, our solution would look like this:
# 遞迴 Recursion
def match_(text, pattern):
    # if pattern: return text
    if not pattern: return not text  # when pattern & text are '' empty strings ==> if True: return True
    A = bool(text)  # bool(text) = True, else = False when text = '' empty string
    B = {text[0], '.'}  # set{}
    C = pattern[0]  # str
    D = C in B  # bool
    first_match = A and D
    return first_match and match_(text[1:], pattern[1:])
    # return first_match STOPS when first_match is False

# Without a Kleene star *, our solution would look like this:
# 簡潔厲害寫法
def match(text, pattern):
    if not pattern: return not text
    '''
    等於: if not bool(pattern): return not bool(text)
    等於: if bool(pattern) == False: return not bool(text)
    # if pattern = empty string, return not bool(text)
    # if pattern = empty string AND text = empty string, return True
    # 檢查如果pattern是否為空字串，text也是空字串，則兩者match回傳True
    # 如果如果pattern不是空字串，這行程式碼就會被跳過去
    '''
    first_match = bool(text) and pattern[0] in {text[0], '.'}
    return first_match and match(text[1:], pattern[1:])


t = 'lennox'
p = 'le..ox'
# print(match_(t,p))

# https://leetcode.com/articles/regular-expression-matching/

class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and
                    self.isMatch(text[1:], pattern))
            # isMatch(text[1:], pattern) *重複一次前個字母後,是否相等於text[1]
            # 運算時，先 and 後 or
            # 對於, 1 or 5 and 4:先算5 and 4, 5為真,值為4.再算1 or 4, 1為真, 值為1
            # 對於, (1 or 5) and 4:先算1 or 5, 1為真,值為1.再算1 and 4, 1為真, 值為4

        else:
            return first_match and self.isMatch(text[1:], pattern[1:])


S = Solution().isMatch
text = 'nnnnnn'
pattern = 'n*n'
print(S(text,pattern))