class Solution:
    def printTree(self, height:int, symbol: str):
        if height == 1:
            print(symbol)
        else:
            i = 1
            count = 1
            space = ' '
            space_ = space * len(symbol)
            space_num = height-1
            while count <= height:
                row = space_ * space_num + symbol * i
                print(row)
                i += 2
                space_num -= 1
                count += 1


Solution().printTree(5, '*')