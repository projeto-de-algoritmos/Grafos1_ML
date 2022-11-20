class Grafo(object):
    """ Implementação básica de um grafo. """

    adjacencias = {
        "AC": ["AM", "RO"],
        "AM": ["RO", "MT", "PA", "RR", "AC"],
        "RO": ["AM", "MT", "AC"],
        "RR": ["AM", "PA"],
        "PA": ["TO", "MT", "AP", "AM", "MA", "RR"],
        "AP": ["PA"],
        "TO": ["PI", "MT", "BA", "GO", "PA", "MA"],
        "MA": ["TO", "PA", "PI"],
        "PI": ["TO", "PE", "BA", "MA", "CE"],
        "BA": ["PI", "TO", "PE", "MG", "GO", "ES", "SE", "AL"],
        "CE": ["PE", "PI", "PB", "RN"],
        "RN": ["CE", "PB"],
        "PB": ["CE", "RN", "PE"],
        "PE": ["PI", "BA", "PB", "AL", "CE"],
        "AL": ["PE", "BA", "SE"],
        "SE": ["AL", "BA"],
        "MT": ["TO", "RO", "GO", "PA", "AM", "MS"],
        "GO": ["TO", "MG", "MT", "BA", "DF", "MS"],
        "MS": ["SP", "PR", "MG", "MT", "GO"],
        "DF": ["MG", "GO"],
        "MG": ["SP", "RJ", "BA", "GO", "ES", "DF", "MS"],
        "ES": ["MG", "RJ", "BA"],
        "SP": ["MG", "RJ", "PR", "MS"],
        "RJ": ["SP", "MG", "ES"],
        "PR": ["SP", "SC", "MS"],
        "SC": ["RS", "PR"],
        "RS": ["SC"],
    }

    estados = {
        'AC': 'Acre', 'AL': 'Alagoas', 'AM': 'Amazonas', 'AP': 'Amapá',
        'BA': 'Bahia', 'CE': 'Ceará', 'DF': 'Distrito Federal', 'ES': 'Espírito Santo',
        'GO': 'Goiás', 'MA': 'Maranhão', 'MG': 'Minas Gerais', 'MS': 'Mato Grosso do Sul',
        'MT': 'Mato Grosso', 'PA': 'Pará', 'PB': 'Paraíba', 'PE': 'Pernambuco', 'PI': 'Piauí',
        'PR': 'Paraná', 'RJ': 'Rio de Janeiro', 'RN': 'Rio Grande do Norte', 'RO': 'Rondônia',
        'RR': 'Roraima', 'RS': 'Rio Grande do Sul', 'SC': 'Santa Catarina', 'SE': 'Sergipe',
        'SP': 'São Paulo', 'TO': 'Tocantins'
    }

    def __init__(self):
        """Inicializa as estruturas base do grafo."""
        self.lista_adj = self.adjacencias

    def get_vertices(self):
        """ Retorna a lista dos nós do grafo. """
        return list(self.lista_adj.keys())

    def get_arestas(self):
        """ Retorna a lista de arestas do grafo. """
        return [(k, v) for k in self.lista_adj.keys() for v in self.lista_adj[k]]

    def existe_aresta(self, u, v):
        """ Verifica se existe uma aresta entre os vértices 'u' e 'v' """
        return u.upper() in self.lista_adj and v.upper() in self.lista_adj[u]

    def total_de_nos(self):
        """ Retorna o número total de nós no grafo."""
        return len(self.lista_adj)

    def __len__(self):
        return len(self.lista_adj)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.lista_adj))

    def __getitem__(self, v):
        """ Retorna a lista de vizinhos de um nó.

        :param v: o nó que se deseja saber os vizinhos
        """
        return self.lista_adj[v.upper()]


if __name__ == "__main__":
    # Cria e imprime o grafo.
    grafo = Grafo()
    print(grafo.lista_adj)
