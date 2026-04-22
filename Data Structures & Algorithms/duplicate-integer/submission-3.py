class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for i in nums:
            if i in seen.keys():
                seen[i] += 1
            else:
                seen[i] = 1
        print(seen)

        for i in seen.values():
            if i > 1:
                return True

        return False