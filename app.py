import os

restaurantes = []

def exibir_nome_do_programa():
    print ("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░ 
       """)

def exibir_opcoes():

    print ('1. Cadastrar Restaurante')
    print ('2. Listar Restaurante')
    print ('3. Ativar Restaurante')
    print ('4. Sair\n')

def finalizar_app():
    os.system('cls')  
   # os.system('clear')  para mac
    print('Finalizando o App\n')

def opcao_invalida():
    print('Opção Invalida!\n')
    input('Pressione qualquer tecla para continuar...')
    main()
    
def cadastrar_novo_restaurante():
        os.system('cls')
        print('Cadastrando novo Restaurante\n')
        nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')    
        restaurantes.append(nome_do_restaurante)
        print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
        input('digite qualquer tecla para continuar...')
        main()    
        
    
def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Ecolha uma opção: '))

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
            nome_do_restaurante = input('Nome do Restaurante: ')
            print(f'Nome do Restaurante {nome_do_restaurante} Cadastrado com sucesso!')
        elif opcao_escolhida == 2:
            print('Listar Restaurantes')
        elif opcao_escolhida == 3:
            print('Ativar Restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()  
              
def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()