class Node(object):
    def __init__(self, tupla, pai=None, op=None):
        '''
        Construtor da Classe Node
        :arg tupla: tupla que contem (Numero de Missionarios, Numero de Canibais, Margem)
        :arg pai: Nó pai
        :arg op:  tupla que contem operação realizada no barco: (Numero de Missionarios, Numero de Canibais)
        '''
        self.tupla = tupla
        self.filhos = []
        self.pai = pai
        self.op = op

    def add(self, filho):
        '''
        Função adiona um novo filho na lista de filhos do nó
        :arg filho: novo Node gerado
        '''
        self.filhos.append(filho)

    def imprime(self):
        '''
        Função que imprime todas operações realizadas
        :arg caminho: lista que contem os passos ate o objetivo (do folha ate o pai)
        '''
        if self.pai is not None:  # pai é nulo?
            self.pai.imprime() # recursão
        if self.op is not None:  # operação é nula?
            print(self.op)  # imprime operação
