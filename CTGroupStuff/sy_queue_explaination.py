class Queue1:
    def __init__(self):
        self.array = []
    
    def enqueue(self, item):
        self.array.append(item)
        
    def dequeue(self):
        if len(self.array) > 0:
            first = self.array[0]
            self.array = self.array[1:]
            return first
        else:
            print("Queue is empty")
class Queue2:
    def __init__(self):
        self.array = []
    
    def enqueue(self, item):
        self.array.insert(0,item)
        
    def dequeue(self):
        if len(self.array) > 0:
            last = self.array[-1]
            self.array = self.array[:-1]
            return last
        else:
            print("Queue is empty")