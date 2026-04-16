class MinStack:

    def __init__(self):
        self.stack = []
        self.orderedList = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        self.orderedList.append(val)
        self.orderedList.sort()

    def pop(self) -> None:
        poppedValue = self.stack.pop()
        self.orderedList.remove(poppedValue)
        self.orderedList.sort()

        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.orderedList[0]
        
