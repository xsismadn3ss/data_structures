from data_structures.stack import Stack


def main():
    """
    Este ejecicio consiste en eliminar el elemento del medio de una pila. (stack)
    """
    example = [10, 20, 30, 40, 50, 60, 70]
    print("Lista de ejemplo: {}".format(example))

    st = Stack()
    for item in example:
        st.push(item)
    middle = st.length / 2

    to_delete = None
    if middle % 1 == 0.5:
        to_delete = middle + 0.5
    else:
        to_delete = middle

    example = []

    while not st.is_empty:
        if st.length == to_delete:
            omited = st.pop()
            print("omitiendo item: {}".format(omited))
        else:
            example.append(st.pop().data)

    example = example[::-1]
    print("Lista resultante: {}".format(example))
