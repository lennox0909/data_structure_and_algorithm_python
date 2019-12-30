'''
Given an array nums of n integers and an integer target,
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example:
    Given array nums = [-1, 2, 1, -4], and target = 1.
    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

'''
:param nums: List[int]
:param target: int
:return: int
'''


# ===Correct but: Time Limit Exceeded===
'''
class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:

        nums = set(nums)
        nums = list(nums)

        s = set()

        temp = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1, len(nums)):
                    temp = nums[i]+nums[j]+nums[k]
                    s.add(temp)
        l = list(s)
        l2 = []
        for i in l:
            e = abs(i - target)
            l2.append(e)
        min_ = min(l2)
        idx = -1
        for i,e in enumerate(l2):
            if e == min_:
                idx = i
                break
        return l[idx]
'''


# 最佳解
# list.sort()之後 = [A,B,C,D,E,Ln-2,Ln-1], 長度為n
# X <= Y <= Z, X+Y+Z = closest
# 固定X, 讓 Y = B, Z = Ln-1
# 比較closest & target
# Runtime: 96 ms, faster than 96.10% of Python3 online submissions for 3Sum Closest.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for 3Sum Closest.
class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        length = len(nums)
        if (length <= 3) :
            return sum([nums[x] for x in range(length)])
        nums.sort()
        closest = sum([nums[x2] for x2 in range(3)])
        result = abs(target - closest)
        for i in range(length - 2) :
            if i > 0 and nums[i] == nums[i - 1]:
                continue;
            j = i + 1
            k = length - 1
            while j < k :
                temp_closest = nums[i] + nums[j] + nums[k]
                temp_result = abs(target - temp_closest)
                if temp_result < result :
                    closest, result = temp_closest, temp_result
                if target > temp_closest :
                    j += 1
                    while j < k and nums[j] == nums[j - 1] :
                        j += 1
                elif target < temp_closest :
                    k -= 1
                    while j < k and nums[k] == nums[k + 1] :
                        k -= 1
                else :
                    return target
        return closest



# list.sort()之後 = [A,B,C,D,E,Ln-2,Ln-1], 長度為n
# X <= Y <= Z, X+Y+Z = target
# 固定X, 讓 Y = B, Z = Ln-1

'''
class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:

        nums.sort()
        ln = len(nums)

        if (ln<=3):
            return sum(nums)

        if target < nums[0] or target <= sum(nums[:3]):
            return sum(nums[:3])

        if nums[-1] < target or sum(nums[-3:]) <= target:
            return sum(nums[-3:])

        if sum(nums[:3]) < target < sum(nums[-3:]):
                # location = 0

                sum_dict = {}  # {idx: sum}
                for i in range(ln-2):
                    sum_ = sum(nums[i:i+3])
                    sum_dict[i] = sum_

                if target in list(sum_dict.values()):
                    return target
                else:
                    sum_distance_dict = {}  # {distance:idx}
                    for k,v in sum_dict.items():
                        distance = abs(v - target)
                        sum_distance_dict[distance] = k
                    min_distance = min(list(sum_distance_dict.keys()))
                    start_idx = sum_distance_dict[min_distance]

                idx2 = start_idx + 1
                idx3 = start_idx + 2
                temp_sum = sum(nums[start_idx:start_idx+3])
                


            # for i, n1 in enumerate(nums[:-2]):
            #     computed = []
            #     if n1 in computed:
            #         continue
            #     computed.append(n1)
            #     l = i + 1
            #     r = ln - 1
            #     while l < r:
            #         s = nums[l] + nums[r]
            #         if n1 == target - s:
            #             return target

        # if sum(nums[:3]) < target < sum(nums[-3:]):
        #     sum_dict = {}
        #     for i in range(ln-2):
        #         sum_ = sum(nums[i:i+3])
        #         sum_dict[i] = sum_
        #     if target in list(sum_dict.values()):
        #         return target
        #     else:
        #         sum_distance_dict = {}
        #         for k,v in sum_dict.items():
        #             sum_distance = v - target
        #             sum_distance_dict[sum_distance] = k
        #         min_ = min(list(sum_distance_dict.keys()))
        #         return sum_distance_dict[min_]
'''



nums = [-4, -1, 1, 2]
nums2 = [-7,-11,12,-15,14,4,4,11,-11,2,-8,5,8,14,0,3,2,3,-3,-15,-2,3,6,1,2,8,-5,-7,3,1,8,11,-3,6,3,-4,-13,-15,14,-8,2,-8,4,-13,13,11,5,0,0,9,-8,5,-2,14,-9,-15,-1,-6,-15,9,10,9,-2,-8,-8,-14,-5,-14,-14,-6,-15,-5,-7,5,-11,14,-7,2,-9,0,-4,-1,-9,9,-10,-11,1,-4,-2,2,-9,-15,-12,-4,-8,-5,-11,-6,-4,-9,-4,-3,-7,4,9,-2,-5,-13,7,2,-5,-12,-14,1,13,-9,-3,-9,2,3,8,0,3]
target = 1


# print(Solution().threeSumClosest(nums,target))
print(Solution().threeSumClosest(nums2,target))
