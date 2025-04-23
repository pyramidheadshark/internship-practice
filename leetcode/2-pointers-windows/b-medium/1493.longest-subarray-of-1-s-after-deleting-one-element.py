#
# @lc app=leetcode id=1493 lang=python3
#
# [1493] Longest Subarray of 1's After Deleting One Element
#

# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        seen_zero = False
        
        max_len = 0
        previous_len = 0
        current_len = 0
        pointer = 0
        
        while pointer < len(nums):
            if nums[pointer] == 1:
                current_len += 1
            else:
                seen_zero = True
                max_len = max(max_len, previous_len + current_len)
                previous_len = current_len
                current_len = 0

            pointer += 1
            
        if not seen_zero:
            max_len = max(max_len, current_len + previous_len - 1)
        else:
            max_len = max(max_len, previous_len + current_len)
            
        return max_len
# @lc code=end

