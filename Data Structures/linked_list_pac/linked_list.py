from linked_list_pac.node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add_to_first(self, value):
        self.head = Node(value, self.head)

        if self.tail is None:
            self.tail = self.head

        self.size += 1
        return self

    def add_to_end(self, value):
        if self.is_empty():
            self.add_to_first(value)
            return self
        if self.tail.next_node is None:
            self.tail.next_node = Node(value)
            self.tail = self.tail.next_node
            self.size += 1
            return self

    def node_at(self, index):
        if isinstance(self.head, Node):
            current_node = self.head
            current_index = 0
            while current_node is not None and current_index < index:
                current_node = current_node.next_node
                current_index += 1
            return current_node
        else:
            print("head is not a Node")

    def insert(self, value, index):
        if index > self.size - 1:
            return self.add_to_end(value)
        if index <= 0:
            return self.add_to_first(value)

        before_node = self.node_at(index - 1)
        before_node.next_node = Node(value, before_node.next_node)
        self.size += 1
        return self

    def pop(self):
        if isinstance(self.head, Node):
            if self.is_empty() is False:
                self.size -= 1
            result = self.head.value
            self.head = self.head.next_node
            if self.is_empty():
                self.tail = None
            return result
        return None

    def remove_last(self):
        if self.head is None:
            return None
        else:
            if isinstance(self.head, Node):
                head = self.head
                if head.next_node is None:
                    return self.pop()

                self.size -= 1

                pre = head
                current = head
                next_node = head.next_node

                while next_node is not None:
                    pre = current
                    current = next_node
                    next_node = current.next_node

                pre.next_node = None
                self.tail = pre
                return current.value
            return None

    def to_string(self):
        if isinstance(self.head, Node):
            if self.is_empty():
                return "Empty list"
            else:
                return self.head.to_string()
        else:
            print("head is not a Node")
