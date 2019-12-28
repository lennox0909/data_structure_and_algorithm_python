'''

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:
    Input: [1,8,6,2,5,4,8,3,7]
    Output: 49

https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg
'''

'''
自己寫的v1：Time Limit Exceeded 
Time complexity : O(n^2)
class Solution:
    def maxArea(self, height: list) -> int:
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2: return 0

        list_ = []
        for i in range(0,len(height)):
            for j in range(i+1,len(height)):
                H = min(height[i], height[j])
                W = j-i
                area = H * W
                list_.append(area)
        max_area = max(list_)
        return max_area

自己寫的v2：Time Limit Exceeded
取消max(list)
Time complexity : O(n^2)

class Solution:
    def maxArea(self, height: list) -> int:
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2: return 0

        max_area = 0
        for i in range(0,len(height)):
            for j in range(i+1,len(height)):
                H = min(height[i], height[j])
                W = j-i
                area = H * W
                if area > max_area:
                    max_area = area

        return max_area
'''

# Two Pointer Approach
# see https://leetcode.com/articles/container-with-most-water/
# Time complexity : O(n)

class Solution:
    def maxArea(self, height:list) -> int:
        water = 0
        head = 0
        tail = len(height) - 1

        for cnt in range(len(height)):

            width = abs(head - tail)

            if height[head] < height[tail]:
                res = width * height[head]
                head += 1
            else:
                res = width * height[tail]
                tail -= 1

            if res > water:
                water = res

        return water

h = [1,8,6,2,5,4,8,3,7]
h2 = [2,9]
ans = Solution().maxArea(h)
print(ans)
