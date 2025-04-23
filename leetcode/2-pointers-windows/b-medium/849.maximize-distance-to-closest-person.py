#
# @lc app=leetcode id=849 lang=python3
#
# [849] Maximize Distance to Closest Person
#

# @lc code=start
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_dist = 1
        left, right = 0, 1
        first_null = seats[0] == 0
        last_null = seats[-1] == 0
        
        while right < len(seats):
            if seats[right] == 1:
                if first_null:
                    max_dist = max(max_dist, right - left)
                    first_null = False
                else:
                    max_dist = max(max_dist, (right - left) // 2)
                left = right
            right += 1
        
        if last_null:
            max_dist = max(max_dist, right - left - 1)
            
        
        return max_dist
                
        
# @lc code=end

