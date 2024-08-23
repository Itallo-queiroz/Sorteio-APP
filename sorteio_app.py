import random

nomes = []

while True:
    print('\n\033[36m          menu\n\033[0m')
    print('1 - Inserir nome na lista. ')
    print('2 - Sortear. ')
    print('3 - Sair. ')

    op = input('\n\033[30m Opção desejada: \033[0m')

    match op:
        case '1':
            nome = input('Insira o nome: ')
            nomes.append(nome)
            print(f'\n\033[31m {nome} insirido com sucesso. \n\033[0m ')
            continue
        case '2':
            indice_sorteado = random.randint(0, len(nomes)-1) # O -1 é pra ñ ultrapassar o intem da lista
            print(f'Nome sorteado: {nomes[indice_sorteado]}. ')
            continue
        case '3':
            print('Saindo...')
            break
        case _:
            print('Opção inválida. Tente novamente.')
            continue


