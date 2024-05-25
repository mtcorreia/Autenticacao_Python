import getpass
from registro_usuario import registrar_usuario
from autenticacao import autenticar_usuario
from menu_usuario_basico import menu_usuario_basico
from menu_usuario_avancado import menu_usuario_avancado

def main():
    print("\nBem-vindo ao Sistema de Registro e Autenticação de Usuários!")

    while True:
        print("\n========== MENU ==========\n")
        print("1 - REGISTRO")
        print("2 - LOGIN")
        print("3 - SAIR")
        print("\n==========================")
        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            registrar_usuario()
        elif escolha == "2":
            email = input("\nEMAIL: ")
            senha = getpass.getpass("SENHA: ")
            usuario = autenticar_usuario(email, senha)
            if usuario:
                if usuario["categoria"] == 1:
                    menu_usuario_basico(usuario)
                elif usuario["categoria"] == 2:
                    menu_usuario_avancado(usuario)
            else:
                print("ERRO: Email ou senha incorretos.")
        elif escolha == "3":
            print("\nSaindo do sistema.\nObrigado por usar nosso programa!!")
            break
        else:
            print("ERRO: Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
