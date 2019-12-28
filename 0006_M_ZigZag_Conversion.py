'''

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:
    Input: s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"

Example 2:
    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I

'''


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = len(s)
        cycle = 2 * numRows - 2  # str_num back to next zigzag top
        strlist = []
        for i in range(numRows):  # read every row
            for j in range(i, n, cycle):  # read element by step of cycle
                strlist.append(s[j])
                # if i is not first/end row
                # j + cycle - 2 * i ==> element in between cycles
                if i != numRows - 1 and i != 0 and j + cycle - 2 * i < n:
                    strlist.append(s[j + cycle - 2 * i])
        newstr = ''.join(strlist)
        return newstr

s = "0123456789"
numRows = 4
S = Solution()
ans = S.convert(s,numRows)
print(ans)