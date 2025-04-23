#
# @lc app=leetcode id=986 lang=python3
#
# [986] Interval List Intersections
#

# @lc code=start
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if firstList == [] or secondList == []:
            return []
        
        pairs = list()
        p1, p2 = 0, 0
        
        while p1 < len(firstList) and p2 < len(secondList):
            a, b, c, d = firstList[p1][0], firstList[p1][1], secondList[p2][0], secondList[p2][1]
            
            if max(a, c) <= min(b, d):
                pairs.append([max(a, c), min(b, d)])
            
            if b < d:
                p1 += 1
            
            elif b > d:
                p2 += 1
                
            else:
                p1 += 1
                p2 += 1
                        
        return pairs
                    
# @lc code=end

