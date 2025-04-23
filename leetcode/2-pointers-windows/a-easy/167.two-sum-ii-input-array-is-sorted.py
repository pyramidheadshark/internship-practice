#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index_sums = dict()
        
        for i in range(len(numbers)):
            needed = target - numbers[i]
            
            if needed in index_sums:
                return [index_sums[needed] + 1, i + 1]
            
            if numbers[i] not in index_sums:
                index_sums[numbers[i]] = i
            
                                   
                                   
# @lc code=end

