class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
    # One Way to do it

        # if len(set(nums)) == len(nums):
        #     return False
        # else:
        #     return True

    # If I can't use the set function then
        seen = {}

        for i in range(len(nums)):
            if nums[i] in seen:
                seen[nums[i]] += 1
            else:
                seen[nums[i]] = 1
        
        for values in seen.values():
            if values > 1:
                return True

        return False