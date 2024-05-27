import getpass
import json
from atualizacao_senha import atualizar_senha_json
from autenticacao import verificar_hash_senha

def menu_usuario_avancado(usuario):
    print(f"\nSeja bem-vindo, {usuario['nome']}!\n")

    while True:
        print("\n===== MENU - Usuário Avançado =====")
        print("1 - LISTAGEM DE USUÁRIOS")
        print("2 - MINHA CONTA")
        print("3 - REDEFINIR SENHA")
        print("4 - VERIFICAR HASH DE SENHA")
        print("5 - LOGOUT")

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
            nova_senha = getpass.getpass("NOVA SENHA: ")
            confirmar_nova_senha = getpass.getpass("CONFIRMAR NOVA SENHA: ")
            if nova_senha == confirmar_nova_senha:
                atualizar_senha_json(usuario["email"], nova_senha)
            else:
                print("ERRO: As senhas não coincidem. Tente novamente.")

        elif escolha == "4":
            hash_armazenado = input("\nHASH ARMAZENADO: ")
            senha_fornecida = getpass.getpass("SENHA FORNECIDA: ")
            if verificar_hash_senha(hash_armazenado, senha_fornecida):
                print("\nA senha corresponde ao hash fornecido.")
            else:
                print("\nA senha não corresponde ao hash fornecido.")

        elif escolha == "5":
            print("Logout realizado.")
            break

        else:
            print("ERRO: Opção inválida. Tente novamente.")
