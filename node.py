class Node(object):
    def __init__(self, tupla, pai=None, op=None):
        '''
        Construtor da Classe Node
        :param tupla: tupla que contem (Numero de Missionarios, Numero de Canibais, Margem)
        :param pai: Nó pai
        :param op:  tupla que contem operação realizada no barco: (Numero de Missionarios, Numero de Canibais)
        '''
        self.tupla = tupla
        self.filhos = []
        self.pai = pai
        self.op = op

    def add(self, filho):
        '''
        Função adiona um novo filho na lista de filhos do nó
        :param filho: novo Node gerado 
        '''
        self.filhos.append(filho)

    def imprime(self, folha):
        '''
        Função que imprime todas operações realizadas
        :param folha: ultimo nó criado que é o objetivo
        '''
        print(folha.op)
        if folha.pai is not None:
            self.imprime(folha.pai)
