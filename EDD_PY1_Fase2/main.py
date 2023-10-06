from arbolAVL.lectura import cargar_json

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
from tablaHash.tablaHash import TablaHash

tablaGlobal = TablaHash()

def verificar_login():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()

    if usuario == "202111849" and contrasena == "admin" or usuario == "1" and contrasena == "1":
        ventana_login.destroy() 
        menu_principal()  
    elif tablaGlobal.buscar(usuario, contrasena):
        ventana_login.destroy()  
        admin_menu_empleados()  
    else:
        messagebox.showerror("Error de inicio de sesión", "Credenciales incorrectas")

def menu_principal():
    global ventana_principal
    ventana_principal = tk.Tk()
    ventana_principal.title("Menú Principal")
    ventana_principal.geometry("1280x700")
    
    # Label "Menú de Administrador"
    label_admin = tk.Label(ventana_principal, text="Menú de Administrador", font=('Arial', 24))
    label_admin.pack(pady=20)

    # Button "Proyectos"
    btn_proyectos = tk.Button(ventana_principal, text="Proyectos", font=('Arial', 18), command=admin_menu_proyectos)
    btn_proyectos.pack(pady=20)

    # Button "Button 2"
    btn_2 = tk.Button(ventana_principal, text="Empleados", font=('Arial', 18), command=admin_menu_empleados)
    btn_2.pack(pady=20)

    # Button "Button 3"
    btn_3 = tk.Button(ventana_principal, text="Button 3", font=('Arial', 18))
    btn_3.pack(pady=20)

def admin_menu_proyectos():
    global ventana_proyectos, textbox
    ventana_principal.destroy()
    
    ventana_proyectos = tk.Tk()
    ventana_proyectos.title("Menú Proyectos")
    ventana_proyectos.geometry("1280x700")

    # Button "Cargar JSON" centered to the left
    btn_cargar_json = tk.Button(ventana_proyectos, text="Cargar JSON", font=('Arial', 18), command=load_json)
    btn_cargar_json.pack(pady=20, anchor='w', padx=20)

    # Textbox that adapts to the size of the window horizontally
    textbox = tk.Text(ventana_proyectos, height=30, wrap=tk.WORD)
    textbox.pack(pady=10, fill=tk.X, padx=20)

    # Button "Button 1"
    btn_1 = tk.Button(ventana_proyectos, text="Button 1", font=('Arial', 18))
    btn_1.pack(pady=10, side=tk.LEFT, padx=10)

    # Button "Button 2"
    btn_2 = tk.Button(ventana_proyectos, text="Button 2", font=('Arial', 18))
    btn_2.pack(pady=10, side=tk.LEFT, padx=10)

    # Button for returning to the previous window
    def return_to_main():
        ventana_proyectos.destroy()
        menu_principal()

    btn_return = tk.Button(ventana_proyectos, text="Regresar", font=('Arial', 18), command=return_to_main)
    btn_return.pack(pady=20, anchor='e', padx=20)

    ventana_proyectos.mainloop()

def admin_menu_empleados():
    ventana_principal.destroy()
    
    ventana_empleados = tk.Tk()
    ventana_empleados.title("Manejo de Empleados")
    ventana_empleados.geometry("1280x700")

    tabla = ttk.Treeview(ventana_empleados, columns=("Columna1", "Columna2", "Columna3", "Columna4"))
    tabla.heading("#1", text="No.")
    tabla.heading("#2", text="Codigo Empleado")
    tabla.heading("#3", text="Nombre")
    tabla.heading("#4", text="Puesto")

    def AgregarTabla():
        tabla.delete(*tabla.get_children())
        for clave, valor in tablaGlobal.tabla.items():
            print(f"Clave: {clave}, Valor: {valor.codigo}")
            tabla.insert("", "end", values=(clave, valor.codigo, valor.nombre, valor.puesto))

    if tablaGlobal.utilizacion > 0:
        AgregarTabla()

    def leer_csv():
        ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])

        if ruta_archivo:
            tabla.delete(*tabla.get_children()) 

            with open(ruta_archivo, newline="\n") as archivo_csv:
                lector_csv = csv.reader(archivo_csv)
                next(lector_csv) 

                for fila in lector_csv:
                    id,nombre,password,puesto = fila #[FDEV-101,Cristian Suy,cris123,Frontend Developer]
                    tablaGlobal.Insertar(id,nombre,password,puesto)
            AgregarTabla()

    boton_leer_csv = tk.Button(ventana_empleados, text="Leer CSV", command=leer_csv)
    boton_leer_csv.pack(pady=20)

    tabla.pack(pady=20)
    
    def cerrar_sesion():
        ventana_empleados.destroy()
        abrir_ventana_login()

    boton_cerrar_sesion = tk.Button(ventana_empleados, text="Cerrar Sesión", command=cerrar_sesion)
    boton_cerrar_sesion.pack(pady=20)

    ventana_empleados.mainloop()

def abrir_ventana_login():
    global ventana_login, entry_usuario, entry_contrasena
    ventana_login = tk.Tk()
    ventana_login.title("ProjectUp")
    ventana_login.geometry("400x450") 
    imagen = tk.PhotoImage(file="unnamed.png")

    label_imagen = ttk.Label(ventana_login, image=imagen)
    label_imagen.pack(pady=20)
    label_portada = tk.Label(ventana_login, text="INICIO DE SESION\nProjectUp")
    label_portada.pack(pady=20)

    label_usuario = tk.Label(ventana_login, text="Usuario:")
    label_contrasena = tk.Label(ventana_login, text="Contraseña:")
    entry_usuario = tk.Entry(ventana_login)
    entry_contrasena = tk.Entry(ventana_login, show="*")  

    label_usuario.pack()
    entry_usuario.pack()
    
    label_contrasena.pack()
    entry_contrasena.pack()

    boton_ingresar = tk.Button(ventana_login, text="Ingresar", command=verificar_login)
    boton_ingresar.pack(pady=20)

    label_pie = tk.Label(ventana_login, text="2023 - 202111849")
    label_pie.pack(pady=20)

    ventana_login.mainloop()

def load_json():
    file_path = filedialog.askopenfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
    if file_path:
        contenido = cargar_json(file_path)
        textbox.delete(1.0, tk.END)
        textbox.insert(tk.END, contenido)

abrir_ventana_login()