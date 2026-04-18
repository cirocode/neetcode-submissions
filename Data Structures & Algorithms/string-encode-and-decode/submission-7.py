class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for i in range(len(strs)):
            encoded_string += str(len(strs[i])) + "#" + strs[i]
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decodedList = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            sizeOfStr = int(s[i:j])
            j += 1
            word = s[j:j+sizeOfStr]

            decodedList.append(word)

            i = j+sizeOfStr

        return decodedList
