#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_len = 0
        current_chars = dict()
        
        for i in range(len(s)):
            char = s[i]
            if char not in current_chars:
                current_chars[char] = i
                
            else:
                start = max(current_chars[char] + 1, start)
                current_chars[char] = i

            max_len = max(max_len, i - start + 1)
            
        return max_len
            
# @lc code=end

