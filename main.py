import node
import sys


def main():
    if len(sys.argv) != 3:
        print("Entrada errada")
        exit(1)
    numM = sys.argv[1]  # Numero de Mercenarios
    numC = sys.argv[2]  # Numero de Canibais

    inicio = (numM, numC, 'MargemEsq')
    fim = (numM, numC, 'MargemDir')

    margemEsq =

    fila = []

    raiz = node.Node(inicio)
    fila.append(raiz)

    while True:
        atual = fila.pop()
        print('Estado atual: ', atual.tupla)
        if atual.tupla == fim:
            break
        for i in range(3):
            for j in range(3):
                if i + j <= 2:
                    m = atual.tupla[0] - i
                    c = atual.tupla[1] - j
                    if (m >= c || m == 0) and (c >= 0 and m >= 0):
                        


main()
