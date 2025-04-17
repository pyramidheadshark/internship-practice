#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums = set(nums)
        
        for i in range(n + 1):
            if i not in nums:
                return i
# @lc code=end

