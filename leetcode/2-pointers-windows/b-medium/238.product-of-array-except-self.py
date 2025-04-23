#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all_product = 1
        count_nulls = 0
        
        for num in nums:
            if num == 0:
                count_nulls += 1
            else:
                all_product *= num
            
            if count_nulls > 1:
                return [0] * len(nums)
        
        answer = list()
        for i in range(len(nums)):
            num = nums[i]
            
            if count_nulls == 0:
                answer.append(all_product // num)
            elif count_nulls == 1:
                if num == 0:
                    answer.append(all_product)
                else:
                    answer.append(0)
        
        return answer
# @lc code=end

