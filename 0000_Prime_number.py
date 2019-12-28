'''
質數（Prime number），又稱素數，指在大於1的自然數中，除了1和該數自身外，無法被其他自然數整除的數。
大於1的自然數若不是質數，則稱之為合數。
'''


class Prime:
    def isPrime(self, x: int) -> bool:
        if x == 0: return False
        elif x == 1: return True
        elif x == 2: return True
        ans = True
        # x starts at 3
        for i in range(2, x):
            bool_ = x % i != 0  # True is Prime
            # exception: 2 is prime; 2%1 == 0
            ans = ans and bool_
        return ans

    def PrimeNumList(self, x: int):
        list_ = []
        for i in range(1, x + 1):
            if self.isPrime(i):
                list_.append(i)
        return len(list_), list_

    def PrimeTrend(self, x:int) -> dict:
        dict_ = {}
        for i in range(1, x + 1):
            Num_, List_ = self.PrimeNumList(i)
            dict_[i] = Num_
        return dict_  # {x: Num of primes within x}


P = Prime().isPrime
print(P(11))

PL = Prime().PrimeNumList
Num, List = PL(100)
print(Num)
print(List)

PT = Prime().PrimeTrend
# print(PT(100))



