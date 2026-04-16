class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenIntegers = {}

        for i in nums:
            if i in seenIntegers.keys():
                return True
            else:
                seenIntegers[i] = 1
        return False