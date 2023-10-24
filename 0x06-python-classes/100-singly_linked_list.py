#!/usr/bin/python3

class Node:
    """This is a definition of a class named Node."""
    
    def __init__(self, data, next_node=None):
        """Constructor for the Node class."""
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Getter method to get the data stored in the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method to set the data of the node."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter method to get the reference to the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method to set the reference to the next node."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """This is a definition of a class named SinglyLinkedList."""

    def __init__(self):
        """Constructor for the SinglyLinkedList class."""
        self.head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list (increasing order)."""
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Generates a string representation of the linked list."""
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result
