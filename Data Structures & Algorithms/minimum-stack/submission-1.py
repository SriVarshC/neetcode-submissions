class MinStack:

    def __init__(self):
        self.values = []
        self.mins = []
        

    def push(self, val: int) -> None:
        if not self.mins:
            current_min = val
        else:
            current_min = min(val,self.mins[-1])
        self.values.append(val)
        self.mins.append(current_min)

    def pop(self) -> None:
        self.values.pop()
        self.mins.pop()
        

    def top(self) -> int:
        return self.values[-1]
        

    def getMin(self) -> int:
        return self.mins[-1]
        
