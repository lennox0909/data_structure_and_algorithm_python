'''

Given an array nums of n integers, are there elements a, b, c in nums
such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
    Given array nums = [-1, 0, 1, 2, -1, -4],
    A solution set is:
    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]

'''

# Correct! But time complexity O(n^3)
'''
class Solution:
    def threeSum(self, nums: list) -> list:
        ans = []
        temp = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j + 1, len(nums)):
                    while nums[i]+nums[j]+nums[k] == 0:
                        temp.append(nums[i])
                        temp.append(nums[j])
                        temp.append(nums[k])
                        temp.sort()
                        if temp not in ans:
                            ans.append(temp)
                        temp = []
                        break
        ans.sort()
        return ans
'''

# Correct! But time complexity O(n^3)
'''
class Solution:
    def twoSum(self,idx_start:int,idx_end:int,nums:list):
        # idx_start < idx_end
        s = set()
        target = 0
        if idx_end+1 < len(nums):
            target = (nums[idx_start] + nums[idx_end]) * -1
            s = set(nums[idx_end + 1:])
        if target in s:
            return target
        else:
            return False

    def threeSum(self, nums: list) -> list:
        ans = []
        temp = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                a = self.twoSum(i,j,nums)
                if type(a) == int:
                    temp.append(a)
                    temp.append(nums[i])
                    temp.append(nums[j])
                    temp.sort()
                    if temp not in ans:
                        ans.append(temp)
                    temp = []
        ans.sort()
        return ans
'''

# Correct! But time complexity O(n^3)
'''
class Solution:
    def threeSum(self, nums: list) -> list:
        nums.sort()
        Len = len(nums)
        zero = []
        ans = []
        for i in range(Len):
            j = i+1
            while j+1 < Len:
                target = (nums[i] + nums[j]) * -1
                if target in nums[j+1:]:
                    zero.append(nums[i])
                    zero.append(nums[j])
                    zero.append(target)
                    zero.sort()
                    if zero not in ans:
                        ans.append(zero)
                    zero = []
                j += 1
        return ans
'''



# A+B+C=0
# 順序 A前 B中 C後
# Runtime: 2792 ms, faster than 5.02% of Python3 online submissions for 3Sum.
# Memory Usage: 16.6 MB, less than 78.57% of Python3 online submissions for 3Sum.
'''
class Solution:
    def threeSum(self, nums: list) -> list:

        result = set()

        def calculate(B_idx, A):
            s = set([nums[B_idx]])
            # 把AC中間的數字加到s_set中

            C_to_end_list = nums[B_idx + 1:]
            # 從C走到最後的list

            for C in C_to_end_list:  # 掃描C
                target = (A + C) * -1

                if target in s:
                    x = tuple(sorted([A, C, target]))
                    if x not in result:
                        result.add(x)
                s.add(C)
                # 每個C都加到s_set中
            return result

        for B_idx in range(1, len(nums) - 1):  # 掃描A
            A = nums[B_idx - 1]
            calculate(B_idx, A)

        return result
'''

# ===== 最佳解 ===== #
# Runtime: 664 ms, faster than 94.39% of Python3 online submissions for 3Sum.
# Memory Usage: 16.2 MB, less than 100.00% of Python3 online submissions for 3Sum.
# list.sort()之後 = [A,B,C,D,E,Ln-2,Ln-1], 長度為n
# X <= Y <= Z, X+Y+Z = 0 , X<=0 and Z >=0, Y+Z= -X
# 固定X, 讓 Y = B, Z = Ln-1


class Solution:
    def threeSum(self, nums: list) -> list:
        results = []
        ln = len(nums)
        if (ln<3):
            return results
        nums.sort()
        if (nums[-1]<0):
            return results
        computed = []  # for檢查重複 X
        for i,n1 in enumerate(nums[:-2]):
            if n1 > 0:
                break
            if n1 in computed:
                continue
            computed.append(n1)
            n = -n1
            l = i+1
            r = ln-1
            computed2 = []  # for檢查重複[Y,Z]
            while(l<r):
                s = nums[l]+nums[r]
                if s == n:
                    pair = [nums[l], nums[r]]
                    if pair not in computed2:
                        computed2.append(pair)
                        res = [n1, nums[l], nums[r]]
                        results.append(res)
                    l += 1
                elif s < n:
                    l += 1
                else:
                    r -= 1
        return results


nums = [-1, 0, 1, 2, -1, -4]
nums2 = [-7,-11,12,-15,14,4,4,11,-11,2,-8,5,8,14,0,3,2,3,-3,-15,-2,3,6,1,2,8,-5,-7,3,1,8,11,-3,6,3,-4,-13,-15,14,-8,2,-8,4,-13,13,11,5,0,0,9,-8,5,-2,14,-9,-15,-1,-6,-15,9,10,9,-2,-8,-8,-14,-5,-14,-14,-6,-15,-5,-7,5,-11,14,-7,2,-9,0,-4,-1,-9,9,-10,-11,1,-4,-2,2,-9,-15,-12,-4,-8,-5,-11,-6,-4,-9,-4,-3,-7,4,9,-2,-5,-13,7,2,-5,-12,-14,1,13,-9,-3,-9,2,3,8,0,3]
nums3 = [1,2,-2,-1]
nums4 = [1,2,3,4,5]

# nums2.sort()
print(Solution().threeSum(nums))
# print(Solution().threeSum(nums2))
print(Solution().threeSum(nums4))