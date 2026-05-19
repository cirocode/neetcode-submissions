class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for index, value in enumerate(nums):
            if target - value in seen.keys():
                return [min(index,seen[target-value]), max(index,seen[target-value])]
            else:
                seen[value] = index
        return []