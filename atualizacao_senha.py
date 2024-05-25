import json

def atualizar_senha_json(email, nova_senha):
    with open("usuarios.json", "r+") as file:
        usuarios = []
        for line in file:
            usuario = json.loads(line)
            if usuario["email"] == email:
                usuario["senha"] = nova_senha
            usuarios.append(usuario)
        
        file.seek(0)
        file.truncate()
        for usuario in usuarios:
            json.dump(usuario, file)
            file.write("\n")
    print("Senha atualizada com sucesso.")
