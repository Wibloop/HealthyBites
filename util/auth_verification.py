
#Recibe usuario y contraseña
# -> (False, error) si credenciales son inválidas, (True, None) caso contrario


def validate_credentials(usuario, contrasena):
    not_allowed_chars = ['"', "'", ',']

    if usuario == '' or contrasena == '':
        return False, "Debe llenar todos los campos"
    
    for letra in usuario:
        if letra in not_allowed_chars:
            return False, "Nombre de usuario inválido"
    
    for letra in contrasena:
        if letra in not_allowed_chars:
            return False, "Contraseña inválida"
        
    return True, None