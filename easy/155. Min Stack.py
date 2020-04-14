'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

'''

#1
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data=[]
        self.helper=[]

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> None:
        self.data.pop()


    def top(self) -> int:
        return self.data[-1]


    def getMin(self) -> int:
        return min(self.data)



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data=[]
        self.helper=[]

    def push(self, x: int) -> None:
        self.data.append(x)
        if not self.helper:
            self.helper.append(x)
        else:
            self.helper.append(min(x,self.helper[-1]))

    def pop(self) -> None:
        self.data.pop()
        self.helper.pop()


    def top(self) -> int:
        return self.data[-1]


    def getMin(self) -> int:
        return self.helper[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()