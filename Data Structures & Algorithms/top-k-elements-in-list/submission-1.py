class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        sol = [-1001] * k
        print(sol)
        seen = {}
        seen[-1001] = -1

        for number in nums:
            if (number in seen.keys()):
                seen[number] += 1
            else:
                seen[number] = 1
            
            for i,val in enumerate(sol):
                if (seen[sol[i]] < seen[number]) & (number not in sol):
                        sol[i] = number
        return sol
