#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = list()
        
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left]**2 > nums[right]**2:
                answer.append(nums[left]**2)
                left += 1
            else:
                answer.append(nums[right]**2)
                right -= 1
        
        return answer[::-1]
# @lc code=end

