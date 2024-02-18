class Queue[T]():

    def __init__(self, length:int = 0) -> None:
        if length:
            self.values: list[T] = [0] * length
            self.length = length
        else:
            self.values: list[T] = []
    
    def enqueue(self, value: T) -> None:
        self.values.append(value)

    def dequeue(self) -> T:
        return self.values.pop(0)
    
    @property
    def front(self) -> T:
        return self.values[0]
    
    @property
    def rear(self) -> T:
        return self.values[-1]
    
    @property
    def isFull(self) -> bool:
        if not hasattr(self, 'length'):
            return False
        else: 
            if len(self.values) == self.values:
                return True
            else: return False
        
    @property
    def isEmpty(self) -> bool:
        if len(self.values) == 0:
            return True
        else: return False

    @property
    def size(self) -> int:
        return len(self.values)
