from typing import Any

type stack_element = Any

class Stack():

    def __init__(self, starting_value) -> None:
        self.values: list[stack_element] = [starting_value]

    def push(self, new_value) -> None:
        self.values.append(new_value)

    def pop(self) -> stack_element:
        return self.values.pop(-1)

    @property
    def top(self) -> stack_element:
        return self.values[-1]
    
    @property
    def is_empty(self) -> stack_element:
        return True if len(self.values)==0 else False
    
    @property
    def stack_size(self) -> stack_element:
        return len(self.values)