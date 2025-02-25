### Native
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = list()
        
        if len(nums1) > len(nums2):
            nums2_unique = set(nums2)
            for current_number in nums2_unique:
                if current_number in nums1:
                    result.extend([current_number] * min(nums1.count(current_number), nums2.count(current_number)))
        else:
            nums1_unique = set(nums1)
            for current_number in nums1_unique:
                if current_number in nums2:
                    result.extend([current_number] * min(nums1.count(current_number), nums2.count(current_number)))
        
        return result
    
### Optimal
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = list()

        if len(nums1) < len(nums2):
            nums1_counts = {}
            for num in nums1:
                if num in nums1_counts:
                    nums1_counts[num] += 1
                else:
                    nums1_counts[num] = 1

            for num in nums2:
                if num in nums1_counts:
                    if nums1_counts[num] > 0:
                        result.append(num)
                        nums1_counts[num] -= 1

        else:
            nums2_counts = {}
            for num in nums2:
                if num in nums2_counts:
                    nums2_counts[num] += 1
                else:
                    nums2_counts[num] = 1

            for num in nums1:
                if num in nums2_counts:
                    if nums2_counts[num] > 0:
                        result.append(num)
                        nums2_counts[num] -= 1

        return result