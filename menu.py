import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from registrar import open_registrar_window
from consultar import open_consultar
from actualizar import open_actualizar
from reportes import open_reportes
from Crud import Crud

crud = Crud()

def open_eliminar():
    new_window = tk.Toplevel(root)
    new_window.title("Eliminar Producto")
    new_window.geometry("400x300")
    new_window.iconbitmap("Assets/Logo.ico")
    frame = ttk.Frame(new_window, padding="10")
    frame.pack(expand=True, fill='both')

    label_code = ttk.Label(frame, text="Ingrese el código del producto a eliminar:")
    label_code.pack(pady=(10,5))

    entry_code = ttk.Entry(frame)
    entry_code.pack(pady=(0,10))

    message_label = ttk.Label(frame, text="", font=("Helvetica", 12))
    message_label.pack(pady=(10,10))

    def eliminar():
        code = entry_code.get().strip()
        if code:
            crud.delete_fila(code)
            message_label.config(text="Producto eliminado", foreground="green")
        else:
            message_label.config(text="Por favor ingrese un código.", foreground="red")

    eliminar_btn = ttk.Button(frame, text="Eliminar", command=eliminar)
    eliminar_btn.pack(pady=(5,10))

def verificar_contrasenia():
    contrasenia = entry_contrasenia.get()
    if contrasenia == "admin123":
        # Ocultamos la pantalla de contraseña y mostramos el menú principal
        login_frame.pack_forget()
        main_frame.pack(expand=True, fill='both')
    else:
        messagebox.showerror("Error", "Contraseña incorrecta")

# ===============================================================
# Menú Principal con botones e íconos
# ===============================================================
root = tk.Tk()
root.title("Gestión de Inventario")
root.geometry("600x500")
root.iconbitmap("Assets/Logo.ico")
root.resizable(False, False)

# Cargar íconos desde la carpeta "Assets"
try:
    registrar_icon = tk.PhotoImage(file="Assets/registrar.png").subsample(2,2)
except Exception as e:
    registrar_icon = None
try:
    consultar_icon = tk.PhotoImage(file="Assets/consultar.png").subsample(2,2)
except Exception as e:
    consultar_icon = None
try:
    actualizar_icon = tk.PhotoImage(file="Assets/actualizar.png").subsample(2,2)
except Exception as e:
    actualizar_icon = None
try:
    eliminar_icon = tk.PhotoImage(file="Assets/eliminar.png").subsample(2,2)
except Exception as e:
    eliminar_icon = None
try:
    reportes_icon = tk.PhotoImage(file="Assets/reportes.png").subsample(2,2)
except Exception as e:
    reportes_icon = None

# Frame de Login (pantalla inicial para ingresar la contraseña)
login_frame = ttk.Frame(root, padding="20")
login_frame.pack(expand=True, fill='both')

tk.Label(login_frame, text="Ingrese la contraseña para acceder al sistema:", font=("Helvetica", 14)).pack(pady=(10, 10))
entry_contrasenia = ttk.Entry(login_frame, show="*", font=("Helvetica", 12))
entry_contrasenia.pack(pady=(0, 20))
ttk.Button(login_frame, text="Acceder", command=verificar_contrasenia).pack()

# Frame del Menú Principal (se muestra después de ingresar la contraseña correcta)
main_frame = ttk.Frame(root, padding="20")

welcome_label = ttk.Label(main_frame, text="Bienvenido a Gestión de Inventario", font=("Helvetica", 20, "bold"))
welcome_label.pack(pady=(10, 5))
desc_label = ttk.Label(main_frame, text="Por favor seleccione una opción", font=("Helvetica", 14))
desc_label.pack(pady=(0, 20))

buttons_frame = ttk.Frame(main_frame)
buttons_frame.pack(expand=True)

registrar_btn = ttk.Button(buttons_frame, text="Registrar", image=registrar_icon, compound="top", command=lambda: open_registrar_window(root, crud))
consultar_btn = ttk.Button(buttons_frame, text="Consultar", image=consultar_icon, compound="top", command=lambda: open_consultar(root, crud))
actualizar_btn = ttk.Button(buttons_frame, text="Actualizar", image=actualizar_icon, compound="top", command=lambda: open_actualizar(root, crud))
eliminar_btn = ttk.Button(buttons_frame, text="Eliminar", image=eliminar_icon, compound="top", command=open_eliminar)
reportes_btn = ttk.Button(buttons_frame, text="Generar Reportes", image=reportes_icon, compound="top", command=lambda: open_reportes(root, crud))

registrar_btn.grid(row=0, column=0, padx=15, pady=15)
consultar_btn.grid(row=0, column=1, padx=15, pady=15)
actualizar_btn.grid(row=1, column=0, padx=15, pady=15)
eliminar_btn.grid(row=1, column=1, padx=15, pady=15)
reportes_btn.grid(row=2, column=0, columnspan=2, padx=15, pady=15)

root.mainloop()
