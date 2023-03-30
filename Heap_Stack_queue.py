import heapq #heap
from queue import LifoQueue #queue
H = [21,1,45,78,3,5]
# Create the list

#makes list to heapq (PriorityQueue)
heapq.heapify(H)
print(H)

# Replace an element
heapq.heapreplace(H,6)
print(H)


#QUEUE
myStack = LifoQueue()
myStack.get()
myStack.get()
myStack.get()

#STACK
# Python program to
# demonstrate stack implementation
# using list
 
stack = []
 
# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')
 
print('Initial stack')
print(stack)
 
# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
 
print('\nStack after elements are popped:')
print(stack)
 
# uncommenting print(stack.pop())
# will cause an IndexError
# as the stack is now empty