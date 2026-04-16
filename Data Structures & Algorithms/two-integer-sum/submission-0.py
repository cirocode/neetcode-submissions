class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        previousNumbers = {}
        answer = []

        for i in range(len(nums)):
            if ((target - nums[i]) in previousNumbers.keys()):
                answer.append(previousNumbers[target - nums[i]])
                answer.append(i)
                break
            else:
                previousNumbers[nums[i]] = i
        return answer