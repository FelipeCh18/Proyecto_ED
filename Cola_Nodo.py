class Nodo():
    def __init__(self, dato=None, next=None):
        self.dato=dato
        self.next=next

class Cola():
    def __init__(self):
        self.len_cola=0
        self.front=None
        self.rear=None

    def empty(self):
        return self.len_cola == 0

    def enqueue(self, dato):
        nodo=Nodo(dato)
        nodo.next=None
        if self.len_cola == 0:
            self.front=self.rear=nodo
        else:
            rear=self.rear
            rear.next=nodo
            self.rear=nodo
        self.len_cola+=1


    def dequeue(self):
        dato=self.front.dato
        self.front=self.front.next
        self.len_cola -= 1
        if self.len_cola==0:
            self.rear=None
        return dato


    def front(self):
        return self.front.dato