import node
import sys


def main():
    '''
        Função Principal
        :param sys.argv: argumentos passados ao executar o programa
        :param numM:
        :param numC:
        :param barco:
        :param inicio:
        :param fim:
        :param visitados:
        :param fila:
        :param raiz:
        :param atual:
        :param filho:
        :param filhos:
        :param mold:
        :param cold:
        :param mnew:
        :param cnew:
    '''
    if len(sys.argv) != 4:
        print("Entrada errada")
        exit(1)
    numM = int(sys.argv[1])
    numC = int(sys.argv[2])
    barco = int(sys.argv[3])

    inicio = (numM, numC, 'MargemEsq')
    fim = (numM, numC, 'MargemDir')
    visitados = []

    fila = []

    raiz = node.Node(inicio)
    fila.append(raiz)

    while True:
        atual = fila.pop(0)
        filhos = []
        visitados.append(atual.tupla)
        print('Estado atual: ', atual.tupla)
        if atual.tupla == fim:
            imprime(atual)
            break
        for i in range(barco+1):
            for j in range(barco+1):
                if barco >= i + j > 0:  # <i,j> OPERADOR
                    mold = atual.tupla[0] - i  # sobrou na margem mold mercenarios
                    cold = atual.tupla[1] - j  # sobrou na margem cold canibais

                    mnew = numM - atual.tupla[0] + i  # barco levou i mercenarios e ficou com mnew na margem
                    cnew = numC - atual.tupla[1] + j  # barco levou j canibais e ficou com cnew na margem

                    if (mold >= cold or mold == 0) and (cold >= 0 and mold >= 0) and (mnew >= cnew or mnew == 0) and (
                            cnew >= 0 and mnew >= 0):
                        if atual.tupla[2] == 'MargemEsq':  # está na margem esquerda
                            filho = ((numM - atual.tupla[0] + i, numC - atual.tupla[1] + j, 'MargemDir'), (i, j))
                        else:  # está na margem direita
                            filho = ((numM - atual.tupla[0] + i, numC - atual.tupla[1] + j, 'MargemEsq'), (i, j))
                        filhos.append(filho)

                        if filho[0] not in visitados:
                            atual.add(node.Node(filho[0], atual, (i, j)))
                            fila.append(atual.filhos[-1])
        print("Estados novos gerados: ", filhos)


main()