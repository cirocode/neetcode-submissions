class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += str(len(string))+ "#" + string

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        p = 0
        current_size = ""
        while p < len(s):
            current_character = s[p]

            if current_character == "#":
                p += 1
                decoded_list.append(s[p:p+int(current_size)])
                p += int(current_size)
                current_size = ""
            else:
                current_size += current_character
                p += 1
        
        return decoded_list

        

