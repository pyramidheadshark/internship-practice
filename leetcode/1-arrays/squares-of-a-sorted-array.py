### Native
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        latest_i = 0

        for i in range(0, len(nums)):
            if nums[i] < 0:
                latest_i = i

        nums_sorted = nums[0:latest_i+1]
        nums_sorted = nums[latest_i+1:len(nums)] + nums_sorted[::-1]
        return [x**2 for x in nums_sorted]
    
### Optimal
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        index = n - 1
        result = [0] * n
        left = 0
        right = n - 1

        while left <= right:
            left_sq = nums[left]**2
            right_sq = nums[right]**2

            if left_sq > right_sq:
                result[index] = left_sq
                left += 1
            
            if left_sq <= right_sq:
                result[index] = right_sq
                right -= 1

            index -= 1
            
        return result
    
### Best (almost) lol
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(x*x for x in nums)