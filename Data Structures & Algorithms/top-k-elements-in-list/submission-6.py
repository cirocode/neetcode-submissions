class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        bucket = []
        frequencyCount = {}

        for i in range(len(nums)):
            bucket.append([])
        
        
        for numbers in nums:
            if numbers in frequencyCount:
                frequencyCount[numbers] += 1
            else:
                frequencyCount[numbers] = 1
        
        for key in frequencyCount.keys():
            bucket[frequencyCount[key]-1].append(key)
        
        output = []
        index = len(nums) - 1

        for index in range(len(nums)-1, -1, -1):
            for numbers in bucket[index]:
                output.append(numbers)

                if len(output) == k:
                    return output