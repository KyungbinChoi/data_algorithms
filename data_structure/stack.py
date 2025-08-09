from typing import Generic, TypeVar, Iterable, Optional, List

T = TypeVar("T")

class Stack(Generic[T]):  
    def __init__(self, data: Optional[Iterable[T]] = None) -> None:
        self.data: List[T] = []
        if data:
            # for x in data: self.push(x)
            pass

    def push(self,element):
        self.data.append(element)

    def pop(self):
        try:
            return self.data.pop()
        except IndexError:
            raise IndexError("pop from empty stack")
        
    def is_empty(self):
        return len(self.data)==0
    
    def peek(self):
        try:
            return self.data[-1]
        except IndexError:
            raise IndexError("pop from empty stack")
        
    def __len__(self):
        return len(self.data)