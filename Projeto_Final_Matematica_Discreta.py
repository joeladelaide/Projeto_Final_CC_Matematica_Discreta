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
    print()
    print('[0] - SAIR')


def main():
    while True:
        
        printMenu()
        opcao = int(input('Digite sua Opção: '))

        if (opcao == 1):
            pass
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

limparTela()
main()