#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        reference_dict = dict()
        for char in p:
            if char not in reference_dict:
                reference_dict[char] = 1
            else:
                reference_dict[char] += 1
        
        dyn_dict = dict()
        for i in range(len(p)):
            char = s[i]
            if char not in dyn_dict:
                dyn_dict[char] = 1
            else:
                dyn_dict[char] += 1
        
        start_indices = []
        
        if reference_dict == dyn_dict:
            start_indices.append(0)
        
        for i in range(len(p), len(s)):
            char = s[i]
            previous_char = s[i - len(p)]
            
            dyn_dict[previous_char] -= 1
            if dyn_dict[previous_char] == 0:
                del dyn_dict[previous_char]
            
            if char not in dyn_dict:
                dyn_dict[char] = 1
            else:
                dyn_dict[char] += 1
            
            if reference_dict == dyn_dict:
                start_indices.append(i - len(p) + 1)
        
        
        return start_indices
            

# @lc code=end

