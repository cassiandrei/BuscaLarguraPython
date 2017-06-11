class Node(object):
    def __init__(self, tupla, pai=None):
        self.tupla = tupla
        self.filhos = []
        self.pai = pai
        self.visitado = False

    def visitar(self):
        self.visitado = True

    def add(self, filho):
        self.filhos.append(filho)
