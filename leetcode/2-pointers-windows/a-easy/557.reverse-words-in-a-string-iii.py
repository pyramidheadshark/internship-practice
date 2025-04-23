#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s + ' '
        s = list(s)
        
        word_pointer = 0
        left, right = 0, 0
        is_processed = True
        
        while word_pointer < len(s):
            if is_processed:
                if s[word_pointer] != ' ':
                    word_pointer += 1
                else:
                    is_processed = False
                    right = word_pointer - 1
            
            else:
                if left < right:
                    s[right], s[left] = s[left], s[right]
                    left += 1
                    right -= 1
                else:
                    is_processed = True
                    word_pointer += 1
                    left = word_pointer
        
        return "".join(s)[:-1]
                    
# @lc code=end

