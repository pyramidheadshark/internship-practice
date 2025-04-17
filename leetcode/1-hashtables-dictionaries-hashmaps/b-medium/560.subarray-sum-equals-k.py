#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = {0: 1}
        
        current_sum = 0
        count = 0
        
        for num in nums:
            current_sum += num
            complement = current_sum - k
            
            count_complement = prefix_sums.get(complement, 0)
            count += count_complement
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
        
        return count
            
        
        
# @lc code=end

