# IMPORT DE BIBLIOTECAS PYTHON
import itertools
import math
import os
import random # Importa o módulo random para realizar a amostragem
from itertools import permutations # Importa o módulo itertools para gerar as combinações
from time import sleep

import numpy as np


#MÉTODOS AUXILIARES
#Método para limpar o terminal 
def limparTela():   
    os.system("cls")

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

def permutaPalavra(palavra, palavra1 = ''):
    if len(palavra) == 0:
        print(palavra1)
    else:
        for i in range(len(palavra)):
            permutaPalavra(palavra[:i]+palavra[(i+1):],palavra1+palavra[i])


#MÉTODOS DE PRINT
#Print inicial contendo informações dos desenvolvedores
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

#Print do menu inicial
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


#FUNÇÕES PRINCIPAIS
#Opção 01 - Princípio da Regra da Soma
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

#Opção 02 - Princípio da Regra da Produto
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

#Opção 03 - Permutação
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

#Opção 04 - Permutação Utilizando as Letras de uma Palavra
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

#Opção 04 - Amostragem com reposição
def opcao05():

    print('\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    print('            Amostragem com reposição            ')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n')

    # Solicitar a quantidade de amostras desejadas
    quantidade_amostras = int(input("Digite a quantidade de amostras desejadas: "))

    # Criar uma lista para armazenar as amostras
    amostras = []

    # Obter a quantidade de elementos em cada amostra
    for i in range(quantidade_amostras):
        quantidade_elementos = int(input("\nDigite a quantidade de elementos para a amostra {}: ".format(i+1)))
        amostra = []

        # Obter cada elemento da amostra
        for j in range(quantidade_elementos):
            elemento = input("Digite o elemento {}: ".format(j+1))
            amostra.append(elemento)

        amostras.append(amostra)

    # Realizar as amostragens com reposição
    for i, amostra in enumerate(amostras):
        amostra_aleatoria = random.choices(amostra, k=len(amostra))
        print("Amostra", i+1, "com reposição:", amostra_aleatoria)
    input()

#Opção 06 - Amostragem sem reposição
def opcao06():

    print('\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    print('           Amostragem sem reposição             ')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n')
    import random

    quantidade_amostras = int(input("Digite a quantidade de amostras desejadas: "))

    amostras = []

    # Obter as amostras desejadas
    for i in range(quantidade_amostras):
        quantidade_elementos = int(input("Digite a quantidade de elementos para a amostra {}: ".format(i+1)))
        amostra = []

    # Obter cada elemento da amostra
    for j in range(quantidade_elementos):
        elemento = input("Digite o elemento {}: ".format(j+1))
        amostra.append(elemento)

    amostras.append(amostra)

    # Realizar a amostragem sem reposição
    for i, amostra in enumerate(amostras):
        amostra_aleatoria = random.sample(amostra, k=len(amostra))
        print("Amostra", i+1, "sem reposição:", amostra_aleatoria)

    input()

#Opção 07 - Combinações
def opcao07():

    print('\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
    print('                  Combinações                   ')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n')

    import itertools

    # Obter o número de combinações e os elementos, cada um armazenado na sua variável
    num_combinacoes = int(input("Digite o número de combinações desejadas: "))

    elementos_input = input("Digite os elementos separados por vírgula: ")
    elementos = [elemento.strip() for elemento in elementos_input.split(",")]

    combinacoes = list(itertools.combinations(elementos, num_combinacoes))
    print(f"\nAs {num_combinacoes} combinações possíveis são:")
     # printar as combinações ultilizando um for
    for combinacao in combinacoes:
        print(combinacao)
    input()


#MAIN()
def main():
    while True:
        limparTela() # Limpa a tela
        printMenu()
        opcao = int(input('Digite sua Opção: '))

        if (opcao == 1):
            limparTela()
            opcao01() # Executa a função correspondente à opção 1, assim como nas proximas escolhas ate 7, sendo 0 a saida da condicional
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
            print("\nSaindo do Código......")
            break
        else:
            print('Opção Inválida!')
            main() # Chama a função main() novamente em caso de opção inválida

#CÓDIGOS INICIALIZADORES
limparTela()
printInicial()
main()