#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        elif len(s) == 0:
            return True
        
        p_s, p_t = 0, 0
        while p_s < len(s) and p_t < len(t):
            if s[p_s] == t[p_t]:
                p_s += 1
            p_t += 1
            
            if p_s == len(s):
                return True
            
        return False
# @lc code=end

