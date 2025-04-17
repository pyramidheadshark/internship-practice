#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        
        for i in range(len(s)):
            if s[i] not in seen:
                seen[s[i]] = i
            
            else:
                seen[s[i]] = -1
                
        for symb in s:
            if symb in seen and seen[symb] != -1:
                return seen[symb]
        
        return -1
# @lc code=end

