import json
from getpass import getpass

def registrar_usuario():
    print("\n=== CADASTRO DE USUÁRIO ===")
    nome = input("NOME: ")
    email = input("EMAIL: ")
    categoria = int(input("CATEGORIA (1 - BÁSICO, 2 - AVANÇADO): "))
    senha = getpass("SENHA: ")
    confirmar_senha = getpass("CONFIRMAR SENHA: ")

    if senha != confirmar_senha:
        print("ERRO: As senhas não coincidem. Tente novamente.")
        return

    novo_usuario = {
        "nome": nome,
        "email": email,
        "categoria": categoria,
        "senha": senha
    }

    with open("usuarios.json", "a") as file:
        json.dump(novo_usuario, file)
        file.write("\n")
    print("\nUsuário registrado com sucesso.")
