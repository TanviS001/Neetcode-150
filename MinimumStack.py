# o(1) space and time
class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            if self.min_stack[-1]>=val:
                self.min_stack.append(val)
        else: 
            self.min_stack.append(val)

    def pop(self) -> None:
        val=self.stack.pop()
        if self.min_stack[-1]==val:
            self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1] 
        else:
            return -1

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return None
