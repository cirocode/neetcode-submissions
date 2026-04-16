class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = []

        mapValues = {}
        for i,value in enumerate(strs):
            keyValues = [0] * 26
            for c in value:
                keyValues[ord(c) - ord("a")] += 1
            if (tuple(keyValues) in mapValues.keys()):
                mapValues[tuple(keyValues)].append(value)
            else:
                mapValues[tuple(keyValues)] = [value]
            
        return list(mapValues.values())


    