class Nodo():
    def __init__(self, dato=None):
        self.left = None
        self.dato = dato
        self.right = None


class BST():
    root = Nodo()

    def __init__(self):
        self.root = None

    def BST_insert(self, edificio):
        self.root = self.insert(edificio, self.root)

    def insert(self, edificio, nodo):
        if nodo == None:
            nodo = Nodo(edificio)
        else:
            if edificio.num_edificio < nodo.dato.num_edificio:
                nodo.left = self.insert(edificio, nodo.left)
            else:
                if edificio.num_edificio > nodo.dato.num_edificio:
                    nodo.right = self.insert(edificio, nodo.right)
                else:
                    print("Item in tree and not inserted")
        return nodo

    def BST_remove(self, dato):
        self.root = self.remove(dato, self.root)

    def remove(self, dato, nodo):
        if nodo!=None:
            if dato<nodo.dato.num_edificio:
                nodo.left=self.remove(nodo.dato, nodo.left)
            else:
                if dato>nodo.dato.num_edificio:
                    nodo.right = self.remove(nodo.dato, nodo.right)
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

    def find(self, dato, raiz):
        if raiz.dato.num_edificio==dato:
            return raiz.dato
        elif raiz.dato.num_edificio>dato:
            if raiz.left!=None:
                return self.find(dato, raiz.left)
        elif raiz.dato.num_edificio<dato:
            if raiz.right!=None:
                return self.find(dato, raiz.right)


