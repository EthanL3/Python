'''
Course: CS 501
Term: Summer 2023
Student: Ethan Levine
Lab #1: Linked Lists and Stacks
Description: Evaluates whether a string containing various opening and closing
symbols has all the symbols balanced (i.e. each opening symbol has a corresponding
closing symbol). Returns True if all symbols are balanced, False if otherwise.
    Opening symbols: (, [, {
    Closing symbols: ), ], }
    Input: User input. Any string containing, but not limited to, these symbols
Development Environment: PyCharm 2023.1.3
Version: Python 3.9
Solution File: ethanlevinea1.py
Date:
'''

'''
Big O-Analysis:
The time and space complexity of the push and pop are O(1)
If n is the length of the input string, then the time complexity of 
our algorithm is O(n), since our algorithm runs over each character in the 
input once. 
The space complexity is O(n) in the worst possible case (all opening symbols). This
is because we would have to store every opening symbol in our stack.
If the input string is balanced, the space complexity is O(n/2) at worst.
'''


from ethanlevinestack import Stack
from ethanlevinenode import Node


def balanced_symbols(input_string):
    stack = Stack()

    opening_symbols = '({['
    closing_symbols = ')}]'

    for symbol in input_string:
        # Checks if symbol is not any of the opening or closing symbols
        if symbol not in opening_symbols and symbol not in closing_symbols:
            continue
        if symbol in opening_symbols:
            stack.push(symbol)
        elif symbol in closing_symbols:
            # Detects attempt to pop from an empty stack
            if stack.is_empty():
                print("Value Error. Unmatched closing symbol: '{}'".format(symbol))
                return False
            # Pops opening symbol on top of stack if stack isn't empty
            top = stack.pop()
            # Detects an incorrect pairing symbol popped from the stack, returns False
            if not matching(top, symbol):
                print("Value Error. Mismatched opening and closing symbols: '{}' and '{}'".format(top, symbol))
                return False
    # If opening symbols still remain on the stack then there is a mismatch
    # Stack must   be empty if all symbols ended up matching
    if not stack.is_empty():
        print("Value Error. Unmatched opening symbols remain on the stack")
        return False
    # Symbols are balanced if no other return statements triggered
    return True


def matching(opening, closing):
    if opening == '(' and closing == ')':
        return True
    elif opening == '[' and closing == ']':
        return True
    elif opening == '{' and closing == '}':
        return True
    return False


def main():
    # Three test cases given
    print("Output 1:", balanced_symbols("([|)]"))
    print("Output 2:", balanced_symbols("() (() [()])"))
    print("Output 3:", balanced_symbols("{{([][])}()}"))

    # Tests to pop from an empty stack
    print("Output 4:", balanced_symbols("]"))
    # Tests non symbol characters
    print("Output 5:", balanced_symbols("(ethan) (levine)"))
    # Tests incorrect symbol pairing popped from stack
    print("Output 6:", balanced_symbols("(]"))


if __name__ == "__main__":
    main()


'''
Value Error. Mismatched opening and closing symbols: '[' and ')'
Output 1: False
Output 2: True
Output 3: True
Value Error. Unmatched closing symbol: ']'
Output 4: False
Output 5: True
Value Error. Mismatched opening and closing symbols: '(' and ']'
Output 6: False
'''