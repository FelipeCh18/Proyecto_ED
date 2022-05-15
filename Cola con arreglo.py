class Cola:
    def __init__(self):
        self.count = 0
        self.arr = []
        self.size = 10
        self.top = 0
        self.tail = 0
    
    def enqueue(self,data):
        if self.full() is False:
            self.arr.append(data)
            self.count+=1
            self.tail = (self.tail+1)%self.size
        else:
            print('Cola llena')
    
    def dequeue(self):
        if self.empty() is False:
            self.arr.remove(self.arr[0])
            self.count-=1
            self.top = (self.top+1)%self.size
        else:
            print('Cola vacia')
    
    def empty(self):
        return self.count == 0
    
    def full(self):
        return self.count >= self.size
    
    def output(self):
        print(self.arr)