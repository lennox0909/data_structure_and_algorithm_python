'''

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

Example 1:
    nums1 = [1, 3]
    nums2 = [2]
    The median is 2.0

Example 2:
    nums1 = [1, 2]
    nums2 = [3, 4]
    The median is (2 + 3)/2 = 2.5

'''


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = sorted(nums1 + nums2)
        Len = len(nums)
        if Len >= 2:
            INT = Len // 2 - 1
            INT1 = INT + 1
            OUT = Len % 2
            if OUT == 0:
                median = (nums[INT] + nums[INT1]) / 2.0
            else:
                median = nums[INT1]
        else:
            median = nums[0]
        return median

nums1 = [3]
nums2 = [-2,-1]

S = Solution()
ans = S.findMedianSortedArrays(nums1,nums2)
print(ans)
