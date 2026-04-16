class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        lPointer = 0
        rPointer = 0
        currentLargestToRight = -1

        for i in range(len(arr)):
            
            for j in range(i+1, len(arr)):
                if arr[j] > currentLargestToRight:
                    currentLargestToRight = arr[j]
            arr[i] = currentLargestToRight
            currentLargestToRight = -1

        arr[-1] = -1
        return arr


