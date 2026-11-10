
class Queue:
    """Stores food orders using the First In, First Out (FIFO) principle."""

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add a new order to the back of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the oldest order."""
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def front(self):
        """View the oldest order without removing it."""
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        """Check whether the queue contains any orders."""
        return len(self.items) == 0

    def size(self):
        """Return the number of orders in the queue."""
        return len(self.items)
