class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Brute for is O(n^2) by going through the list comparing it with each value


        seen = {}

        for index, value in enumerate(nums):

            if target - value in seen.keys():
                return [seen[target-value], index]
            else:
                seen[value] = index

        return []
