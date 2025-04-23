#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        n = len(s)
        if n < 2:
            return s

        longest_start = 0
        longest_len = 1 

        def expand_around_center(left: int, right: int):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            
            start_index = left + 1
            end_index = right - 1
            
            return start_index, end_index
        
        for i in range(n):
            l1, r1 = expand_around_center(i, i)
            current_len1 = r1 - l1 + 1

            if i + 1 < n: 
                 l2, r2 = expand_around_center(i, i + 1)
                 current_len2 = r2 - l2 + 1
            else:
                 current_len2 = 0

            if current_len1 > longest_len:
                longest_len = current_len1
                longest_start = l1
            
            if current_len2 > longest_len:
                longest_len = current_len2
                longest_start = l2

        return s[longest_start : longest_start + longest_len]

# @lc code=end