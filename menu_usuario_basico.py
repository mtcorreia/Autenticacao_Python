import getpass
from atualizacao_senha import atualizar_senha_json

def menu_usuario_basico(usuario):
    print(f"Seja bem-vindo, {usuario['nome']}!")

    while True:
        print("\n===== MENU - Usuário Básico =====")
        print("1 - MINHA CONTA")
        print("2 - REDEFINIR SENHA")
        print("3 - LOGOUT")
  
        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            print("\n=== MINHA CONTA ===")
            print("NOME:", usuario["nome"])
            print("EMAIL:", usuario["email"])
            print("CATEGORIA: Usuário Básico")
        elif escolha == "2":
            nova_senha = input("NOVA SENHA: ")
            confirmar_nova_senha = getpass("CONFIRMAR NOVA SENHA: ")
            if nova_senha == confirmar_nova_senha:
                atualizar_senha_json(usuario["email"], nova_senha)
            else:
                print("ERRO: As senhas não coincidem. Tente novamente.")
        elif escolha == "3":
            print("Logout realizado.")
            break
        else:
            print("ERRO: Opção inválida. Tente novamente.")
