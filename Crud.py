CONSTANTE_HASH = 0.6180339887
TAMANIO_FILAS = 2
TAMANIO_COLUMNAS = 5

class Crud:

    def __init__(self):
        # Inicializa la tabla
        self.table = [[[] for _ in range(TAMANIO_COLUMNAS)] for _ in range(TAMANIO_FILAS)]

    # calcula el valor hash de la cadena ingresada
    #(toma la posición de cada carácter y lo multiplica por su valor ASCII)
    def ascii_hash(self, valorLlave):
        return sum((i + 1) * ord(ch) for i, ch in enumerate(valorLlave))

    # cálculo del índice utilizando el método multiplicación
    def hash_index(self, key, table_size):
        return int(table_size * ((key * CONSTANTE_HASH) % 1))

    # inserta una fila completa, ya maneja las colisiones
    def insert_fila(self, fila):
        key = self.ascii_hash(fila[0])  # Llamar al método de la instancia con `self`
        index = self.hash_index(key, TAMANIO_FILAS)  # Llamar al método de la instancia con `self`
        for i, item in enumerate(fila):
            self.table[index][i].append(item)

    def get_fila(self, valorLlave):
        # Calculamos la clave y el índice de hash
        key = self.ascii_hash(valorLlave)  # Llamar al método de la instancia con `self`
        index = self.hash_index(key, TAMANIO_FILAS)  # Llamar al método de la instancia con `self`
        fila3 = []
        for i, sublista in enumerate(self.table[index][0]):
            if sublista == valorLlave:
                for j, subList2 in enumerate(self.table[index]):
                    fila3.append(subList2[i])
        return fila3

    def update_fila(self, nuevaFila):
        key = self.ascii_hash(nuevaFila[0])  # Llamar al método de la instancia con `self`
        index = self.hash_index(key, TAMANIO_FILAS)  # Llamar al método de la instancia con `self`
        for i, sublista in enumerate(self.table[index][0]):
            if sublista == nuevaFila[0]:
                for j, subList2 in enumerate(self.table[index]):
                    self.table[index][j][i] = nuevaFila[j]
        return self.table

    def delete_fila(self, valorLlave):
        key = self.ascii_hash(valorLlave)  # Llamar al método de la instancia con `self`
        index = self.hash_index(key, TAMANIO_FILAS)  # Llamar al método de la instancia con `self`
        for i, sublista in enumerate(self.table[index][0]):
            if sublista == valorLlave:
                for j, subList2 in enumerate(self.table[index]):
                    del self.table[index][j][i]
        return self.table

