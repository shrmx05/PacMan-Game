class Stack:
    def __init__(self) -> None:
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def length(self):
        return len(self.items)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()   
        else:
            return [-1,-1]
    def is_empty(self):
        return len(self.items) == 0   