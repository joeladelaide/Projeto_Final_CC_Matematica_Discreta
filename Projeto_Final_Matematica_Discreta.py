import os

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

    
def main():
    while True:
        
        printMenu()
        opcao = int(input('Digite sua Opção: '))

        if (opcao == 1):
            opcao01()
        elif (opcao == 2):
            pass
        elif (opcao == 3):
            pass
        elif (opcao == 4):
            pass
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