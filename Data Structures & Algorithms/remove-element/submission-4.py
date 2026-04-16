class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        left = 0

        seenValue = False

        for r in range(len(nums)):
            if (nums[left] != val):
                if (seenValue):
                    if (nums[r] != val):
                        nums[left] = nums[r]
                        left += 1
                else:
                    left += 1
            else:
                seenValue = True
                if (nums[r] != val):
                    nums[left] = nums[r]
                    left += 1
        if (seenValue == False):
            left +=1
        return left