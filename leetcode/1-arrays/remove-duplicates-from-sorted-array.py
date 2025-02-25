### Optimal
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        last_num = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != last_num:
                nums[k] = nums[i]
                last_num = nums[i]
                k += 1
        
        return k