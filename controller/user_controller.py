users_path = "./data/users.txt"

def iniciar_sesion(usuario, contrasena): #-> bool(Funcionando)
    print(usuario, contrasena)
    with open(users_path, "r") as users:
        for user in users:
            exi_user, password = user.strip().split(",")
            if exi_user == usuario and password == contrasena:
                return True
    return False 


def crear_cuenta(user, password):
    with open(users_path, "a+") as users:
        users.seek(0)  # Mover el puntero al inicio del archivo
        lines = users.readlines()

        # Verificar si el usuario ya existe
        for existing_user in lines:
            existing_user = existing_user.strip().split(",")
            existing_user = existing_user[0]
            if existing_user == user:
                print("El usuario ya existe")
                return False
        users.write(f"{user},{password}"+"\n")
        print("Usuario registrado exitosamente")
        return True