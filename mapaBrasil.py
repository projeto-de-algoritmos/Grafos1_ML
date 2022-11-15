from collections import defaultdict


class Grafo(object):
    """ Implementação básica de um grafo. """

    def __init__(self, arestas, direcionado=False):
        """Inicializa as estruturas base do grafo."""
        self.adj = defaultdict(set)
        self.direcionado = direcionado
        self.adiciona_arestas(arestas)


    def get_vertices(self):
        """ Retorna a lista de vértices do grafo. """
        return list(self.adj.keys())


    def get_arestas(self):
        """ Retorna a lista de arestas do grafo. """
        return [(k, v) for k in self.adj.keys() for v in self.adj[k]]


    def adiciona_arestas(self, arestas):
        """ Adiciona arestas ao grafo. """
        for u, v in arestas:
            self.adiciona_arco(u, v)


    def adiciona_arco(self, u, v):
        """ Adiciona uma ligação (arco) entre os nodos 'u' e 'v'. """
        self.adj[u].add(v)
        # Se o grafo é não-direcionado, precisamos adicionar arcos nos dois sentidos.
        if not self.direcionado:
            self.adj[v].add(u)


    def existe_aresta(self, u, v):
        """ Existe uma aresta entre os vértices 'u' e 'v'? """
        return u in self.adj and v in self.adj[u]


    def __len__(self):
        return len(self.adj)


    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.adj))


    def __getitem__(self, v):
        return self.adj[v]

if __name__== "__main__":
    # Cria a lista de arestas.
    arestas = [('Acre', 'Amazonas'), ('Amazonas', 'Rondonia'), ('Amazonas', 'Roraima'), ('Amazonas', 'Mato Grosso'), ('Amazonas', 'Pará'),
               ('Roraima', 'Pará'), ('Amapá', 'Pará'), ('Rondonia', 'Mato Grosso'), ('Mato Grosso', 'Pará'),('Mato Grosso', 'Tocantins'),
               ('Mato Grosso', 'Goiás'),('Mato Grosso', 'Mato Grosso do Sul'),('Pará', 'Tocantins'), ('Pará', 'Maranhão'), ('Maranhão','Piauí'),
               ('Maranhão','Tocantins'),('Maranhão','Piauí'), ('Tocantins','Bahia'),('Tocantins','Goiás'),('Maranhão','Piauí'), ('Ceará','Piauí'),
               ('Ceará','Paraíba'), ('Ceará','Pernambuco'), ('Ceará','Rio Grande do Norte'), ('Rio Grande do Norte','Paraíba'), ('Paraíba','Pernambuco'),
               ('Pernambuco','Alagoas'), ('Alagoas','Sergipe'), ('Sergipe','Bahia'), ('Pernambuco','Bahia'), ('Pernambuco','Alagoas'), ('Bahia','Alagoas'),
               ('Bahia','Goiás'),('Bahia','Espirito Santo'), ('Goiás','Minas Gerais'), ('Goiás','Mato Grosso do Sul'), ('Bahia','Minas Gerais'),
               ('Espirito Santo','Minas Gerais'),('Rio de Janeiro Santo','Minas Gerais'), ('Espirito Santo','Rio de Janeiro'), ('Minas Gerais','Mato Grosso do Sul'),
               ('São Paulo','Mato Grosso do Sul'), ('Paraná','Mato Grosso do Sul'), ('São Paulo','Rio de Janeiro'), ('São Paulo','Paraná'), ('Santa Catarina','Paraná'),
               ('Santa Catarina', 'Rio Grande do Sul'), ]

    # Cria e imprime o grafo.
    grafo = Grafo(arestas, direcionado=False)
    print(grafo.adj)
