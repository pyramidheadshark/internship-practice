#
# @lc app=leetcode id=395 lang=python3
#
# [395] Longest Substring with At Least K Repeating Characters
#

# @lc code=start
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        latest_char = s[0]
        latest_char_count = 1
        max_len = 0
        current_len = 1
        
        for i in range(1, len(s)):
            char = s[i]
            
            if char == latest_char:
                latest_char_count += 1
                current_len += 1
            
            else:
                latest_char = s[i]
                max_len = max(max_len, current_len)
                
                if latest_char_count < k:
                    current_len = 0
                else:
                    current_len += 1
            
            latest_char_count = 1

        return max_len
                    
            
# @lc code=end

