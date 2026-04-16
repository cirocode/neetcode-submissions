class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # if this is empty then return 0
        if not nums:
            return 0

        # Start at 1
        l = 1

        for r in range(1, len(nums)):
            if nums[r] != nums[l - 1]:
                nums[l] = nums[r]
                l += 1
        return l
        