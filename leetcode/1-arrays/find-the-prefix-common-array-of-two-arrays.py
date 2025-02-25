### Optimal
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        commons = []
        A_set = set()
        B_set = set()

        for i in range(len(A)):
            A_set.add(A[i])
            B_set.add(B[i])

            commons.append(len(A_set.intersection(B_set)))
        
        return commons
