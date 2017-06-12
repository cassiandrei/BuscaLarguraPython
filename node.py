class Node(object):
    def __init__(self, tupla, pai=None, op=None):
        self.tupla = tupla
        self.filhos = []
        self.pai = pai
        self.op = op

    def add(self, filho):
        self.filhos.append(filho)
