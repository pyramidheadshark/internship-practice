#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
    
        for word in strs:
            sorted_word = ''.join(sorted(word))
            
            if sorted_word not in anagrams:
                anagrams[sorted_word] = [word]
            else:
                anagrams[sorted_word].append(word)
        
        return list(anagrams.values())
        
# @lc code=end

