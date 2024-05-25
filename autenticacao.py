import json

def autenticar_usuario(email, senha):
    with open("usuarios.json", "r") as file:
        for line in file:
            usuario = json.loads(line)
            if usuario["email"] == email and usuario["senha"] == senha:
                return usuario
    return None
