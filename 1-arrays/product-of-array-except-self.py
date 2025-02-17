### Native
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        prefix = [1] * length
        postfix = [1] * length

        result = []

        for i in range(1, length):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        for i in range(length - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]

        for i in range(length):
            result.append(prefix[i] * postfix[i])

        return result
    
### Optimal
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1] * length

        for i in range(1, length):
            result[i] = result[i - 1] * nums[i - 1]

        postfix_product = 1
        for i in range(length - 1, -1, -1):
            result[i] *= postfix_product
            postfix_product *= nums[i]

        return result