instruction_path = "./data/instructions.txt"

def obtener_instruccion( receta_buscada ):
    with open( instruction_path, "r" , encoding="utf-8") as file:
        for line in file:
            nombre_receta, instruccion = line.split( ";" )

            if nombre_receta == receta_buscada:
                return instruccion

    return None