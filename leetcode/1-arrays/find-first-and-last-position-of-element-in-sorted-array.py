### Optimal
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        p_left = 0
        p_right = len(nums)

        answer = [-1, -1]

        while p_left < p_right:
            p_mid = p_left + (p_right - p_left) // 2
            
            if nums[p_mid] == target:
                while p_mid >= 0 and nums[p_mid] == target:
                    answer[0] = p_mid
                    p_mid -= 1

                p_mid += 1

                while p_mid < len(nums) and nums[p_mid] == target:
                    answer[1] = p_mid
                    p_mid += 1
                
                break

            elif nums[p_mid] > target:
                p_right = p_mid

            else:
                p_left = p_mid + 1
            
        return answer