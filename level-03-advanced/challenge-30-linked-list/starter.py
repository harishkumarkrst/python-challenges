class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None


    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node


    def prepend(self, value):
        new_node = Node(value)

        new_node.next = self.head
        self.head = new_node


    def delete(self, value):
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        prev = self.head
        current = self.head.next

        while current is not None:
            if current.value == value:
                prev.next = current.next
                return

            prev = current
            current = current.next


    def contains(self, value):
        current = self.head

        while current is not None:
            if current.value == value:
                return True

            current = current.next

        return False


    def to_list(self):
        result = []
        current = self.head

        while current is not None:
            result.append(current.value)
            current = current.next

        return result


    def length(self):
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count


    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev

            prev = current
            current = next_node

        self.head = prev