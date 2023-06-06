import itertools
import math
import os
import random
from itertools import permutations
from time import sleep

import numpy as np


def limparTela():
    os.system("cls")

def printInicial():
    print("\t\t\tCENTRO UNIVERSITÁRIO DE JOÃO PESSOA - UNIPÊ\n");
    sleep(2)
    print("\t\t\tCIÊNCIAS DA COMPUTAÇÃO\n")
    sleep(2)
    print("\t\t\tPROJETO FINAL - MATEMÁTICA DISCRETA\n")
    sleep(2)
    print("\t\t\tEQUIPE:\n")
    sleep(2)
    print("\t\t\tJoel Adelaide Medeiros - RGM: 29799384\n")
    sleep(2)
    print("\t\t\tMarcos Barbosa Vieira Filho - RGM: 30174503\n")
    sleep(2)
    limparTela()


def printMenu():
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    print('                MENU                  ')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n')
    print('               OPÇÕES:                  ')
    print('[1] - Princípio da Regra da Soma')
    print('[2] - Princípio da Regra do Produto')
    print('[3] - Permutação')
    print('[4] - Permutação Utilizando as Letras de uma Palavra')
    print('[5] - Amostragem com Reposição')
    print('[6] - Amostragem sem Reposição')
    print('[7] - Combinações')
    print('[0] - SAIR\n')

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

    input()

def printarPermutacoes(lista, qntPermutacao):

    perm = permutations(lista, qntPermutacao)

    for i in list(perm):
        print(i) 

def quantidadePermutacoes(qntItens, qntPermutacao):
    return (math.factorial(qntItens) / math.factorial(qntItens - qntPermutacao))


def printarPrincipioProduto(qntConjuntos, itensConjunto, indices):

    if(qntConjuntos == 1):
        print(itensConjunto)

    elif(qntConjuntos == 2):

        a = indices[0]
        b = indices[1]

        for i in range(a):
            for j in range(b):
                print(itensConjunto[i] + itensConjunto[j+a] )
    
    elif(qntConjuntos == 3):

        a = indices[0]
        b = indices[1]
        c = indices[2]

        for i in range(a):
            for j in range(b):
                for k in range(c):
                    print(itensConjunto[i] + itensConjunto[j+a] +  itensConjunto[k+a+b])

    elif(qntConjuntos == 4):

        a = indices[0]
        b = indices[1]
        c = indices[2]
        d = indices[3]

        for i in range(a):
            for j in range(b):
                for k in range(c):
                    for l in range(d):
                        print(itensConjunto[i] + itensConjunto[j+a] +  itensConjunto[k+a+b] + itensConjunto[j+a+b+c] )
    
    elif(qntConjuntos == 5):

        a = indices[0]
        b = indices[1]
        c = indices[2]
        d = indices[3]
        e = indices[4]

        for i in range(a):
            for j in range(b):
                for k in range(c):
                    for l in range(d):
                        for m in range(e):
                            print(itensConjunto[i] + itensConjunto[j+a] +  itensConjunto[k+a+b] + itensConjunto[l+a+b+c] +  itensConjunto[m+a+b+c+d])


def multiplicacaoLista(indices):

    multiplicacao = 1
    for i in indices:
        multiplicacao = multiplicacao * i
    
    return multiplicacao


def opcao02():
    print('\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    print('     Princípio da Regra da Produto      ')
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

    print('\nPrincípio da Regra do Produto:')
    print('Quantidade de Combinações: %d' % multiplicacaoLista(indices))
    print('Combinações: ')
    printarPrincipioProduto(qntConjuntos, itensConjunto, indices)
    input()

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
    input()

def opcao04():

    print('\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    print('Permutação Utilizando as Letras de uma Palavra')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n')

    palavra = input('Digite a palavra a ser permutada: ')

    print('\nPermutação Utilizando as Letras de uma Palavra:')
    print('Quantidade de Combinações: %d' % math.factorial(len(palavra)))
    print('Combinações: ')
    permutaPalavra(palavra)
    input()


def permutaPalavra(palavra, palavra1 = ''):
    if len(palavra) == 0:
        print(palavra1)
    else:
        for i in range(len(palavra)):
            permutaPalavra(palavra[:i]+palavra[(i+1):],palavra1+palavra[i])

def opcao05():

    print('\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    print('            Amostragem com reposição            ')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n')

    quantidade_amostras = int(input("Digite a quantidade de amostras desejadas: "))

    populacao = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for i in range(quantidade_amostras):
        amostra = random.choices(populacao, k=len(populacao))
        print("Amostra", i+1, "com reposição:", amostra)
    input()

def opcao06():

    print('\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    print('           Amostragem sem reposição             ')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n')
    quantidade_amostras = int(input("Digite a quantidade de amostras desejadas: "))

    populacao = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for i in range(quantidade_amostras):
        amostra = random.sample(populacao, k=len(populacao))
    print("Amostra numero", i+1, "sem reposição:", amostra[:quantidade_amostras])
    input()

def opcao07():

    print('\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    print('                  Combinações                   ')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n')

    num_opcoes = int(input("Digite o número de opções para as combinações: "))

    populacao = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    combinacoes = list(itertools.combinations(populacao, num_opcoes))

    print("Combinações de", num_opcoes, "opções:")
    for combinacao in combinacoes:   
        print(combinacao)
    input()
   
def main():
    while True:
        limparTela()
        printInicial()
        printMenu()
        opcao = int(input('Digite sua Opção: '))

        if (opcao == 1):
            limparTela()
            opcao01()
        elif (opcao == 2):
            limparTela()
            opcao02()
        elif (opcao == 3):
            limparTela()
            opcao03()
        elif (opcao == 4):
            limparTela()
            opcao04()
        elif (opcao == 5):
            limparTela()
            opcao05()
        elif (opcao == 6):
            limparTela()
            opcao06()
        elif (opcao == 7):
            limparTela()
            opcao07()
        elif (opcao == 0):
            break
        else:
            print('Opção Inválida!')
            main()

main()