
#Defino nodo provincia
class NodoProvincia:

    def __init__ (self, name):
        # self.value = value
        self.name = name
        self.destinations = [] #Destinos disponibles desde la provincia definida
    
    def myfunc(self) -> str:
        print('Origen: ', self.name)
        print('Destinos: ')
        for prov in self.destinations:
            prov.myfunc()
        # print('\n')




               


class Edge:
    def __init__ (self, provincia , prices):
        self.name = provincia.name
        self.prices = prices

    def myfunc(self) -> str:
        print(self.name, self.prices)

    # def minPrice(self):
    #     min = self.prices[0]
    #     for p in self.prices:
    #         if p 

    




# for day in edge_BA_CBA.prices:
#     print(edge_BA_CBA.prices[day])

# nodo_BA.myfunc()
# nodo_CBA.myfunc()
# nodo_BA.cheapest('Cordob')
