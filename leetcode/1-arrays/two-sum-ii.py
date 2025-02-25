### Native
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for p_right in range(0, len(numbers), -1):
            num2 = numbers[p_right]

            for p_left in range(p_right):
                num1 = numbers[p_left]

                if num1 + num2 == target:
                    return [p_left + 1, p_right + 1]
                
### Optimal
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p_left = 0
        p_right = len(numbers) - 1

        while p_left < p_right:
            current = numbers[p_left] + numbers[p_right]

            if current == target:
                return [p_left + 1, p_right + 1]

            elif current > target:
                p_right -= 1
            
            else:
                p_left += 1