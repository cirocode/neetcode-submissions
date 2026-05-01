class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        values = {}
        output = []

        frequency_buckets = [[] for i in range(len(nums) + 1)]

        for i in nums:

            if i in values.keys():
                values[i] += 1
            else:
                values[i] = 1
        
        for i in values.keys():
            print(f"key {i}")
            frequency_buckets[values[i] - 1].append(i)

        print(frequency_buckets)
        p = k - 1

        for i in range(len(nums)-1, -1, -1):
            for num in frequency_buckets[i]:
                output.append(num)

                if len(output) == k:
                    return output
