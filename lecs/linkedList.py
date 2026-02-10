class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def value(self):
        return self.data

class linked_list():
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def append(self, val):
        valN = Node(val)
        if self.head is not None:
            self.tail.next = valN
            self.tail = valN
            self.length += 1
        else:
            self.head = valN
            self.tail = valN
            self.length += 1

    def __repr__(self) -> str:
        nodes = []
        while self.head is not None:
            nodes.append(self.head.value())
            self.head = self.head.next
        nodes.append("None")
        return " -> ".join([str(item) for item in nodes])


ll = linked_list()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

print(ll)
