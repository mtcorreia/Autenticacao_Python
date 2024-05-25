import getpass
import json
from atualizacao_senha import atualizar_senha_json

def menu_usuario_avancado(usuario):
    print(f"\nSeja bem-vindo, {usuario['nome']}!\n")

    while True:
        print("\n===== MENU - Usuário Avançado =====")
        print("1 - LISTAGEM DE USUÁRIOS")
        print("2 - MINHA CONTA")
        print("3 - REDEFINIR SENHA")
        print("4 - LOGOUT")

        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            print("\n=== LISTAGEM DE USUÁRIOS ===")
            with open("usuarios.json", "r") as file:
                for line in file:
                    usuario_cadastrado = json.loads(line)
                    print("\nNOME:", usuario_cadastrado["nome"])
                    print("EMAIL:", usuario_cadastrado["email"])
                    print("CATEGORIA:", "Usuário Básico" if usuario_cadastrado["categoria"] == 1 else "Usuário Avançado")

        elif escolha == "2":
            print("\n=== MINHA CONTA ===")
            print("NOME:", usuario["nome"])
            print("EMAIL:", usuario["email"])
            print("CATEGORIA: Usuário Avançado")

        elif escolha == "3":
            nova_senha = input("NOVA SENHA: ")
            confirmar_nova_senha = getpass("CONFIRMAR NOVA SENHA: ")
            if nova_senha == confirmar_nova_senha:
                atualizar_senha_json(usuario["email"], nova_senha)
            else:
                print("ERRO: As senhas não coincidem. Tente novamente.")
        elif escolha == "4":
            print("Logout realizado.")
            break
        else:
            print("ERRO: Opção inválida. Tente novamente.")
