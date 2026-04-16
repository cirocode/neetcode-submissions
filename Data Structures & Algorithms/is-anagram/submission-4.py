class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        stringOneAsList = []
            
        for char in s:
            stringOneAsList.append(char)
        
        for char in t:
            if (char in stringOneAsList):
                stringOneAsList.remove(char)
            else:
                return False
        
        if len(stringOneAsList) == 0:
            return True

        return False