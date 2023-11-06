from tp import *
from prices import *

class Graph:

    def __init__(self):

        self.provincias = []

    def __str__(self):
        for i in self.provincias:
            i.myfunc()
    
    def agregar(grafo, provincia):
        grafo.provincias.append(provincia)
    


nodo_BA = NodoProvincia("Buenos Aires")
nodo_CBA = NodoProvincia("Cordoba")
nodo_BR = NodoProvincia("Bariloche")
nodo_SF = NodoProvincia("Santa Fe")

edge_BA_CBA = Edge(nodo_CBA, BA_CBA_prices)
edge_BA_BR = Edge(nodo_BR, BA_BR_prices)
edge_CBA_BR = Edge(nodo_BR, CBA_BR_prices)

nodo_BA.destinations.append(edge_BA_BR)
nodo_BA.destinations.append(edge_BA_CBA)
nodo_CBA.destinations.append(edge_CBA_BR)

grafo = Graph()

grafo.agregar(nodo_BA)
grafo.agregar(nodo_CBA)
# grafo.__str__()

# For each vertex v:
# 	Dist[v] = infinite
# 	Prev[v] = none
# Dist source = 0
# Set all vertices to unexplored
# While destination not explored:
# V = least valued unexplored vortex
# Set v to explored
# For each edge (v, w):
# 	If dist[v] + len(v, w) < dist[w]:
# 	Dist[w] = dist[v] + len[v, w]
# Prev[w] = v

def caminoMinimo(grafo, origen, destino):
    etiquetas = {origen: (0, None)
                 
                 #{BA: (0, None)
                 # CBA: (1000, BA),
                 # BR: (1500, CBA)
                 # }
                 }

    dijkstra(grafo, origen, destino, fecha, etiquetas, procesados = [])


def dijkstra(grafo, origen, destino, fecha,etiquetas, procesados):

    nodoActual = menorValorNoProcesado(etiquetas, procesados)

    if nodoActual.name == destino:
        return
    procesados.append(nodoActual)

    for destino in  destinosNoprocesados(grafo, nodoActual, procesados):
        generarEtiqueta()


    def generarEtiqueta(grafo, nodo, anterior, etiquetas):
        etiquetaprev = etiquetas[anterior]

        etiquetaNueva =  nodo.destinations.price + acumulado(etiquetaprev)

    def acumulado(etiqueta):
        return etiqueta[0]

    def menorValorNoProcesado(etiquetas, procesados):
        # etiquetadosSinProcesar =    filter( x no en procesados , siendo x  -> eitquetas)
        
         a =    
        return 'min'

    def destinosNoprocesados(grafo, nodoActual, procesados):
        
        #Filtrar
        return ['Bariloche']











#     costo = 0 
#     visited = []
#     temp = origen
#    #Greedy aproach
#     for i in grafo:
#         if temp not in visited:
#             visited.push(temp)
#             min = []
#             for j in grafo[temp].connections:

#     visited = []
#     provincias = grafo.provincias
#     for p in range(len(provincias)):
#         dist = 0
#         prev = None

#         provincia = provincias[p]
#         if provincia.name == origen:
#             min = []
#             for j  in provincia.destinations:
#                 dijkstra(grafo, j.name, destino, fecha)
#                 if j.name == destino:
#                     print(j.prices[fecha])
#                     min.append(j.prices[fecha])

            
#             return min
        


#     dist[w] = 1000
#     prev = None
#     dist = 0
#     for j in provincia.destinations:
    
#      if dist + j.price < dist[w]:
#          dist[w] =  dist + j.price
    
#     prev[w] = provincia.name


# dijkstra(grafo, 'Buenos Aires', 'Bariloche', 'jueves')




