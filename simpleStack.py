class Stack:
    def __init__(self):
        self.items = []  # Initialize an empty list to represent the stack.

    def is_empty(self):
        return len(self.items) == 0  # Check if the stack is empty.

    def push(self, item):
        self.items.append(item)  # Add an item to the top of the stack.

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # Remove and return the top item from the stack.
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # Return the top item without removing it.
        else:
            raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)  # Return the number of items in the stack.


# Example usage:
if __name__ == "__main__":
    stack = Stack()  # Create a new stack.
    
    stack.push(1)  # Push 1 onto the stack.
    stack.push(2)  # Push 2 onto the stack.
    stack.push(3)  # Push 3 onto the stack.
    
    print("Stack:", stack.items)  # Print the stack: [1, 2, 3]
    print("Stack size:", stack.size())  # Print the size of the stack: 3
    print("Top element:", stack.peek())  # Print the top element: 3
    print("Popped element:", stack.pop())  # Pop and print the top element: 3
    print("Stack after pop:", stack.items)  # Print the stack after pop: [1, 2]
