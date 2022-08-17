import random


class node:
    def __init__(this, id_=None, next_=None):
        this.id = id_
        this.next = next_
    def __eq__(this, anobj):
        return this is anobj
    def __repr__(this):
        return f"{this.id}"
    def set_next(this, next_):
        assert isinstance(next_, type(this))
        this.next = next_
    def advance(this):
        return this.next
    def double_advance(this):
        n = this.advance()
        if n is None:
            return n
        else:
            n =n.advance()
            return n


def cycle_detect(head):
    slow = head
    fast = head
    while True:
        slow = slow.advance()
        fast = fast.double_advance()
        if fast is None:
            print("No cycle")
            return
        if slow is fast:
            print("Cycle detected")
            break
    slow = head
    while slow is not fast:
        slow = slow.advance()
        fast = fast.advance()
    print("Cycle starts at",slow)


def main():
    length = random.randint(13,40)
    nodes = [node(n) for n in range(length)]
    for node1, node2 in zip(nodes[:-1], nodes[1:]):
        node1.set_next(node2)
    loop_end = random.randint(10, len(nodes) - 2)
    loop_start = random.randint(0, loop_end)
    nodes[loop_end].set_next(nodes[loop_start])
    cycle_detect(nodes[0])
    print(F"{length = } {loop_start = } {loop_end = }")


if __name__=="__main__":
    main()
