# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explored two fundamental linear data structures: stacks and queues. I implemented both structures in Python and used a cat café scenario to demonstrate how each one organized and processed information. A stack follows Last-In, First-Out (LIFO), while a queue follows First-In, First-Out (FIFO).

## Learning Objectives

During this assignment, I implemented stack operations using a Python list and queue operations using collections.deque. I demonstrated LIFO and FIFO behavior, tested empty structures and single-item edge cases, applied both data structures to a real-world scenario, and documented the program with comments and descriptive output.

## Implementation and Real-World Scenario

For the stack, I created a cat profile update history for a cat café. Each profile update was added using push(). The pop() method removed the most recent update, while peek() displayed the latest update without removing it. The is_empty() method checked whether the stack contained any updates. This scenario demonstrated LIFO behavior because the most recent profile update was the first one undone.

For the queue, I created a line of cats waiting to receive treats at the café. The enqueue() method added cats to the end of the line, while dequeue() served the cat at the front. The front() method displayed the next cat to be served without removing it. The is_empty() method checked whether any cats remained in line. This scenario demonstrated FIFO behavior because the first cat to join the line was the first cat served.

## Testing and Edge Cases

I tested both data structures with four items to verify their expected processing order. I also tested what happened when removal and inspection methods were called on empty structures. These operations returned None instead of causing an error. Finally, I created single-item stacks and queues, removed their only items, and verified that both structures became empty.

## Memory Usage and Efficiency

Both data structures used more memory as additional items were added. If a structure contained n items, its space complexity was O(n). Stack insertion and removal at the end of a Python list typically took O(1) time. Queue insertion at the back and removal at the front of a deque also typically took O(1) time.

## Discussion Board Reflection

For my initial discussion post, I reflected on the concepts I learned, the challenges I encountered, and the differences between stacks and queues. I explained how these data structures applied to the cat café examples and how their processing order affected their usefulness in different situations.