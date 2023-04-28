class Arbol():
    def __init__(self,orden):
        self.raiz = None
        self.orden = orden

    def insertar_vuelo(self,vuelo):
        if self.raiz == None:
            self.raiz = Nodo(self.orden, self.orden[0])
        nodo:Nodo = self.raiz
        # mira si está la caracteristica del vuelo en el diccionario del vuelo  |  ver si vuelo.origen in nodo.dictç
        posicion = 0
        for caracteristica in self.orden:
            atributo = getattr(vuelo, caracteristica)   # Atributo del vuelo
            if atributo not in nodo.diccionario:
                print(f"EL atributo {atributo} no está en el diccionario {nodo.diccionario} de {nodo}")
                if posicion+1>=len(self.orden):
                    nuevo_nodo = Nodo(self.orden, None, {}, [])
                else:
                    nuevo_nodo = Nodo(self.orden, self.orden[posicion+1], {}, [])
                nodo.diccionario[atributo] = nuevo_nodo
                print(f"DESPUES -> {nodo.diccionario}")
            
            nodo = nodo.diccionario[atributo]

            posicion = posicion + 1
        
        nodo.vuelos.append(vuelo)
        if len(nodo.vuelos) == 1:
            print(nodo, nodo.vuelos)
        return nodo
        # si no está, la añade al diccionario con un nodo

        # si está, cambia al nodo del diccionario y repite el proceso

class Nodo():
    def __init__(self, orden, caracteristica = None, diccionario={}, vuelos = []):
        self.orden = orden
        self.caracteristica = caracteristica   # ["origen", "destino", "compania", "cuarto"]
        self.diccionario = diccionario
        self.vuelos = vuelos

    def __repr__(self) -> str:
        return f"{self.caracteristica}"
