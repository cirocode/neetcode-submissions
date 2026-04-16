class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        setOfNumbers = set()
        seenNumbers = {}
        kUnique = len(nums)

        i = 0
        
        while True:
            if (i==len(nums)):
                break
            if nums[i] in seenNumbers.keys():
                nums.pop(i)
                i -= 1
            else:
                seenNumbers[nums[i]] = 1
            i +=1

        return len(nums)