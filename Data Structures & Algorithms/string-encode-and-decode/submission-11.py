class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for string in strs:
            encodedString += str(len(string)) + "#" + string

        return encodedString

    def decode(self, s: str) -> List[str]:

        decodedList = []
        index = 0
        prevIndex = 0
        while index < len(s):
            currCharacter = s[index]

            while currCharacter != '#':
                currCharacter = s[index] 
                index += 1
            
            sizeOfString = int(s[prevIndex:index-1])
            decodedList.append(s[index:index+sizeOfString])
            index += sizeOfString
            prevIndex = index
            
        return decodedList

        