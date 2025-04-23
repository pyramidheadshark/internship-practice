#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        seen_chars = dict()
        part_left, part_right = 0, 0
        pointer = 0
        answer = list()
        
        for i in range(len(s)):
            if s[i] not in seen_chars:
                seen_chars[s[i]] = i
            else:
                seen_chars[s[i]] = i
        
        while pointer < len(s):
            if seen_chars[s[pointer]] > part_right:
                part_right = seen_chars[s[pointer]]    
            
            if pointer == part_right:
                answer.append(part_right - part_left + 1)
                part_left = pointer + 1
                
            pointer += 1
        
        return answer

# @lc code=end

