ingredients_path = "./data/ingredients.txt"

# -> retorna los ingredientes en una lista
def obtener_ingredientes():
    ingredientes = []
    with open(ingredients_path, "r") as file:
        for line in file:
            ingredientes.append(line.strip())
    return sorted( ingredientes )

ingredientes = obtener_ingredientes()