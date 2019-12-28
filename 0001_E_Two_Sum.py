# class Solution:
#     def twoSum(self, nums, target):
#         l = len(nums)
#         for i in range(0, l):
#             for j in range(1, l):
#                 sumL = nums[i] + nums[j]
#                 while sumL == target:
#                     return [i, j]
#
#
# llist = [1, 2, 5, 3, 6, 3]
# target = 11
#
# a = Solution.twoSum(self=0, nums=llist, target=target)
# print(a)
#
# h = {}
# for k, v in enumerate(llist):
#     print(k, v)
#     h[k] = v
# print(h)

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]


llist = [1, 2, 5, 3, 6, 3]
target = 11
A = Solution()
b = A.twoSum(llist, target)
print(b)

c = Solution().twoSum(llist, target)
print(c)
