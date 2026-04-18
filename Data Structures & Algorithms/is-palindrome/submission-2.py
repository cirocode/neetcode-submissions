class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        leftPointer = 0
        rightPointer = len(s)-1
        s = s.lower()

        while leftPointer < rightPointer:

            while leftPointer < rightPointer and not s[leftPointer].isalnum():
                leftPointer += 1

            while leftPointer < rightPointer and not s[rightPointer].isalnum():
                rightPointer -= 1

            if s[leftPointer] == s[rightPointer]:
                leftPointer += 1
                rightPointer -= 1
            else:
                return False
            

        return True