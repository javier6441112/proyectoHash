from tkinter import *
import tkinter as tk
from tkinter import messagebox
from openpyxl import Workbook

def open_reportes(parent, crud):
    def guardar_en_excel():
        wb = Workbook()
        ws = wb.active
        ws.title = "Datos CRUD"

        ws.append(["Codigo", "Nombre", "Precio", "Cantidad", "Peso"])

        for fila in crud.table:
            for columna in zip(*fila):
                ws.append(columna)

        try:
            wb.save("Reporte_CRUD.xlsx")
            messagebox.showinfo("Éxito", "Archivo Excel generado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el archivo:\n{e}")

    reporte_window = tk.Toplevel(parent)
    reporte_window.title("Generar Reportes")
    reporte_window.geometry("500x400")
    reporte_window.iconbitmap("Assets/Logo.ico")
    reporte_window.resizable(False, False)

    # Botón sin ícono, pero con estilo
    boton_guardar = tk.Button(
        reporte_window,
        text="Guardar en Excel",
        font=("Segoe UI", 10, "bold"),
        bg="#1D6F42",
        fg="white",
        padx=10,
        pady=5,
        command=guardar_en_excel
    )
    boton_guardar.pack(pady=30)
