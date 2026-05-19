class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        alphabetLetters = [0] * 26

        for index in range(len(s)):
            alphabetLetters[ord(s[index]) - ord('a')] += 1
            alphabetLetters[ord(t[index]) - ord('a')] -= 1

        for numbers in alphabetLetters:
            if numbers != 0:
                return False

        return True
