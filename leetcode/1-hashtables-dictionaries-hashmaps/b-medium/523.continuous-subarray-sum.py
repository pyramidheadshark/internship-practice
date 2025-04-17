#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#

# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        prefix_mods = {0: -1}
        current_sum = 0

        for i in range(len(nums)):
            current_sum += nums[i]
            current_mod = current_sum % k

            if current_mod in prefix_mods:
                if i - prefix_mods[current_mod] > 1:
                    return True
            else:
                prefix_mods[current_mod] = i

        return False
# @lc code=end

