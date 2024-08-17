class Node:
    """
    Node class represents each element in the stack.
    It contains the data and a reference (link) to the next node in the stack.
    """
    def __init__(self, data):
        self.data = data  # The value stored in this node
        self.next = None  # Pointer to the next node in the stack

class Stack:
    """
    Stack class using a linked list for dynamic storage.
    It supports typical stack operations: push, pop, and peek.
    """
    def __init__(self):
        self.top = None  # Initialize the stack with the top pointing to None (empty stack)
    
    def is_empty(self):
        """
        Check if the stack is empty.
        Returns True if empty, False otherwise.
        """
        return self.top is None
    
    def push(self, data):
        """
        Push a new element onto the stack.
        
        Steps:
        1. Create a new node with the provided data.
        2. Link the new node to the current top node.
        3. Update the top pointer to the new node.
        """
        new_node = Node(data)
        new_node.next = self.top  # New node points to the current top
        self.top = new_node  # Top now points to the new node
    
    def pop(self):
        """
        Pop the top element from the stack.
        
        Steps:
        1. Check if the stack is empty. If yes, return None or raise an exception.
        2. Store the top node's data.
        3. Update the top pointer to the next node in the stack.
        4. Return the stored data.
        """
        if self.is_empty():
            print("Stack is empty, cannot pop.")
            return None
        
        popped_node = self.top  # Get the top node
        self.top = self.top.next  # Update top to the next node
        return popped_node.data  # Return the data of the popped node
    
    def peek(self):
        """
        Peek at the top element without removing it.
        
        Returns the data of the top node if the stack is not empty.
        """
        if self.is_empty():
            print("Stack is empty, nothing to peek.")
            return None
        
        return self.top.data
    
    def display(self):
        """
        Display the elements in the stack.
        """
        if self.is_empty():
            print("Stack is empty.")
            return
        
        current = self.top
        print("Stack elements:")
        while current:
            print(current.data)
            current = current.next


# Example usage:
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Top element is:", stack.peek())  # Should output 30

stack.display()  # Displays stack elements

print("Popped element is:", stack.pop())  # Should output 30
stack.display()  # Displays remaining stack elements
