
class Stack:
    """Stores actions using the Last In, First Out (LIFO) principle."""

    def __init__(self):
        self.items = []

    def push(self, item):
        """Add a new item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the most recent item."""
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        """View the most recent item without removing it."""
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        """Check whether the stack contains any items."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)
