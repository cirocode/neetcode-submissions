class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if (len(s) != len(t)):
            return False

        lettersUsed = [0] * 26

        for i in range(len(s)):
            lettersUsed[ord(s[i]) - ord("a")] = lettersUsed[ord(s[i]) - ord("a")] + 1
            lettersUsed[ord(t[i]) - ord("a")] = lettersUsed[ord(t[i]) - ord("a")] - 1
        
        for x in lettersUsed:
            if (x != 0):
                return False
        return True
        