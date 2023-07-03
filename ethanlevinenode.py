'''
Course: CS 501
Term: Summer 2023
Student: Ethan Levine
Lab #1: Linked Lists and Stacks
Description: Defines the 'Node' class which makes up the elements of
a linked list. The node contains one data field which will store the symbol.
The node class contains a constructor, set and get methods, and helper methods to validate
the fields of the node.
Development Environment: PyCharm 2023.1.3
Version: Python 3.9
Solution File: ethanlevinenode.py
Date:
'''


class Node:
    def __init__(self, data=None, next_node=None):
        self._data = data
        self._next = next_node

    def set_data(self, data):
        # Uses helper functions to validate data before setting
        if self.validate_data(data):
            self._data = data
            return True
        else:
            return False

    def set_next(self, next_node):
        # Uses helper functions to validate pointer before setting
        if self.validate_next(next_node):
            self._next = next_node
            return True
        else:
            return False

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def points_to_another_node(self):
        return self._next is not None

    def validate_data(self, data):
        # Data must be string
        if isinstance(data, str):
            return True
        else:
            return False

    def validate_next(self, next_node):
        # Current node must point to another node before setting current's node's next value
        if isinstance(next_node, Node):
            return True
        else:
            return False