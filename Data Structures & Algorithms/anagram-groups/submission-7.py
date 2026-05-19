class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # keep track of the used letters
            # list of 26, seen = [0] * 26

        groupedAnagrams = {}

        for string in strs:
            seen = [0] * 26
            for character in string:
                seen[ord(character) - ord('a')] += 1
            codedKey = "#".join(map(str,seen))

            if codedKey in groupedAnagrams:
                groupedAnagrams[codedKey].append(string)
            else:
                groupedAnagrams[codedKey] = [string]
        
        output = []

        for values in groupedAnagrams.values():
            output.append(values)
        return output