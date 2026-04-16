class Solution:
    def calPoints(self, operations: List[str]) -> int:
        typesOfOperations = ["D", "+", "C"]
        newList = []

        for i in range(len(operations)):
            if operations[i] in typesOfOperations:
                if operations[i] == "D":
                    newList.append(newList[-1] * 2)
                elif operations[i] == "+":
                    newList.append(newList[-1] + newList[-2])
                elif operations[i] == "C":
                    newList.pop()
            else:
                newList.append(int(operations[i]))
        return sum(newList)
            
        