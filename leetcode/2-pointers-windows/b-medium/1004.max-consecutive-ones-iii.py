#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count_zeros = 0
        left, right = 0, 0
        max_len = 0
        while right < len(nums):
            if nums[right] == 1:
                right += 1
            else:
                if count_zeros < k:
                    count_zeros += 1
                    right += 1
                else:
                    if nums[left] == 0:
                        count_zeros -= 1
                    left += 1
                        
            max_len = max(max_len, right - left)
            
        return max_len
                    
# @lc code=end

