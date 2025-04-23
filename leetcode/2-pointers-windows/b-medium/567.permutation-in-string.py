#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        if len(s1) == 1:
            if s1 in set(s2):
                return True
            else:
                return False
        
        reference_dict = dict()
        
        for char in s1:
            if char not in reference_dict:
                reference_dict[char] = 1
            else:
                reference_dict[char] += 1
        
        dyn_dict = dict()
        for i in range(len(s1)):
            char = s2[i]
            if char not in dyn_dict:
                dyn_dict[char] = 1
            else:
                dyn_dict[char] += 1
        
        if reference_dict == dyn_dict:
            return True
        
        for pointer in range(len(s1), len(s2)):
            dyn_dict[s2[pointer - len(s1)]] -= 1
            if dyn_dict[s2[pointer - len(s1)]] == 0:
                del dyn_dict[s2[pointer - len(s1)]]
            
            if s2[pointer] not in dyn_dict:
                dyn_dict[s2[pointer]] = 1
            else:
                dyn_dict[s2[pointer]] += 1
                
            if reference_dict == dyn_dict:
                return True
            
        return False            
            
        
# @lc code=end

