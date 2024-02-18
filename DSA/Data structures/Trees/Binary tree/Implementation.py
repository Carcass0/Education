class Node[T]():
    
    def __init__(self, val: T):
        self.value = val
        self.left: Node = None
        self.right: Node = None
