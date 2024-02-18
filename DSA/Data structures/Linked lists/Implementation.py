"""Какая глупость. На кой делать списки в питоне. Бредом занимаюсь."""
from typing import Any
class Node():
    
    def __init__(self, data):
        self.data: Any = data
        self.next: Node | None = None

    def __hash__(self):
        return hash(id(self))
    
    def insert_next(self, new):
        self.next: Node | None = new


class DoublyLinkedNode(Node):
    
    def __init__(self, data, prev):
        super.__init__(data)
        self.prev:DoublyLinkedNode | None = prev
    
    def __hash__(self):
        return hash(id(self))
    
    def insert_before(self, new):
        self.prev.next = new
        pass

class LinkedList():

    def __init__(self):
        self.head = None
        self.last = None