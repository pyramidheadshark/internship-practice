#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i in range(len(nums)):
            num = nums[i]
            looking_for = target - num
            
            if looking_for in seen:
                return [seen[looking_for], i]
            
            seen[num] = i
        
        
# @lc code=end
