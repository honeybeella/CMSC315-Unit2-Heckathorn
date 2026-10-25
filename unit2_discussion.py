
"""
============================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
============================================================
OVERVIEW:
This assignment demonstrates two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).
The examples use text editor undo history and a coffee shop line.
"""


from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # A list stores stack values, with the last item at the top.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Adding to the top supports LIFO: the newest item is removed first.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Return None if the stack is empty instead of causing an error.
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Peek lets us view the newest item while keeping it in the stack.
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # A deque supports efficient additions at the back and removals at the front.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # New arrivals join the back, so earlier arrivals are served first.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front.
        # Return None if the queue is empty instead of causing an error.
        if self.is_empty():
            return None
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # This shows who is next without changing the line.
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0



def main():
    print("=== UNIT 2: CAT CAFE STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # The stack tracks cat profile updates.
    # The most recent update is undone first (LIFO).

    print("\n=== STACK DEMO: CAT PROFILE UNDO ===")
    cat_updates = Stack()

    cat_updates.push("Updated Maui's feeding schedule")
    cat_updates.push("Changed Princess Charlotte's profile photo")
    cat_updates.push("Added Pele's favorite toy")
    cat_updates.push("Updated Kona's adoption status")

    print("Four cat profile updates were recorded.")
    print("Most recent update:", cat_updates.peek())

    print("Undoing profile updates in LIFO order:")
    while not cat_updates.is_empty():
        print("Undo:", cat_updates.pop())

    print("Is the update history empty?", cat_updates.is_empty())
    print("Trying to undo with no updates:", cat_updates.pop())
    print("Viewing the latest update when empty:", cat_updates.peek())

    # Test a stack containing one update.
    single_stack = Stack()
    single_stack.push("Updated Cheddar's profile")
    print("Single update:", single_stack.pop())
    print("Is the single-item stack empty?", single_stack.is_empty())

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Cats join the treat line in arrival order.
    # The first cat to join is served first (FIFO).

    print("\n=== QUEUE DEMO: CAT TREAT LINE ===")
    treat_line = Queue()

    treat_line.enqueue("Maui")
    treat_line.enqueue("Princess Charlotte")
    treat_line.enqueue("Pele")
    treat_line.enqueue("Kona")

    print("Four cats joined the treat line.")
    print("Next cat to receive a treat:", treat_line.front())

    print("Serving cats in FIFO order:")
    while not treat_line.is_empty():
        print("Treat served to:", treat_line.dequeue())

    print("Is the treat line empty?", treat_line.is_empty())
    print("Trying to serve from an empty line:", treat_line.dequeue())
    print("Checking the front of an empty line:", treat_line.front())

    # Test a queue containing one cat.
    single_queue = Queue()
    single_queue.enqueue("Cheddar")
    print("Next cat in the single-cat line:", single_queue.front())
    print("Treat served to:", single_queue.dequeue())
    print("Is the single-cat queue empty?", single_queue.is_empty())


if __name__ == "__main__":
    main()


