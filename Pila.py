class Nodo():
    def __init__(self, dato=None, next=None):
        self.dato=dato
        self.next=next

class Pila():
    def __init__(self):
        self.top=None

    def push(self, dato):
        newp=Nodo()
        newp.next=self.top
        top=newp

    def pop(self):
        if not self.empty():
            n=self.top.dato
            top=self.top.next
            return n
        else:
            return -1

    def empty(self):
        return self.top==None


