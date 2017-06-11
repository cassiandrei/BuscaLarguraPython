import node
import sys


def main():
    if len(sys.argv) != 3:
        print("Entrada errada")
        exit(1)
    numM = int(sys.argv[1])  # Numero de Mercenarios
    numC = int(sys.argv[2])  # Numero de Canibais

    inicio = (numM, numC, 'MargemEsq')
    fim = (numM, numC, 'MargemDir')

    fila = []

    raiz = node.Node(inicio)
    fila.append(raiz)

    while True:
        atual = fila.pop(0)
        filhos = []
        print('Estado atual: ', atual.tupla)
        if atual.tupla == fim:
            break
        for i in range(3):
            for j in range(3):
                if 2 >= i + j > 0:  # <i,j> OPERADOR
                    mold = atual.tupla[0] - i  # sobrou na margem mold mercenarios
                    cold = atual.tupla[1] - j  # sobrou na margem cold canibais

                    mnew = numM - atual.tupla[0] + i  # barco levou i mercenarios e ficou com mnew na margem
                    cnew = numC - atual.tupla[1] + j  # barco levou j canibais e ficou com cnew na margem

                    if (mold >= cold or mold == 0) and (cold >= 0 and mold >= 0) and (mnew >= cnew or mnew == 0) and (cnew >= 0 and mnew >= 0):
                        if atual.tupla[2] == 'MargemEsq':  # está na margem esquerda
                            filho = ((numM - atual.tupla[0] + i, numC - atual.tupla[1] + j, 'MargemDir'), (i, j))
                        else:                              # está na margem direita
                            filho = ((numM - atual.tupla[0] + i, numC - atual.tupla[1] + j, 'MargemEsq'), (i, j))
                        filhos.append(filho)

                        atual.add(node.Node(filho[0], atual))
                        fila.append(atual.filhos[-1])
        print("Estados novos gerados: ", filhos)

main()
