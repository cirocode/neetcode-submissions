class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        left = 0

        seenValue = False

        for r in range(len(nums)):
                if (nums[r] != val):
                    nums[left] = nums[r]
                    left += 1

        return left