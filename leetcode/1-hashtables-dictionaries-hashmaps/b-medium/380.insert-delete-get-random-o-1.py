#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
import random

class RandomizedSet:

    def __init__(self):
        self.values = []
        self.values_indexes = {}

    def insert(self, val: int) -> bool:
        if val in self.values_indexes:
            return False
        
        self.values_indexes[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.values_indexes:
            return False

        index_to_remove = self.values_indexes[val]
        last_val = self.values[-1]

        self.values[index_to_remove] = last_val
        self.values_indexes[last_val] = index_to_remove
        self.values.pop()

        del self.values_indexes[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

