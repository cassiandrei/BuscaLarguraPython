"""
    Trabalho 1 de buscas. Inteligência Artifical - UFSM
    Aluno Cassiano Andrei Schneider
    Busca em Largura no problema dos missioarios e Canibais

    Pacotes necessários: Python versão 3

    Para executar digite:
        $python3 <Numero de Missioarios> <Numero de Canibais> <Numero maximo de Pessoas no barco>
"""

import node
import sys


def main():
    '''
        Função Principal
        :param sys.argv: argumentos passados ao executar o programa
        :param numM: Numero total de Missionarios
        :param numC: Numero total de Canibais
        :param barco: tupla que contem: (numero de missionarios, numero canibais) para transportar de uma margem pra outra
        :param inicio:  tupla que contem estado inicial: (numM, numC, 'MargemEsq')
        :param fim: tupla que contem estado objetivo: (numM, numC, 'MargemDir')
        :param visitados: lista de estados visitados (tuplas)
        :param fila: fila de nós abertos
        :param raiz: nó inicial (inicio)
        :param atual: nó visitado por ultimo
        :param filho: tupla de tupla  que contem ((Novo estado gerado), (operação))
            Novo estado gerado é atribuido à filho de atual: (Numero de missionarios, Numero de Canibais, Margem)
            operação: (Numero de missionarios, numero de Canibais)
        :param filhos: lista de filhos de atual
        :param mold: Numero de missionarios que ficou na margem depois que o barco retirou
        :param cold: Numero de Canibais que ficou na margem depois que o barco retirou
        :param mnew: Numero de missionarios que a marge ficou depois que o barco desembarcou
        :param cnew: Numero de canibais que a marge ficou depois que o barco desembarcou
    '''
    if len(sys.argv) != 4:  # testa se argumentos de entrada é diferente de 4
        print("Entrada errada")
        exit(1)
    # Atribui os argumentos de entrada
    numM = int(sys.argv[1])
    numC = int(sys.argv[2])
    barco = int(sys.argv[3])

    inicio = (numM, numC, 'MargemEsq')  # estado inicial
    fim = (numM, numC, 'MargemDir')  # estado objetivo
    visitados = []
    fila = []

    raiz = node.Node(inicio)
    fila.append(raiz)

    # loop
    while True:
        if len(fila) == 0:  # fila de nos abertos está vazia?
            print("Sem solução")
            break

        atual = fila.pop(0)  # atual é o estado retirado da fila de nós abertos
        filhos = []  # cria lista filhos do nó aberto
        visitados.append(atual.tupla)  # seta o nó aberto como visitado
        print('Estado atual: ', atual.tupla)  # imprime o estado que foi visitado

        if atual.tupla == fim:  # estado é o objetivo?
            #  imprime estado e sai do loop
            print("Solução: ")
            atual.imprime()
            break

        # laço que vai gerar todas operações válida
        for i in range(barco + 1):
            for j in range(barco + 1):
                if barco >= i + j > 0:  # <i,j> OPERADOR: esse operador é válido?
                    mold = atual.tupla[0] - i  # sobrou na margem mold missionarios
                    cold = atual.tupla[1] - j  # sobrou na margem cold canibais

                    mnew = numM - atual.tupla[0] + i  # barco levou i missionarios e ficou com mnew na margem
                    cnew = numC - atual.tupla[1] + j  # barco levou j canibais e ficou com cnew na margem

                    if (mold >= cold or mold == 0) and (cold >= 0 and mold >= 0) and (mnew >= cnew or mnew == 0) and (
                                    cnew >= 0 and mnew >= 0):  # as margens ficaram válidas?
                        if atual.tupla[2] == 'MargemEsq':  # está na margem esquerda
                            filho = ((numM - atual.tupla[0] + i, numC - atual.tupla[1] + j, 'MargemDir'),
                                     (i, j))  # gera novo estado
                        else:  # está na margem direita
                            filho = ((numM - atual.tupla[0] + i, numC - atual.tupla[1] + j, 'MargemEsq'),
                                     (i, j))  # gera novo estado
                        filhos.append(filho)  # estado gerado inserido na lista de filhos

                        if filho[0] not in visitados:  # estado gerado já é um estado visitado?
                            atual.add(
                                node.Node(filho[0], atual, (i, j)))  # adiciona estado gerado como nó filho de atual
                            fila.append(atual.filhos[-1])  # adionado o estado gerado na fila de nós abertos
        print("Estados novos gerados: ", filhos)  # printa todos filhos gerado do atual



main()  # chama função principal
