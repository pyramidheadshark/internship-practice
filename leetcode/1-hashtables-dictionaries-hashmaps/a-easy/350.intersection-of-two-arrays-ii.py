#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        counted = {}
        for num in nums1:
            if num not in counted:
                counted[num] = 1
            else:
                counted[num] += 1
            
        answer = []
        for num in nums2:
            if num in counted and counted[num] > 0:
                answer.append(num)
                counted[num] -= 1
        
        return answer
        
# @lc code=end

