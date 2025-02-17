### Native
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        for i in range(length):
            if nums[i] == 0:
                for j in range(i + 1, length):
                    if nums[j] != 0:
                        nums[i] = nums[j]
                        nums[j] = 0
                        break
        return nums
    
### Optimal
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_null_pointer = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_null_pointer] = nums[i]
                non_null_pointer += 1
        
        for i in range(non_null_pointer, len(nums)):
            nums[i] = 0