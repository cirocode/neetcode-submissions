class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenValues = set()

        for value in nums:
            if (value in seenValues):
                return True
            else:
                seenValues.add(value)

        return False;
        