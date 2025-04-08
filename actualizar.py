import tkinter as tk
from tkinter import ttk

def open_actualizar(parent, crud):
    actualizar_window = tk.Toplevel(parent)
    actualizar_window.title("Actualizar Producto")
    actualizar_window.geometry("500x450")
    actualizar_window.iconbitmap("Assets/Logo.ico")
    actualizar_window.resizable(False, False)
    
    # Contenedor principal
    frame = ttk.Frame(actualizar_window, padding="10")
    frame.pack(expand=True, fill='both')
    
    # Sección de búsqueda: Ingresar el código a buscar
    label_search = ttk.Label(frame, text="Ingrese el código del producto a actualizar:")
    label_search.pack(pady=(10,5))
    entry_search = ttk.Entry(frame, width=30)
    entry_search.pack(pady=(0,10))
    
    search_message = ttk.Label(frame, text="", font=("Helvetica", 12))
    search_message.pack(pady=(5,10))
    
    # Contenedor del formulario de actualización (se llenará tras buscar)
    form_frame = ttk.Frame(frame, padding="10")
    form_frame.pack(expand=True, fill='both')
    
    # Campo Código (readonly)
    label_code = ttk.Label(form_frame, text="Código:")
    label_code.grid(row=0, column=0, pady=(5, 2), sticky="w")
    entry_code = ttk.Entry(form_frame, width=30, state="readonly")
    entry_code.grid(row=0, column=1, pady=(5, 2), sticky="w")
    
    # Campo Nombre
    label_name = ttk.Label(form_frame, text="Nombre:")
    label_name.grid(row=1, column=0, pady=(5, 2), sticky="w")
    entry_name = ttk.Entry(form_frame, width=30)
    entry_name.grid(row=1, column=1, pady=(5, 2), sticky="w")
    
    # Campo Precio
    label_precio = ttk.Label(form_frame, text="Precio:")
    label_precio.grid(row=2, column=0, pady=(5, 2), sticky="w")
    entry_precio = ttk.Entry(form_frame, width=30)
    entry_precio.grid(row=2, column=1, pady=(5, 2), sticky="w")
    
    # Campo Cantidad
    label_cantidad = ttk.Label(form_frame, text="Cantidad:")
    label_cantidad.grid(row=3, column=0, pady=(5, 2), sticky="w")
    entry_cantidad = ttk.Entry(form_frame, width=30)
    entry_cantidad.grid(row=3, column=1, pady=(5, 2), sticky="w")
    
    # Campo Peso: Entry para el valor y Combobox para la unidad
    label_peso = ttk.Label(form_frame, text="Peso:")
    label_peso.grid(row=4, column=0, pady=(5, 2), sticky="w")
    entry_peso = ttk.Entry(form_frame, width=20)
    entry_peso.grid(row=4, column=1, pady=(5, 2), sticky="w")
    unit_combobox = ttk.Combobox(form_frame, 
                                 values=("kg", "lb", "g", "oz", "ton"), 
                                 width=5, 
                                 state="readonly")
    unit_combobox.grid(row=4, column=2, padx=(5,0), pady=(5,2), sticky="w")
    unit_combobox.set("kg")
    
    update_message = ttk.Label(frame, text="", font=("Helvetica", 12))
    update_message.pack(pady=(5,10))
    
    def buscar_actualizar():
        code = entry_search.get().strip()
        if code:
            data = crud.get_fila(code)
            if data:
                entry_code.configure(state="normal")
                entry_code.delete(0, tk.END)
                entry_code.insert(0, data[0])
                entry_code.configure(state="readonly")
                
                entry_name.delete(0, tk.END)
                entry_name.insert(0, data[1])
                
                entry_precio.delete(0, tk.END)
                entry_precio.insert(0, data[2])
                
                entry_cantidad.delete(0, tk.END)
                entry_cantidad.insert(0, data[3])
                
                # Suponemos que el campo peso viene como "valor unidad"
                peso_parts = data[4].split()
                if len(peso_parts) >= 2:
                    entry_peso.delete(0, tk.END)
                    entry_peso.insert(0, peso_parts[0])
                    unit_combobox.set(peso_parts[1])
                else:
                    entry_peso.delete(0, tk.END)
                    unit_combobox.set("kg")
                search_message.config(text="Datos cargados. Modifique y presione Actualizar.", foreground="green")
            else:
                search_message.config(text="Producto no encontrado.", foreground="red")
        else:
            search_message.config(text="Por favor ingrese un código.", foreground="red")
    
    def actualizar():
        code_val = entry_code.get().strip()
        if not code_val:
            update_message.config(text="Código no puede estar vacío.", foreground="red")
            return
        nombre_val = entry_name.get().strip()
        if not nombre_val:
            update_message.config(text="El nombre es obligatorio.", foreground="red")
            return
        precio_val = entry_precio.get().strip()
        try:
            precio_num = float(precio_val)
            if precio_num < 0:
                update_message.config(text="El precio debe ser positivo.", foreground="red")
                return
        except ValueError:
            update_message.config(text="El precio debe ser un número.", foreground="red")
            return
        cantidad_val = entry_cantidad.get().strip()
        try:
            cantidad_num = int(cantidad_val)
            if cantidad_num < 0:
                update_message.config(text="La cantidad debe ser positiva.", foreground="red")
                return
        except ValueError:
            update_message.config(text="La cantidad debe ser un número entero.", foreground="red")
            return
        peso_val = entry_peso.get().strip()
        try:
            peso_num = float(peso_val)
            if peso_num < 0:
                update_message.config(text="El peso debe ser positivo.", foreground="red")
                return
        except ValueError:
            update_message.config(text="El peso debe ser un número.", foreground="red")
            return
        unidad_val = unit_combobox.get().strip()
        
        final_peso = f"{peso_val} {unidad_val}"
        nuevos_datos = [code_val, nombre_val, str(precio_num), str(cantidad_num), final_peso]
        
        crud.update_fila(nuevos_datos)
        update_message.config(text="Producto actualizado exitosamente.", foreground="green")
        
        # Limpiar todos los campos para actualizar otro producto
        entry_search.delete(0, tk.END)
        entry_code.configure(state="normal")
        entry_code.delete(0, tk.END)
        entry_code.configure(state="readonly")
        entry_name.delete(0, tk.END)
        entry_precio.delete(0, tk.END)
        entry_cantidad.delete(0, tk.END)
        entry_peso.delete(0, tk.END)
        unit_combobox.set("kg")
    
    buscar_btn = ttk.Button(frame, text="Buscar", command=buscar_actualizar)
    buscar_btn.pack(pady=(5,5))
    
    actualizar_btn = ttk.Button(frame, text="Actualizar", command=actualizar)
    actualizar_btn.pack(pady=(5,5))
