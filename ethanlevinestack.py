'''
Course: CS 501
Term: Summer 2023
Student: Ethan Levine
Lab #1: Linked Lists and Stacks
Description: Defines the Stack ADT which will be used to store Nodes.
The Stack class contains a constructor, push, pop, peek, is_empty, create_stack, and
delete_stack methods. Here, we are using a stack implementation of a linked list, which
was defined in the Node class. The stack will use the "LIFO" approach, meaning the most recently
inserted element is at the beginning (top) of the Stack, and the first element inserted is at the end (bottom)
Development Environment: PyCharm 2023.1.3
Version: Python 3.9
Solution File: ethanlevinestack.py
Date:
'''

from ethanlevinenode import Node

class Stack:
    def __init__(self):
        self._head = None

    def push(self, data):
        new_node = Node(data)
        new_node.set_next(self._head)
        self._head = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped_data = self._head.get_data()
        self._head = self._head.get_next()
        return popped_data

    def peek(self):
        if self.is_empty():
            return None
        return self._head.get_data()

    def is_empty(self):
        return self._head is None

    @classmethod
    def create_stack(cls, data_list):
        stack = cls()
        for data in data_list:
            stack.push(data)
        return stack

    def delete_stack(self):
        self._head = None

