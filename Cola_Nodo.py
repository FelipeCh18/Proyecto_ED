class Cola():
    def __init__(self):
        self.cola=[]
        self.size=0

    def empty(self):
        return len(self.cola) == 0

    def enqueue(self, dato):
        self.cola.append(dato)
        self.size+=1

    def dequeue(self):
        if self.empty():
            print("La cola está vacía")
        else:
            self.cola=[self.cola[i] for i in range(1,self.size)]
            self.size-=1

    def show(self):
        n=self.size-1
        while n>-1:
            print("[%d]  =>  %d"%(n,self.cola[n]))

    def front(self):
        if self.empty():
            print("Cola vacía")
        else:
            print(self.cola[0])