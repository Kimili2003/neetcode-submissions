class MinStack:

    def __init__(self):
        self.stack = []
        self.curr = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        temp = min(val, self.curr[-1] if self.curr else val)
        self.curr.append(temp)


    def pop(self) -> None:
        self.stack.pop()
        self.curr.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.curr[-1]
        
