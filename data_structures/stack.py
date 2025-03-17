from typing import Optional
import copy


class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

    def __str__(self):
        return f"{self.data}"


class StackOverFlowError(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class StackUnderFlowError(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class Stack:
    def __init__(self):
        self.head: Optional[Node] = None
        self.length: Optional[int] = 0

    @property
    def is_empty(self):
        return self.head is None

    def push(self, new_data):
        new_node = Node(new_data)
        if not new_node:
            raise StackOverFlowError("No es posible añadir un nuevo nodo")
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return

    def pop(self):
        if self.is_empty:
            raise StackUnderFlowError("El stack esta vacio")
        else:
            temp = copy.copy(self.head)
            self.head = self.head.next
            self.length -= 1
            return temp

    def peek(self):
        if not self.is_empty:
            return self.head.data
        raise StackUnderFlowError("El stack esta vacio")
