from data_structures.stack import Stack

def is_balanced(s: str):
    st = Stack()
    opening = set("([{")
    closing = set(")]}")
    pair = {")": "(", "]": "[", "}": "{"}

    for i in s:
        if i in opening:
            st.push(i)
        if i in closing:
            if st.is_empty:
                return False
            elif st.pop().data != pair[i]:
                return False
            else:
                continue
        continue
    if st.is_empty:
        return True
    return False


def main():
    s = "{}()"
    result = is_balanced(s)
    print(result)
