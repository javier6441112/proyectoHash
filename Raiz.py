from tkinter import *
from Crud import *
crud = Crud()

# # Mostrar la tabla
# print(crud.table)
#
# # Obtener una fila por la clave
# print(crud.get_fila('cambi'))
# # Actualizar una fila
# print(crud.update_fila(fila3))
# # Eliminar una fila
# print(crud.delete_fila('cambio'))

raiz = Tk()
raiz.title("INVENTARIO")
raiz.geometry("500x500")
raiz.iconbitmap("Logo.ico")
raiz.config(bg="#E0F8FE")
raiz.resizable(False, False)
frame = Frame()
frame.pack()
frame.configure(background="#CBECFE")
frame.config(width=480, height=480)
labels = ["Codigo", "Nombre", "Precio", "Cantidad", "Peso"]
entries = []  # Lista para almacenar las entradas
for i, text in enumerate(labels):
    label = Label(frame, text=text, bg="#CBECFE")
    label.grid(row=i, column=0, padx=15, pady=10, sticky="nsew")  # Posicionar la etiqueta
    entry = Entry(frame, width=30)  # Crear una entrada de texto
    entry.grid(row=i, column=1, padx=10, pady=5)  # Posicionar la entrada
    entries.append(entry)  # Almacenar la entrada en la lista
for entry in entries:
        entry.delete(0, END)
# Función para obtener los valores ingresados
def mostrar_valores():
    valores = [entry.get() for entry in entries]
    print("Valores ingresados:", valores)
    crud.insert_fila(valores)
    print(crud.table)
    for entry in entries:
        entry.delete(0, END)
# Botón para obtener los valores
boton = Button(frame, text="Guardar valores", command=mostrar_valores)
boton.grid(row=len(labels), column=0, columnspan=2, pady=10)

raiz.mainloop()