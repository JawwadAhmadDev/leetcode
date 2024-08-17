class Stack:
    """
    Stack class using a Python list (array) for storage.
    It supports typical stack operations: push, pop, and peek.
    """
    def __init__(self):
        self.stack = []  # Initialize an empty list to represent the stack
    
    def is_empty(self):
        """
        Check if the stack is empty.
        Returns True if empty, False otherwise.
        """
        return len(self.stack) == 0
    
    def push(self, data):
        """
        Push a new element onto the stack.
        
        Steps:
        1. Append the data to the end of the list.
        """
        self.stack.append(data)  # Add the new data to the end of the list
    
    def pop(self):
        """
        Pop the top element from the stack.
        
        Steps:
        1. Check if the stack is empty. If yes, return None or raise an exception.
        2. Remove and return the last element of the list (the top element of the stack).
        """
        if self.is_empty():
            print("Stack is empty, cannot pop.")
            return None
        
        return self.stack.pop()  # Remove and return the last element
    
    def peek(self):
        """
        Peek at the top element without removing it.
        
        Returns the last element of the list (the top element of the stack) if the stack is not empty.
        """
        if self.is_empty():
            print("Stack is empty, nothing to peek.")
            return None
        
        return self.stack[-1]  # Return the last element without removing it
    
    def size(self):
        """
        Returns the number of elements in the stack.
        """
        return len(self.stack)
    
    def display(self):
        """
        Display the elements in the stack.
        """
        if self.is_empty():
            print("Stack is empty.")
            return
        
        print("Stack elements:", self.stack)


# Example usage:
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Top element is:", stack.peek())  # Should output 30

stack.display()  # Displays stack elements

print("Popped element is:", stack.pop())  # Should output 30
stack.display()  # Displays remaining stack elements
