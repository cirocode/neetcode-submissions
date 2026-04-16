class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        # currentLargestToRight = -1

        # for i in range(len(arr)):
        #     for j in range(i+1, len(arr)):
        #         if arr[j] > currentLargestToRight:
        #             currentLargestToRight = arr[j]
        #     arr[i] = currentLargestToRight
        #     currentLargestToRight = -1

        # arr[-1] = -1
        # return arr

        # Iterate right to left keep track of larges value

        currLargest = arr[-1]
        prevLargest = -1

        for i in range(len(arr)-1,0, -1):
            prevLargest = arr[i-1]
            if arr[i] > currLargest:
                currLargest = arr[i]
            arr[i-1] = currLargest

            currLargest = max(prevLargest, currLargest)


        arr[-1] = -1
        return arr

