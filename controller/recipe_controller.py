ingredients_path = "./data/recipes.txt"

# -> retorna lista de recetas
# receta = [
# 0 -> nombre, 
# 1 -> [ingredientes],
# 2 -> kcal,
# 3 -> carbos,
# 4 -> grasas,
# 5 -> protes ]

def obtener_recetas():
    recetas = []
    with open( ingredients_path, "r" ) as file:
        for line in file:
            receta = line.strip().split(";")
            receta[1] = receta[1].split(",")
            recetas.append( receta )
    return recetas

# -> retorna lista de recetas posibles con los ingredientes
def recetas_posibles( ingredientes ):
    recetas = obtener_recetas()
    posibles = []

    for receta in recetas:
        ingredientes_receta = receta[1]

        # Verifica que todos los ingredientes en la lista ingredientes
        # Existan en la lista de ingredientes de la receta
        es_posible = all( ingrediente in ingredientes for ingrediente in ingredientes_receta )

        if es_posible:
            posibles.append( receta )

    return posibles