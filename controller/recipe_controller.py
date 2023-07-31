ingredients_path = "./data/recipes.txt"

# -> retorna lista de recetas
# receta = [
# 0 -> nombre, 
# 1 -> [ingredientes],
# 2 -> kcal,
# 3 -> carbos,
# 4 -> grasas,
# 5 -> protes ]


# Función para obtener la lista de recetas a partir del archivo recipes.txt
# Retorna una lista de recetas, donde cada receta es representada
def obtener_recetas():
    recetas = []
    with open(ingredients_path, "r") as file:
        for line in file:
            receta = line.strip().split(";")
            receta[1] = receta[1].split(",")
            recetas.append(receta)
    return recetas


# Función para obtener una lista de recetas posibles basadas en una lista de ingredientes dados
# Recibe como argumento la lista de ingredientes seleccionados
# Retorna una lista con las recetas que contienen todos los ingredientes de la lista proporcionada

def recetas_posibles(ingredientes):
    recetas = obtener_recetas()
    posibles = []

    for receta in recetas:
        ingredientes_receta = receta[1]

        # Verifica que todos los ingredientes en la lista ingredientes
        # Existan en la lista de ingredientes de la receta
        es_posible = all(ingrediente in ingredientes for ingrediente in ingredientes_receta)

        if es_posible:
            posibles.append(receta)

    return posibles