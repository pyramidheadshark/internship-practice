#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniques_index = 0
        
        for pointer in range(1, len(nums)):
            if nums[uniques_index] != nums[pointer]:
                nums[uniques_index + 1] = nums[pointer]
                uniques_index += 1
        
        return uniques_index + 1

        
        
        
        
# @lc code=end

