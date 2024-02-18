class DEQueue[T]():

    def __init__(self, size:int):
        self.values:list[T] = [0] * size
        self.size = size
        self.front = -1
        self.rear = 0

    @property
    def is_full(self) -> bool:
        return ((self.front == 0 and self.rear == self.size-1) or (self.front == self.rear+1))

    @property
    def is_empty(self) -> bool:
        return (self.front == -1)
    
    def insert_front(self, value:T) -> None:
        if not self.is_full:
            if self.front == 0:
                self.front = self.size - 1
            else:
                self.front -= 1
            self.values[self.front] = value
    
    def insert_rear(self, value:T) -> None:
        if not self.is_full:
            if self.rear == self.size - 1:
                self.rear = 0
            else:
                self.rear += 1
            self.values[self.rear] = value
    
    def delete_front(self) -> None:
        if not self.is_empty:
            if self.front == self.rear:
                self.front == -1
                self.rear == -1
                return
            if self.front == self.size-1:
                self.front = 0
                return
            self.front += 1
    
    def delete_rear(self) -> None:
        if not self.is_empty:
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
                return
            if self.rear == 0:
                self.rear = self.size - 1
                return
            self.rear -= 1
    
    def get_front(self) -> T:
        return self.values[self.front]
    
    def get_rear(self) -> T:
        return self.values[self.rear]