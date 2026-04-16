class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        lettersInS = {}

        for letter in s:
            if letter in lettersInS.keys():
                lettersInS[letter] += 1
            else:
                lettersInS[letter] = 1
        
        for letter in t:
            if letter in lettersInS.keys():
                lettersInS[letter] -= 1
        
        for i in lettersInS.values():
            if i != 0:
                return False
    
        return True