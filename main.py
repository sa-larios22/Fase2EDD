"""import tkinter as tk
from tkinter import messagebox

def on_signin_clicked():
    # Dummy function for sign-in button click
    username_value = username_entry.get()
    password_value = password_entry.get()
    
    if username_value and password_value:
        messagebox.showinfo('Acceso concedido', 'Sign-in clicked!')
    else:
        messagebox.showwarning('Acceso denegado', 'Ingrese un usuario y contraseña válidos')
        
    

# Ventana Principal
root = tk.Tk()
root.title('Login Menu')
root.geometry('480x480')
root.resizable(False, False)

# USUARIO
username_label = tk.Label(root, text='Username:', font=('Arial', 18))
username_label.pack(pady=10)

username_entry = tk.Entry(root, font=('Arial', 18))
username_entry.pack(pady=10)

# CONTRASEÑA
password_label = tk.Label(root, text='Password:', font=('Arial', 18))
password_label.pack(pady=10)

password_entry = tk.Entry(root, show='*', font=('Arial', 18))
password_entry.pack(pady=10)

# Create and place the sign-in button
signin_button = tk.Button(root, text='Iniciar Sesión', command=on_signin_clicked, font=('Arial', 18))
signin_button.pack(pady=20)

root.mainloop()"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
from tablaHash.tablaHash import TablaHash

tablaGlobal = TablaHash()

def verificar_login():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()

    if usuario == "201700918" and contrasena == "admin":
        ventana_login.destroy() 
        abrir_ventana_principal()  
    elif tablaGlobal.buscar(usuario, contrasena):
        ventana_login.destroy()  
        abrir_ventana_principal()  
    else:
        messagebox.showerror("Error de inicio de sesión", "Credenciales incorrectas")

def abrir_ventana_principal():
    ventana_principal = tk.Tk()
    ventana_principal.title("Ventana Principal")
    ventana_principal.geometry("1280x700")

    tabla = ttk.Treeview(ventana_principal, columns=("Columna1", "Columna2", "Columna3", "Columna4"))
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

    boton_leer_csv = tk.Button(ventana_principal, text="Leer CSV", command=leer_csv)
    boton_leer_csv.pack(pady=20)

    tabla.pack(pady=20)
    
    def cerrar_sesion():
        ventana_principal.destroy()
        abrir_ventana_login()

    boton_cerrar_sesion = tk.Button(ventana_principal, text="Cerrar Sesión", command=cerrar_sesion)
    boton_cerrar_sesion.pack(pady=20)

    ventana_principal.mainloop()

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

    label_pie = tk.Label(ventana_login, text="2023 - 201700918")
    label_pie.pack(pady=20)

    ventana_login.mainloop()

abrir_ventana_login()