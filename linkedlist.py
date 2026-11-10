class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Manages customer records using a singly linked list."""

    def __init__(self):
        self.head = None

    def add_customer(self, data):
        """Add a new customer to the end of the list."""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def display_customers(self):
        """Display all customers in the linked list."""
        current = self.head

        while current is not None:
            print(current.data)
            current = current.next

    def search_customer(self, name):
        """Find a customer by name."""
        current = self.head

        while current is not None:
            if current.data["name"].lower() == name.lower():
                return current.data

            current = current.next

        return None

    def delete_customer(self, name):
        """Delete a customer using their name."""
        current = self.head
        previous = None

        while current is not None:
            if current.data["name"].lower() == name.lower():

                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next

                return True

            previous = current
            current = current.next

        return False

    def size(self):
        """Count the number of customers."""
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count
