'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums
such that a + b + c + d = target?

Find all unique quadruplets in the array which gives the sum of target.

Note:
The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
    A solution set is:
    [
      [-1,  0, 0, 1],
      [-2, -1, 1, 2],
      [-2,  0, 0, 2]
    ]
'''
# list.sort()之後 = [A,B,C,D,E,Ln-2,Ln-1], 長度為n
# W <= X <= Y <= Z, W+X+Y+Z = target
# 固定W, 讓 X = B, Y = C, Z = Ln-1
# 自己寫的
# Runtime: 2184 ms, faster than 5.06% of Python3 online submissions for 4Sum.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for 4Sum.
class Solution:
    def fourSum(self, nums: list, target: int) -> list:
        nums.sort()
        ln = len(nums)
        # nums_sum = sum(nums[i] for i in range(ln))
        # nums_sum = nums[0] + nums[1] + nums[2] + nums[3]
        if ln == 4 and sum(nums) == target:
            return [nums]

        result = []
        for i in range(ln-3):
            # if nums[i] == nums[i-1] and i > 0:
            #     continue
            for r in range(ln-1,0,-1):
                # if nums[r] == nums[r-1]:
                #     continue
                j = i + 1
                k= r-1
                while i<j<k<r:
                    temp_list = [nums[i], nums[j], nums[k], nums[r]]
                    temp_sum = sum(temp_list)
                    distance = target - temp_sum
                    if distance > 0:# and j+1<k:
                        j += 1
                        # while nums[j] == nums[j+1] and j+1<k:
                        #     j += 1
                    elif distance < 0:# and k-1 > j:
                        k -= 1
                        # while nums[k] == nums[k-1] and k-1 > j:
                        #     k -= 1
                    elif distance == 0:
                        k -= 1
                        if temp_list not in result:
                            result.append(temp_list)
                        # if k-1 > j:
                        #     k -= 1
                        # else: break
                    # else:break

        return result

# 最佳解
# Runtime: 84 ms, faster than 95.06% of Python3 online submissions for 4Sum.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for 4Sum.
class Solution2:
    def fourSum(self, nums: list, target: int) -> list:
        nums.sort()
        res = []
        self.findNSum(nums, target, 4, [], res)
        return res

    def findNSum(self, nums, target, N, prefix, result):
        L = len(nums)
        if N == 2:
            l, r = 0, L-1
            while l < r:
                add = nums[l] + nums[r]
                if add == target:
                    result.append(prefix + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l<r and nums[l-1] == nums[l]:
                        l += 1
                    while l<r and nums[r+1] == nums[r]:
                        r -= 1
                elif add > target:
                    r -= 1
                else:
                    l += 1
        else:
            for i in range(L-N+1):
                if target < N*nums[i] or target > N*nums[-1]: # key judgement
                    break
                if i == 0 or (i>0 and nums[i] != nums[i-1]):
                    self.findNSum(nums[i+1:], target-nums[i], N-1, prefix+[nums[i]], result)
        # return


nums1 = [-7,-11,12,-15,14,4,4,11,-11,2,-8,5,8,14,0,3,2,3,-3,-15,-2,3,6,1,2,8,-5,-7,3,1,8,11,-3,6,3,-4,-13,-15,14,-8,2,-8,4,-13,13,11,5,0,0,9,-8,5,-2,14,-9,-15,-1,-6,-15,9,10,9,-2,-8,-8,-14,-5,-14,-14,-6,-15,-5,-7,5,-11,14,-7,2,-9,0,-4,-1,-9,9,-10,-11,1,-4,-2,2,-9,-15,-12,-4,-8,-5,-11,-6,-4,-9,-4,-3,-7,4,9,-2,-5,-13,7,2,-5,-12,-14,1,13,-9,-3,-9,2,3,8,0,3]
nums1_sort = [-15, -15, -15, -15, -15, -15, -15, -14, -14, -14, -14, -13, -13, -13, -12, -12, -11, -11, -11, -11, -11, -10, -9, -9, -9, -9, -9, -9, -9, -8, -8, -8, -8, -8, -8, -8, -7, -7, -7, -7, -7, -6, -6, -6, -5, -5, -5, -5, -5, -5, -4, -4, -4, -4, -4, -4, -3, -3, -3, -3, -2, -2, -2, -2, -2, -1, -1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 7, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 11, 11, 11, 12, 13, 13, 14, 14, 14, 14, 14]
nums2 = [1, 0, -1, 0, -2, 2]
nums3 = [0,0,0,0]
target1 = 1
target2 = 0
target3 = 55

print(Solution().fourSum(nums3,target2))
print(Solution2().fourSum(nums2,target2))














