class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def append(self, data):
        # If there are no elements in the LL, the new_node is created
        if self.head is None:
            # Last node always points to None
            new_node = Node(data, None)
            return None
        # Iterating through linked list using the itr pointer
        # we first set the pointer to be the address of the first element.
        # Since the first element's pointer points to the next element, we want to set the itr
        # variable to be the .next of each element
        # once itr.next = None, the while loop will close
        itr = self.head
        while itr.next:
            itr = itr.next
        # We are now at the end of the list. We now create a new Node, which points to None since it's the
        # last element. We set the current next pointer to point to this new Node which is now the end element
        itr.next = Node(data, None)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            return None
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                return None
            itr = itr.next
            count += 1

    def print(self):
        if self.head is None:
            print("Linked list is empty")
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        llstr += 'None'
        print(llstr)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_start(data)
            return None
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                return None
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
        if self.head.data == data_after:
            self.head.next == Node(data_to_insert, self.head.next)
            return
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                return

    def remove_by_value(self,data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                return
            itr = itr.next




if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.insert_at(1, "blueberry")
    ll.remove_at(2)
    ll.print()

    ll.insert_values([45, 7, 12, 567, 99])
    ll.insert_at_end(67)
    ll.print()