class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # First brute force solution

        seenLetter = {}

        for i in range(len(s)):
            if s[i] in seenLetter.keys():
                seenLetter[s[i]] += 1
            else:
                seenLetter[s[i]] = 1

        for i in range(len(t)):
            if t[i] in seenLetter.keys():
                seenLetter[t[i]] -= 1
            else:
                return False

        for i in seenLetter.values():
            if i != 0:
                return False

        return True

        