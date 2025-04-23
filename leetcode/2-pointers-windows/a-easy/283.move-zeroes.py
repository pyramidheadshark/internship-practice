#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        left, right = 0, 0
        
        while right < len(nums):
            if nums[right] != 0:
                if nums[left] == 0:
                    nums[left] = nums[right]
                    nums[right] = 0
                left += 1
            right += 1
            
# @lc code=end

