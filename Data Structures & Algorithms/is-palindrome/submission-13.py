class Solution:
    def isPalindrome(self, s: str) -> bool:
        stringLowerCase = s.lower()

        leftIndex = 0
        rightIndex = len(stringLowerCase) - 1

        while leftIndex < rightIndex:
            
            while leftIndex < rightIndex and not stringLowerCase[leftIndex].isalnum():
                leftIndex += 1
            while rightIndex > leftIndex and not stringLowerCase[rightIndex].isalnum():
                rightIndex -= 1

            if stringLowerCase[leftIndex] != stringLowerCase[rightIndex]:
                return False
            else:
                leftIndex += 1
                rightIndex -= 1
        return True