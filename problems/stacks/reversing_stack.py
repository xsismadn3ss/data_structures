from data_structures.stack import Stack


# revertir el orden de un stack, crear uno nuevo y poner los nodos en orden inverso
def reverse_stack(st: Stack):
    new_stack = Stack()
    while not st.is_empty:
        new_stack.push(st.pop())
    del st
    return new_stack


def print_stack(st: Stack):
    node = st.head
    while node:
        print(node)
        node = node.next


def main():
    stack_inicial = Stack()
    stack_inicial.push("este")
    stack_inicial.push("stack")
    stack_inicial.push("esta")
    stack_inicial.push("en")
    stack_inicial.push("orden")

    print("Stack inicial")
    print_stack(stack_inicial)

    stack_inicial = reverse_stack(stack_inicial)
    print("\n\nStack invertido")
    print_stack(stack_inicial)
