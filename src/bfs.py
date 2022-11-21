from queue import Queue
from src.model import Grafo

fila = Queue()


def aplicar_busca(grafo: Grafo, estado_partida, estado_destino):
    """ Implementa o algoritmo BFS no grafo. """

    for nos in grafo.get_vertices():
        grafo.visitado[nos] = False
        grafo.vizinhos[nos] = None

    node = estado_partida
    grafo.visitado[node] = True
    fila.put(node)

    while not fila.empty():
        u = fila.get()

        for v in grafo.lista_adj[u]:
            if not grafo.visitado[v]:
                grafo.visitado[v] = True
                grafo.vizinhos[v] = u
                fila.put(v)

    menor_caminho = caminho(grafo, estado_destino)

    return menor_caminho


def caminho(grafo, estado_destino):
    """ Analisa o caminho que passa por menos estados. """
    v = estado_destino
    path = []
    while v is not None:
        path.append(v)
        v = grafo.vizinhos[v]
    path.reverse()

    return path
