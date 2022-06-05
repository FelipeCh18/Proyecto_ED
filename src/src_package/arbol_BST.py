class Nodo():
    def __init__(self, dato=None):
        self.left = None
        self.dato = dato
        self.right = None


class BST():
    root = Nodo()

    def __init__(self):
        self.root = None

    def BST_insert(self, dato):
        self.root = self.insert(dato, self.root)

    def insert(self, dato, nodo):
        if nodo == None:
            nodo = Nodo(dato)
        else:
            if dato < nodo.dato:
                nodo.left = self.insert(dato, nodo.left)
            else:
                if dato > nodo.dato:
                    nodo.right = self.insert(dato, nodo.right)
                else:
                    print("Item in tree and not inserted")
        return nodo

    def BST_remove(self, dato):
        self.root = self.remove(dato, self.root)

    def remove(self, dato, nodo):
        if nodo!=None:
            if dato<nodo.dato:
                nodo.left=self.remove(dato, nodo.left)
            else:
                if dato>nodo.dato:
                    nodo.right = self.remove(dato, nodo.right)
                else:
                    if nodo.left==None and nodo.right==None:
                        nodo=None
                    else:
                        if nodo.left==None:
                            nodo=nodo.left
                        else:
                            t=self.findMin(nodo.right)
                            nodo.dato=t.dato
                            nodo.right=self.remove(nodo.dato, nodo.right)
        else:
            print("Item not in tree and not removed")
        return nodo

    def findMin(self, nodo):
        if nodo!=None:
            while nodo.left!=None:
                nodo=nodo.left
        return nodo