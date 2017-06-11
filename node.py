class Node(object):
    def __init__(self, tupla, pai=None):
        self.tupla = tupla
        self.filhos = []
        self.pai = pai

    def add(self, filho):
        self.filhos.append(filho)
