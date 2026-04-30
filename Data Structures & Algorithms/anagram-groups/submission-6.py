class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen = {}
        for i in strs:
            key = [0] * 26

            for char in i:
                key[ord(char) - ord('a')] += 1
            
            key_code = "#".join(map(str,key))
            if key_code in seen.keys():
                seen[key_code].append(i)
            else:
                seen[key_code] = [i]

        for i in seen.values():
            print(i)
        return list(seen.values())
                
        