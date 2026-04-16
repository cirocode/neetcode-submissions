class Solution:
    def isValid(self, s: str) -> bool:

        if (len(s) == 1):
            return False

        diffChars = {'[': ']', '{': '}', '(': ')'}
        currOrder = []

        for char in s:
            if (char in diffChars.keys()):
                currOrder.append(diffChars[char])
            elif ((len(currOrder) != 0)):
                if (char == currOrder[len(currOrder)-1]):
                    currOrder.pop(len(currOrder)-1)
                else:
                    return False
            else:
                return False
        if (len(currOrder) != 0):
            return False
        return True
        