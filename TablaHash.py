def funcion_hash(clave, tamaño_tabla):
    valor_hash  = 0
    for c in clave:
        valor_hash += ord(c) + 1
    return valor_hash % tamaño_tabla


tabla_hash = [None] * 10

archivoEntrada = "input.txt"
archivoSalida = "output.txt"

tamanio_tabla = len(tabla_hash)

# Insertar frutas en tabla hash
for string in open(archivoEntrada, 'r'):
    string = string.strip()
    indice = funcion_hash(string, tamanio_tabla)
    tabla_hash[indice] = string


# Mostrar tabla hash solo una vez
for i, valor in enumerate(tabla_hash):
    if valor is not None:
        print(f"Índice {i}: {valor}")


# Guardar en archivo de salida
with open(archivoSalida, 'w') as f:
    for i, valor in enumerate(tabla_hash):
        if valor is not None:
            f.write(f"Índice {i}: {valor}\n")
