### Optimal
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_unique = set(nums1)
        nums2_unique = set(nums2)

        nums1_distinct = [x for x in nums1_unique if x not in nums2_unique]
        nums2_distinct = [x for x in nums2_unique if x not in nums1_unique]

        return [nums1_distinct, nums2_distinct]