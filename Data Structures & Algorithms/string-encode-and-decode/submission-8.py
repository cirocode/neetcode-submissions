class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += str(len(string))+ "#" + string

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_list = []

        print(f"Encoded string sent is {s}")

        p = 0
        i = 0
        current_size = ""
        while p < len(s):
            current_character = s[p]

            if current_character == "#":
                print(f"current size is {current_size}")
                p += 1
                decoded_list.append(s[p:p+int(current_size)])
                i = p
                p += int(current_size)
                current_size = ""
            else:
                current_size += current_character
                p += 1
        
        return decoded_list

        

