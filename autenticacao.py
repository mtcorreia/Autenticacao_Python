import json
import hashlib

def autenticar_usuario(email, senha):
    # Gerar o hash da senha fornecida
    hash_senha = hashlib.sha256(senha.encode()).hexdigest()

    with open("usuarios.json", "r") as file:
        for line in file:
            usuario = json.loads(line)
            if usuario["email"] == email and usuario["senha"] == hash_senha:
                return usuario
    return None

def verificar_hash_senha(hash_armazenado, senha_fornecida):
    hash_senha_fornecida = hashlib.sha256(senha_fornecida.encode()).hexdigest()
    return hash_armazenado == hash_senha_fornecida
