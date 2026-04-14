class stack():
    def __init__(self):
        self.stack=[]

    def push(self,item):
        return self.stack.append(item)
    
    def safe_pop(self):
        if len(self.stack)==0:
            print("Stack is empty, nothing to pop")
            return None
        else:
            return self.stack.pop()
        
    def display(self):
        print("The item has been appended in the stack")

    def peek(self):
        if len(self.stack)>0:
             print(self.stack[-1])
        else:
            return None 
           
s=stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.display()
s.safe_pop()
s.peek()