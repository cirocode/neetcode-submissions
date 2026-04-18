class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        leftPointer = 0
        rightPointer = len(s)-1
        s = s.lower()
        print(s)

        while leftPointer < rightPointer:

            while leftPointer < rightPointer and not s[leftPointer].isalnum():
                leftPointer += 1

            while leftPointer < rightPointer and not s[rightPointer].isalnum():
                rightPointer -= 1

            print(f"Left {leftPointer}")
            print(f"Right {rightPointer}")  

            if s[leftPointer] == s[rightPointer]:
                leftPointer += 1
                rightPointer -= 1
            else:
                print(s[leftPointer])
                print(s[rightPointer])
                return False
            

        return True