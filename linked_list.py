"""A simple implementation of a singly linked list in Python."""
class LinkedList:
    """Class representing a singly linked list."""
    class Node:
        """Class representing a node in the linked list."""

        def __init__(self, element):
            self.element = element
            self.next = None

    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        """Check if the linked list is empty."""
        return self.length == 0

    def add(self, element):
        """Add an element to the end of the linked list."""
        node = self.Node(element)
        if self.is_empty():
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
        self.length += 1

    def remove(self, element):
        """Remove the first occurrence of an element from the linked list."""
        previous_node = None
        current_node = self.head
        while current_node is not None and current_node.element != element:
            previous_node = current_node
            current_node = current_node.next
        if current_node is None:
            return
        elif previous_node is not None:
            previous_node.next = current_node.next
        else:
            self.head = current_node.next
        self.length -= 1


my_list = LinkedList()
print(my_list.is_empty())

my_list.add(1)
my_list.add(2)
print(my_list.is_empty())
print(my_list.length)

my_list.remove(1)
print(my_list.length)
