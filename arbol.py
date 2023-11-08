class Arbol:
    def __init__(self, elemento):
        self.root = root

class Nodo:
    left = right = None
    def __init__(self, value):
        self.value = value



def buscarSubArbol(root, elemento) => {

    if root is None:
        root = new Nodo(elemento)

    if(elemento< root.value) {
          
        buscarSubArbol(root.left, elemento  )
    }

    else:
        root.right = buscarSubArbol(root.right, elemento    )
    
    return root

}