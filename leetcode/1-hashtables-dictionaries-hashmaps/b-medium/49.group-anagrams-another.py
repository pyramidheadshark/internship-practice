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
            counts = [0] * 26
            for char in word:
                counts[ord(char) - ord('a')] += 1
            key_tuple = tuple(counts)

            if key_tuple not in anagrams:
                anagrams[key_tuple] = [word]
            else:
                anagrams[key_tuple].append(word)

        return list(anagrams.values())
        
# @lc code=end

