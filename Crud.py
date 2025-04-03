
CONSTANTE_HASH = 0.6180339887
TAMANIO_FILAS = 2
TAMANIO_COLUMNAS = 5

# calcula el valor hash de la cadena ingresada
#(toma la posicion de cada caractes y lo multiplica por su valor ASCII )

def ascii_hash(valorLlave):
    return sum((i + 1) * ord(ch) for i, ch in enumerate(valorLlave))


#calculo del idice utilizando el metodo multiplicacion
def hash_index(key, table_size):
    return int(table_size * ((key * CONSTANTE_HASH) % 1))

# inserta una fila completa, ya maneja las coliciones
def insert_fila(table, fila):
    key = ascii_hash(fila[0])
    index = hash_index(key, TAMANIO_FILAS)
    for i, item in enumerate(fila):
        table[index][i].append(item)




def get_fila(table, valorLlave):
    # Calculamos la clave y el índice de hash
    key = ascii_hash(valorLlave)
    index = hash_index(key, TAMANIO_FILAS)
    fila3 = []
    for i, sublista in enumerate(table[index][0]):
        if sublista == valorLlave:
            for j, subList2 in enumerate(table[index]):
                fila3.append(subList2[i])
    return fila3

def update_fila(table, nuevaFila ):
    key = ascii_hash(nuevaFila[0])
    index = hash_index(key, TAMANIO_FILAS)
    fila3 = []
    for i, sublista in enumerate(table[index][0]):
        if sublista == nuevaFila[0]:
            for j, subList2 in enumerate(table[index]):
                table[index][j][i] = nuevaFila[j]
    return table

def delete_fila(table, valorLlave):
    key = ascii_hash(valorLlave)
    index = hash_index(key, TAMANIO_FILAS)
    fila3 = []
    for i, sublista in enumerate(table[index][0]):
        if sublista == valorLlave:
            for j, subList2 in enumerate(table[index]):
                del table[index][j][i]
    return table


#Crea una lista que contiene varias listas del valor que especifiquemos
table = [[[] for _ in range(TAMANIO_COLUMNAS)] for _ in range(TAMANIO_FILAS)]

fila = [None for _ in range(TAMANIO_COLUMNAS)]
fila2 = [None for _ in range(TAMANIO_COLUMNAS)]

fila = ['cambio', 'codigo2', 'prueba3', 'prueba4', 'prueba5']
fila2 = ['cambi', 'segundafila1', 'segundafila3', 'segundafila4', 'segundafila6']
fila3 = ['camb', 'update1', 'update2', 'update3', 'update4']


insert_fila(table, fila)
insert_fila(table, fila2)

print(table)
print(get_fila(table,'cambio'))

print(update_fila(table,fila3))
print(delete_fila(table,'cambio'))

