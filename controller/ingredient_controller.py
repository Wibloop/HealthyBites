# Ruta del archivo que contiene la lista de ingredientes
ingredients_path = "./data/ingredients.txt"


# Función para obtener los ingredientes desde el archivo y retornarlos en una lista
def obtener_ingredientes():
    # Lista para almacenar los ingredientes
    ingredientes = []
    
    # Abrimos el archivo de ingredientes en modo lectura
    with open(ingredients_path, "r") as file:
        # Iteramos sobre cada línea del archivo
        for line in file:
            # Añadimos cada línea (ingrediente) a la lista de ingredientes, eliminando espacios en blanco al final
            ingredientes.append(line.strip())
    

    # Ordenamos la lista de ingredientes alfabéticamente
    return sorted(ingredientes)


# Obtenemos la lista de ingredientes llamando a la función
ingredientes = obtener_ingredientes()
