### Native
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_counter = 0

        for i in range(len(stones)):
            if stones[i] in jewels:
                jewels_counter += 1
        
        return jewels_counter
    
### Optimal
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_counter = 0
        jewels_set = set(jewels)

        for i in range(len(stones)):
            if stones[i] in jewels:
                jewels_counter += 1
        
        return jewels_counter