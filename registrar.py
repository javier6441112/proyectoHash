import tkinter as tk
from tkinter import *
import datetime
from tkinter import ttk

def generar_codigo(crud):
    year = datetime.datetime.now().year % 100
    count = 0
    for bucket in crud.table:
        if bucket[0]:
            count += len(bucket[0])
    new_number = count + 1
    codigo = f"{year:02d}{new_number:04d}"
    return codigo

def open_registrar_window(parent, crud):
    window = Toplevel(parent)
    window.title("Ingresar producto")
    window.geometry("500x500")
    window.iconbitmap("Assets/Logo.ico")
    window.config(bg="#E0F8FE")
    window.resizable(False, False)
    
    frame = Frame(window, bg="#CBECFE", width=480, height=480)
    frame.pack(expand=True, fill=BOTH)
    
    labels = ["Codigo", "Nombre", "Precio", "Cantidad", "Peso"]
    entries = []
    
    for i, text in enumerate(labels):
        label = Label(frame, text=text, bg="#CBECFE")
        label.grid(row=i, column=0, padx=15, pady=10, sticky="nsew")
        if text == "Codigo":
            entry = Entry(frame, width=30, state="readonly")
            codigo_generado = generar_codigo(crud)
            entry.configure(state="normal")
            entry.insert(0, codigo_generado)
            entry.configure(state="readonly")
            entry.grid(row=i, column=1, padx=10, pady=5)
            entries.append(entry)
        elif text == "Peso":
            entry = Entry(frame, width=20)
            entry.grid(row=i, column=1, padx=10, pady=5)
            unit_combobox = ttk.Combobox(frame, 
                                         values=("kg", "lb", "g", "oz", "ton"), 
                                         width=5, 
                                         state="readonly")
            unit_combobox.set("kg")
            unit_combobox.grid(row=i, column=2, padx=10, pady=5)
            entries.append((entry, unit_combobox))
        else:
            entry = Entry(frame, width=30)
            entry.grid(row=i, column=1, padx=10, pady=5)
            entries.append(entry)
    
    for entry in entries:
        if isinstance(entry, tuple):
            entry[0].delete(0, END)
        else:
            entry.delete(0, END)
    
    message_label = Label(frame, text="", bg="#CBECFE", fg="red")
    message_label.grid(row=len(labels)+1, column=0, columnspan=3, pady=10)
    
    def mostrar_valores():
        codigo = entries[0].get().strip()
        nombre = entries[1].get().strip()
        precio = entries[2].get().strip()
        cantidad = entries[3].get().strip()
        peso_entry, peso_unit = entries[4]
        peso = peso_entry.get().strip()
        unidad = peso_unit.get().strip()
        
        if not codigo:
            message_label.config(text="El código es obligatorio.", fg="red")
            return
        if crud.get_fila(codigo):
            message_label.config(text="Ya existe un producto con ese código.", fg="red")
            return
        if not nombre:
            message_label.config(text="El nombre es obligatorio.", fg="red")
            return
        try:
            precio_val = float(precio)
            if precio_val < 0:
                message_label.config(text="El precio debe ser positivo.", fg="red")
                return
        except ValueError:
            message_label.config(text="El precio debe ser un número.", fg="red")
            return
        try:
            cantidad_val = int(cantidad)
            if cantidad_val < 0:
                message_label.config(text="La cantidad debe ser positiva.", fg="red")
                return
        except ValueError:
            message_label.config(text="La cantidad debe ser un número entero.", fg="red")
            return
        try:
            peso_num = float(peso)
            if peso_num < 0:
                message_label.config(text="El peso debe ser positivo.", fg="red")
                return
        except ValueError:
            message_label.config(text="El peso debe ser un número.", fg="red")
            return
        
        final_peso = f"{peso} {unidad}"
        valores = [codigo, nombre, str(precio_val), str(cantidad_val), final_peso]
        
        crud.insert_fila(valores)
        message_label.config(text="Producto registrado exitosamente.", fg="green")
        
        nuevo_codigo = generar_codigo(crud)
        entries[0].configure(state="normal")
        entries[0].delete(0, END)
        entries[0].insert(0, nuevo_codigo)
        entries[0].configure(state="readonly")
        
        entries[1].delete(0, END)
        entries[2].delete(0, END)
        entries[3].delete(0, END)
        entries[4][0].delete(0, END)
        entries[4][1].set("kg")
    
    boton = Button(frame, text="Guardar valores", command=mostrar_valores)
    boton.grid(row=len(labels), column=0, columnspan=3, pady=10)



