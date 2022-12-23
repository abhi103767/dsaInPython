
class Node:
    def __init__(self,val,next=None) -> None:
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, val=None):
        self.head = None
        self.tail = None
        if val is not None:
            self.add_multiple_nodes(val)
    def __str__(self):
        return ' -> '.join([str(node) for node in self])
    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
    @property
    def val(self):
        return [node.val for node in self]
    def add_node(self, val):
        if self.head is None:
            self.tail = self.head = Node(val)
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
        return self.tail

    def add_node_as_head(self, val):
        if self.head is None:
            self.tail = self.head = Node(val)
        else:
            self.head = Node(val, self.head)
        return self.head