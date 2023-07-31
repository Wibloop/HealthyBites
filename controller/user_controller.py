# Ruta del archivo que contiene los usuarios y contraseñas
users_path = "./data/users.txt"


# Función para iniciar sesión de un usuario
def iniciar_sesion(usuario, contrasena):
    # Abrimos el archivo de usuarios en modo lectura
    with open(users_path, "r") as users:
        # Recorremos el archivo línea por línea
        for user in users:
            # Dividimos la línea en usuario y contraseña
            exi_user, password = user.strip().split(",")
            
            # Comparamos el usuario y la contraseña con los proporcionados
            if exi_user == usuario and password == contrasena:
                # Si coinciden, retornamos True (sesión iniciada)
                return True
                
    # Si no se encuentra el usuario o la contraseña es incorrecta, retornamos False
    return False 


# Función para crear una nueva cuenta de usuario
def crear_cuenta(user, password):
    # Abrimos el archivo de usuarios en modo lectura y escritura
    with open(users_path, "a+") as users:
        # Movemos el puntero al inicio del archivo para leerlo desde el principio
        users.seek(0)
        # Leemos todas las líneas del archivo
        lines = users.readlines()

        # Verificamos si el usuario ya existe en el archivo
        for existing_user in lines:
            # Dividimos la línea en usuario y contraseña
            existing_user = existing_user.strip().split(",")
            existing_user = existing_user[0]
            
            # Comparamos el usuario con los usuarios existentes
            if existing_user == user:
                print("El usuario ya existe")
                # Si el usuario ya existe, retornamos False (registro fallido)
                return False
        
        # Si el usuario no existe, lo añadimos al archivo junto con su contraseña
        users.write(f"{user},{password}" + "\n")
        print("Usuario registrado exitosamente")
        # Retornamos True para indicar que el registro fue exitoso
        return True