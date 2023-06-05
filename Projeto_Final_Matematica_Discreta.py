import math
import os
from itertools import permutations


def limparTela():
    os.system("cls")

def printMenu():
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    print('                MENU                  ')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    print('OPÇÕES: ')
    print('[1] - Princípio da Regra da Soma')
    print('[2] - Princípio da Regra do Produto')
    print('[3] - Permutação')
    print('[4] - Permutação Utilizando as Letras de uma Palavra')
    print('[5] - Amostragem com Reposição')
    print('[6] - Amostragem sem Reposição')
    print('[7] - Combinações')
    print('[0] - SAIR')

def opcao01():
    print('\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    print('     Princípio da Regra da Soma       ')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')

    itensConjunto = []
    indices = []

    qntConjuntos = int(input('\nQuantidade de Conjuntos: '))

    for i in range(qntConjuntos):
        qnt = int(input('\nQuantidade de entradas do conjunto %d: ' % (i+1)))
        indices.append(qnt)
        for j in range(qnt):
            entrada = input('Insira o elemento %d do conjunto %d: ' % ((j+1),(i+1)))
            itensConjunto.append(entrada)

    print('\nPrincípio da Regra da Soma:')
    print('Quantidade de Combinações: %d' % sum(indices))
    print('Combinações: ')
    print(itensConjunto)

def printarPermutacoes(lista, qntPermutacao):

    perm = permutations(lista, qntPermutacao)

    for i in list(perm):
        print(i) 

def quantidadePermutacoes(qntItens, qntPermutacao):
    return (math.factorial(qntItens) / math.factorial(qntItens - qntPermutacao))

def opcao03():

    print('\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    print('                   Permutação                   ')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n')

    qntItens = int(input('Quantidade de itens da lista gostaria de inserir: '))
    lista = []

    for i in range(qntItens):
        item = input('Insira o item %d: ' %i)
        lista.append(item)

    qntPermutacao = int(input('\nQuantidade de permutacões desejadas por vez: '))

    print('\nPermutação:')
    print('Quantidade de Combinações: %d ' %quantidadePermutacoes(qntItens, qntPermutacao) )
    print('Combinações: ')
    printarPermutacoes(lista, qntPermutacao)

def opcao04():

    print('\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    print('Permutação Utilizando as Letras de uma Palavra')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n')

    palavra = input('Digite a palavra a ser permutada: ')

    print('\nPermutação Utilizando as Letras de uma Palavra:')
    print('Quantidade de Combinações: %d' % math.factorial(len(palavra)))
    print('Combinações: ')
    permutaPalavra(palavra)


def permutaPalavra(palavra, palavra1 = ''):
    if len(palavra) == 0:
        print(palavra1)
    else:
        for i in range(len(palavra)):
            permutaPalavra(palavra[:i]+palavra[(i+1):],palavra1+palavra[i])

    
def main():
    while True:
        
        printMenu()
        opcao = int(input('Digite sua Opção: '))

        if (opcao == 1):
            opcao01()
        elif (opcao == 2):
            pass
        elif (opcao == 3):
            opcao03()
        elif (opcao == 4):
            opcao04()
        elif (opcao == 5):
            pass
        elif (opcao == 6):
            pass
        elif (opcao == 7):
            pass
        elif (opcao == 0):
            break
        else:
            print('Opção Inválida!')
            main()

main()