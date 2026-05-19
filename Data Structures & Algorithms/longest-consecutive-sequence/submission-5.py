class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setOfNumbers = set(nums)

        longestConsecutive = 0

        for i in setOfNumbers:
            if i - 1 not in setOfNumbers:
                currentLongest = 1
                nextDigit = i + 1
                while nextDigit in setOfNumbers:
                    currentLongest += 1
                    nextDigit += 1
                longestConsecutive = max(currentLongest, longestConsecutive)
        return longestConsecutive
