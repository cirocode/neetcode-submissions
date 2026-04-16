class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxConsecutive = 0
        currentConsecutive = 0

        for i in nums:
            if i == 1:
                currentConsecutive += 1
            else:
                maxConsecutive = max(maxConsecutive, currentConsecutive)
                currentConsecutive = 0
        maxConsecutive = max(maxConsecutive, currentConsecutive)
        
        return maxConsecutive