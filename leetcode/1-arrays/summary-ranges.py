### Optimal lol
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = list()
        if len(nums) > 0:
            first_num = nums[0]
            current_num = int()

            for i in range(1, len(nums)):
                current_num = nums[i]
                previous_num = nums[i-1]

                if current_num != previous_num + 1:
                    if previous_num == first_num:
                        ranges.append(str(first_num))

                    else:
                        ranges.append(f'{first_num}->{previous_num}')
                    
                    first_num = current_num

            if current_num == first_num:
                ranges.append(str(first_num))

            elif len(nums) > 1:
                ranges.append(f'{first_num}->{current_num}')
            
            else: ranges.append(str(first_num))
        
        return ranges