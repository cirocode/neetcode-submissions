class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # First brute force solution with 0(n) space and O(m+n) time complexity

        # seenLetter = {}

        # for i in range(len(s)):
        #     if s[i] in seenLetter.keys():
        #         seenLetter[s[i]] += 1
        #     else:
        #         seenLetter[s[i]] = 1

        # for i in range(len(t)):
        #     if t[i] in seenLetter.keys():
        #         seenLetter[t[i]] -= 1
        #     else:
        #         return False

        # for i in seenLetter.values():
        #     if i != 0:
        #         return False

        # return True

    # For a solution with O(n + m) time complexity and O(1) space

        alphabet = [0] * 26

        for i in s:
            alphabet[ord(i) - ord('a')] += 1
        for i in t:
            alphabet[ord(i) - ord('a')] -= 1

        for i in alphabet:
            if i != 0:
                return False
        return True



        