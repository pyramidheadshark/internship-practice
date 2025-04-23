#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        
        water_trapped = 0
        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        
        while left < right:
            if height[left] < height[right]:
                water_trapped += min(max_left, max_right) - height[left]
                left += 1
                max_left = max(max_left, height[left])
            
            else:
                water_trapped += min(max_right, max_left) - height[right]
                right -= 1
                max_right = max(max_right, height[right])
                
        return water_trapped
            
            
            
            
# @lc code=end

