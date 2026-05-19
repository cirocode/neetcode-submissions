class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        leftIndex = 0
        rightIndex = len(numbers)-1

        while leftIndex < rightIndex:
            currentSum = numbers[leftIndex] + numbers[rightIndex]
            
            if currentSum < target:
                leftIndex += 1
            elif currentSum > target:
                rightIndex -= 1
            else:
                return [leftIndex + 1, rightIndex + 1]