# 遞迴 Recursion
# Fibonacci sequence
'''
    Python預設Recursion次數為3000
import sys
sys.getrecursionlimit()
'''


# 迴圈太多速度很慢
class Fibonacci:
    def key2value(self, n:int) -> int:
        if n == 0 : return 0
        elif n == 1: return 1
        else: return self.key2value(n-1) + self.key2value(n-2)

    def key2list(self, n: int) -> list:
        list_ = []
        for i in range(1, n+1):
            ele = self.key2value(i)
            list_.append(ele)
        return list_


F = Fibonacci()
KV = F.key2value
KL = F.key2list
n = int(input('Input an Int:'))
# print(KV(n))
# print(KL(n))

#迴圈解，速度快多了
class Fibonacci_Faster:
    def key2value(self, n: int) -> int:
        if n == 1 or n == 2: return 1
        else:
            fib1 = 1
            fib2 = 1
            fib3 = 0
            for i in range(3, n+1):
                fib3 = fib1 + fib2
                fib1 = fib2
                fib2 = fib3
            return fib3

    def key2list(self, n: int) -> list:
        list_ = []
        for i in range(1, n+1):
            ele = self.key2value(i)
            list_.append(ele)
        return list_


FF = Fibonacci_Faster()
FFkv = FF.key2value
FFkl = FF.key2list

print(FFkv(n))
# print(FFkl(n))
