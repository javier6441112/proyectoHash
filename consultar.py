import tkinter as tk
from tkinter import ttk

def open_consultar(parent, crud):
    consultar_window = tk.Toplevel(parent)
    consultar_window.title("Consultar Producto")
    consultar_window.geometry("600x400")
    consultar_window.iconbitmap("Assets/Logo.ico")
    consultar_window.resizable(False, False)
    
    frame = ttk.Frame(consultar_window, padding="10")
    frame.pack(expand=True, fill='both')
    
    search_frame = ttk.Frame(frame)
    search_frame.pack(fill='x', pady=(0, 10))
    
    label_code = ttk.Label(search_frame, text="Ingrese el código del producto:")
    label_code.pack(side='left', padx=(0, 10))
    
    entry_code = ttk.Entry(search_frame)
    entry_code.pack(side='left', padx=(0, 10))
    
    result_label = ttk.Label(frame, text="", font=("Helvetica", 12))
    result_label.pack(pady=(0, 10))
    
    columns = ("codigo", "nombre", "precio", "cantidad", "peso")
    tree = ttk.Treeview(frame, columns=columns, show='headings', height=10)
    for col in columns:
        tree.heading(col, text=col.capitalize())
        tree.column(col, width=100, anchor='center')
    tree.pack(expand=True, fill='both')
    
    def cargar_productos():
        for row in tree.get_children():
            tree.delete(row)
        productos = []
        for bucket in crud.table:
            for i in range(len(bucket[0])):
                producto = [bucket[j][i] for j in range(len(bucket))]
                productos.append(producto)
        for producto in productos:
            tree.insert("", "end", values=producto)
    
    def buscar():
        code = entry_code.get().strip()
        if code:
            result = crud.get_fila(code)
            if result:
                result_label.config(text=f"Datos: {result}", foreground="green")
                for item in tree.selection():
                    tree.selection_remove(item)
                for item in tree.get_children():
                    values = tree.item(item, "values")
                    if values and values[0] == code:
                        tree.selection_set(item)
                        tree.see(item)
                        break
            else:
                result_label.config(text="Producto no encontrado.", foreground="red")
        else:
            result_label.config(text="Por favor ingrese un código.", foreground="red")
    
    buscar_btn = ttk.Button(search_frame, text="Buscar", command=buscar)
    buscar_btn.pack(side='left')
    
    refresh_btn = ttk.Button(frame, text="Refrescar lista", command=cargar_productos)
    refresh_btn.pack(pady=(10, 0))
    
    cargar_productos()
