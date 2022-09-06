'''
@@@@@@ Queue : FIFO Structure @@@@@@
'''
# Design Circular Queue
class MyCircularQueue:
    def __init__(self, k: int):
        self.k = k #size of the queue
        self.queue = []
        self.size = 0

    def enQueue(self, value: int) -> bool:
        #if not empty
        if self.queue: 
            if self.size < self.k:
                self.queue.append(value)
                self.size += 1
                return True #if successful
            else:
                return False
        #if empty
        else:
            self.queue.append(value)
            self.size += 1
            return True #if successful     

    def deQueue(self) -> bool:
        #if not empty
        if self.queue:
            self.queue = self.queue[1:]
            self.size -= 1
            return True #if successful
        #if empty
        else:
            return False

    def Front(self) -> int:
        #if not empty
        if self.queue:
            return self.queue[0]
        #if empty
        else:
            return -1

    def Rear(self) -> int:
        #if not empty
        if self.queue:
            return self.queue[-1]
        #if empty
        else:
            return -1

    def isEmpty(self) -> bool:
        if self.queue:
            return False
        else:
            return True

    def isFull(self) -> bool:
        if self.size == self.k:
            return True
        else:
            False

# Design Circular Queue (Best)
class MyCircularQueue:
    def __init__(self, k: int):
        self.size = k 
        self.length = 0 
        self.queue = [-1] * self.size 
        self.head = self.tail = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.tail] = value
        self.tail = (self.tail+1) % self.size 
        self.length += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False 
        self.head = (self.head+1) % self.size 
        self.length -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.tail-1]

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.size

'''
@@@@@@ Queue and BFS @@@@@@

Main scenarios of using BFS
1. Do traversal
2. Find the shortest path
'''
# Number of Islands


# Perfect Squares (BFS Template Version)
class Solution:
    def numSquares(self, n: int) -> int:

        # BFS template
        if n < 2: return n
        squares = [i**2 for i in range(1, int(n**0.5)+1)]
        queue = [n]
        cnt = 0

        while queue:
            cnt += 1
            for _ in range(len(queue)):
                node = queue.pop(0)
                for square in squares:
                    if node == square:
                        return cnt
                    if node < square:
                        break
                    queue.append(node-square)

            # eliminate duplicate to prevent exponential calls
            queue = list(set(queue))
        return cnt 

'''
@@@@@@ Stack : LIFO Structure @@@@@@
'''
# Min Stack
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        else:
            return

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return
    def getMin(self) -> int:
        if self.stack:
            return sorted(self.stack)[0]
        else:
            return

# Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s)%2 != 0:
            return False
        try:
            for p in s:
                if p is '(' or p is '{' or p is '[':
                    stack.append(p)
                elif p is ')':
                    temp = stack.pop()
                    if temp != '(':
                        return False
                elif p is '}':
                    temp = stack.pop()
                    if temp != '{':
                        return False
                elif p is ']':
                    temp = stack.pop()
                    if temp != '[':
                        return False
        except:
            return False
        if not stack:
            return True
        else:
            return False

# Valid Parentheses (better)
class Solution:
    def isValid(self, s: str) -> bool:              
        stack = []       
        for c in s:           
            if c == '(' or c == '[' or c == '{':               
                stack.append(c)
            else:      
                if len(stack) == 0:
                    return False
                
                if c == '}':
                    if stack[-1] == '{':
                        stack.pop(-1)
                    else:
                        return False
                if c == ')':
                    if stack[-1] == '(':
                        stack.pop(-1)
                    else:
                        return False
                if c == ']':
                    if stack[-1] == '[':
                        stack.pop(-1)
                    else:
                        return False                 
                    
        return len(stack) == 0

# Daily Temperatures (Fail : Time Limit)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        max_index = len(temperatures)
        answer = [0 for _ in range(max_index)]

        for i in range(max_index):
            today = temperatures[i]

            for j in range(i+1, max_index):
                if temperatures[j] > today:
                    answer[i] = j-i
                    break

        return answer

# Evaluate Reverse Polish Notation
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        result = 0
        stack = []
        for token in tokens:
            try:
                token = int(token)
                stack.append(token)
            except:
                if token == '+':
                    result = stack.pop() + stack.pop()
                    stack.append(result)
                elif token == '-':
                    a = stack.pop()
                    b = stack.pop()
                    result = b - a
                    stack.append(result)
                elif token == '*':
                    result = stack.pop() * stack.pop()
                    stack.append(result)
                elif token == '/':
                    a = stack.pop()
                    b = stack.pop()
                    result = int(b / a)
                    stack.append(result)
        return stack.pop()

# Evaluate Reverse Polish Notation (better)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = collections.deque()
        
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                x, y = stack.pop(), stack.pop()
                stack.append(y - x)
            elif token == "/":
                x, y = stack.pop(), stack.pop()
                stack.append(int(y / x))
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(token))
        
        return stack[0]

'''
@@@@@@ Stack and DFS @@@@@@
'''


'''
@@@@@@ Conclusion @@@@@@
'''