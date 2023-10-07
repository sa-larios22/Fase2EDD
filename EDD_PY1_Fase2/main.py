from arbolAVL.lectura import cargar_json

import tkinter as tk
import csv

from tkinter import ttk, messagebox, filedialog

from tablaHash.tablaHash import TablaHash
from arbolAVL.lectura import graficar_arbol, graficar_arbolB, lista_enlazada
from listaEnlazada.listaEnlazada import ListaEnlazada

tablaGlobal = TablaHash()

def verificar_login():
    global usuario, contrasena
    
    usuario = ""
    contrasena = ""
    
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()

    if usuario == "PM-202111849" and contrasena == "PM-202111849" or usuario == "1" and contrasena == "1":
        ventana_login.destroy() 
        admin_menu()   
    elif tablaGlobal.buscar(usuario, contrasena) or usuario == "2" and contrasena == "2":
        ventana_login.destroy()
        user_menu()
    else:
        messagebox.showerror("Error de inicio de sesión", "Credenciales incorrectas")

def admin_menu():
    global ventana_admin
    ventana_admin = tk.Tk()
    ventana_admin.title("Menú Principal")
    ventana_admin.geometry("640x480")
    ventana_admin.configure(bg="#A0FAE3")
    
    # Label "Menú de Administrador"
    label_admin = tk.Label(ventana_admin, text="Menú de Administrador", font=('Arial', 24, 'bold'), background="#A0FAE3", foreground="black")
    label_admin.pack(pady=20)

    # Botón Proyectos
    btn_proyectos = tk.Button(ventana_admin, text="Proyectos", fg="white", font=('Arial', 18, 'bold'), background="#0388a9", command=admin_menu_proyectos)
    btn_proyectos.pack(pady=20)

    # Botón Empleados
    btn_2 = tk.Button(ventana_admin, text="Empleados", fg="white", font=('Arial', 18, 'bold'), background="#0388a9", command=admin_menu_empleados)
    btn_2.pack(pady=20)

    # Botón Cerrar Sesión
    btn_3 = tk.Button(ventana_admin, text="Cerrar Sesión", fg="white", font=('Arial', 18, 'bold'), background="#0388a9", command = abrir_ventana_login)
    btn_3.pack(pady=20)

def admin_menu_proyectos():
    global ventana_proyectos, textbox
    ventana_admin.destroy()
    
    ventana_proyectos = tk.Tk()
    ventana_proyectos.title("Menú Proyectos")
    ventana_proyectos.geometry("1280x700")
    ventana_proyectos.configure(bg="#A0FAE3")

    # Botón "Cargar JSON"
    btn_cargar_json = tk.Button(ventana_proyectos, text="Cargar JSON", fg="white", background="#0388a9", font=('Arial', 18, 'bold'), command=load_json)
    btn_cargar_json.pack(pady=20, anchor='w', padx=10)

    # Caja de texto
    textbox = tk.Text(ventana_proyectos, height=30, wrap=tk.WORD)
    textbox.pack(pady=10, fill=tk.X, padx=20)

    # Botón "Reporte de Proyectos"
    btn_1 = tk.Button(ventana_proyectos, text="Reporte Proyectos", fg="white", background="#0388a9", font=('Arial', 18, 'bold'), command=reporte_proyectos)
    btn_1.pack(pady=10, side=tk.LEFT, padx=10)

    # Botón "Reporte de Tareas"
    btn_2 = tk.Button(ventana_proyectos, text="Reporte de Tareas", fg="white", background="#0388a9", font=('Arial', 18, 'bold'), command=reporte_tareas)
    btn_2.pack(pady=10, side=tk.LEFT, padx=10)

    # Volver a la ventana anterior
    def return_to_main():
        ventana_proyectos.destroy()
        admin_menu()

    btn_return = tk.Button(ventana_proyectos, text="Regresar", fg="white", background="#0388a9", font=('Arial', 18, 'bold'), command=return_to_main)
    btn_return.pack(pady=10, side=tk.RIGHT, padx=10)

    ventana_proyectos.mainloop()

def admin_menu_empleados():
    global ventana_empleados
    ventana_admin.destroy()

    ventana_empleados = tk.Tk()
    ventana_empleados.title("Listado de Empleados")
    ventana_empleados.geometry("1280x700")
    ventana_empleados.configure(bg="#A0FAE3")

    tabla = ttk.Treeview(ventana_empleados, columns=("Columna1", "Columna2", "Columna3", "Columna4"))
    tabla.column("#0", width=0, stretch=tk.NO)
    tabla.heading("#1", text="No.")
    tabla.heading("#2", text="Codigo Empleado")
    tabla.heading("#3", text="Nombre")
    tabla.heading("#4", text="Puesto")

    style = ttk.Style(ventana_empleados)
    
    style.configure("Treeview",
                    font=('Arial', 16),
                    background="#f7f7f7",
                    foreground="black",
                    rowheight=25,
                    fieldbackground="#E1E1E1")
    
    style.configure("Treeview.Heading",
                    font=('Arial', 18, 'bold'),
                    background="#f7f7f7",
                    foreground="Black")
    
    style.map('Treeview', background=[('selected', '#0388a9')])
    
    tabla.column("#1", width=50, anchor=tk.W)
    tabla.column("#2", width=150, anchor=tk.W)
    tabla.column("#3", width=300, anchor=tk.W)
    tabla.column("#4", width=200, anchor=tk.W)

    def AgregarTabla():
        tabla.delete(*tabla.get_children())
        for clave, valor in tablaGlobal.tabla.items():
            #print(f"Clave: {clave}, Valor: {valor.codigo}")
            tabla.insert("", "end", values=(clave, valor.codigo, valor.nombre, valor.puesto))

    if tablaGlobal.utilizacion > 0:
        AgregarTabla()

    def leer_csv():
        ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])

        if ruta_archivo:
            tabla.delete(*tabla.get_children()) 

            with open(ruta_archivo, newline="\n", encoding="utf-8") as archivo_csv:
                lector_csv = csv.reader(archivo_csv, delimiter=",")
                next(lector_csv) 

                for fila in lector_csv:
                    #print(fila)
                    
                    codigo,nombre,password,puesto = fila
                    tablaGlobal.Insertar(codigo,nombre,password,puesto)
            AgregarTabla()

    boton_leer_csv = tk.Button(ventana_empleados, text="Leer CSV", command=leer_csv, font=('Arial', 18, 'bold'), fg="white", background="#0388a9")
    boton_leer_csv.pack(pady=20)

    tabla.pack(pady=10, padx=20, fill = tk.X, expand=1)
    
    def regresar():
        ventana_empleados.destroy()
        admin_menu()

    boton_cerrar_sesion = tk.Button(ventana_empleados, text="Regresar", font=('Arial', 18, 'bold'), fg="white", background="#0388a9", command=regresar)
    boton_cerrar_sesion.pack(pady=20)

    ventana_empleados.mainloop()

def abrir_ventana_login():
    try:
        ventana_admin.destroy()
    except:
        pass
    
    global ventana_login, entry_usuario, entry_contrasena
    ventana_login = tk.Tk()
    ventana_login.title("ProjectUp - 202111849")
    ventana_login.geometry("480x640") 
    ventana_login.configure(bg="#A0FAE3")
    
    imagen = tk.PhotoImage(file="unnamed.png")

    label_imagen = ttk.Label(ventana_login, image=imagen, font=('Arial', 24))
    label_imagen.pack(pady=20)
    label_portada = tk.Label(ventana_login, text="INICIO DE SESION\nProjectUp",font=('Arial', 18, 'bold'), background="#A0FAE3")
    label_portada.pack(pady=20)

    label_usuario = tk.Label(ventana_login, text="Usuario:", font=('Arial', 16), background="#A0FAE3")
    label_contrasena = tk.Label(ventana_login, text="Contraseña:", font=('Arial', 16), background="#A0FAE3")
    entry_usuario = tk.Entry(ventana_login, font=('Arial', 16))
    entry_contrasena = tk.Entry(ventana_login, show="*", font=('Arial', 16)) 

    label_usuario.pack()
    entry_usuario.pack()
    
    label_contrasena.pack()
    entry_contrasena.pack()

    boton_ingresar = tk.Button(ventana_login, text="Ingresar", command=verificar_login, fg="white",font=('Arial', 18, 'bold'), background="#0388a9")
    boton_ingresar.pack(pady=20)

    label_pie = tk.Label(ventana_login, text="2023 - 202111849", font=('Arial', 16), background="#A0FAE3")
    label_pie.pack(pady=20)

    ventana_login.mainloop()

def load_json():
    file_path = filedialog.askopenfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
    if file_path:
        contenido = cargar_json(file_path)
        textbox.delete(1.0, tk.END)
        textbox.insert(tk.END, contenido)

def reporte_proyectos():
    graficar_arbol()

def reporte_tareas():
    graficar_arbolB()

def user_menu():
    global ventana_usuario, tree
    ventana_usuario = tk.Tk()
    ventana_usuario.title("Menú Principal")
    ventana_usuario.geometry("1280x720")
    ventana_usuario.configure(bg="#A0FAE3")
    
   # Imagen
    image = tk.PhotoImage(file="user.png")  # Ensure the image path is correct
    image_label = tk.Label(ventana_usuario, image=image, bg="#A0FAE3")
    image_label.pack(side=tk.TOP, anchor=tk.NE, padx=10, pady=10)

    # Label del usuario
    text_label = tk.Label(ventana_usuario, text=usuario, bg="#A0FAE3", font=('Arial', 16))
    text_label.pack(side=tk.TOP, anchor=tk.NE, padx=10, pady=10)

    # Label del título
    label = tk.Label(ventana_usuario, text="Visualización de Tareas", fg="black", bg="#A0FAE3", font=('Arial', 24, 'bold'))
    label.pack(side=tk.TOP, anchor=tk.CENTER, pady=0)
    
    # Tabla
    tree = ttk.Treeview(ventana_usuario, columns=("Columna1", "Columna2", "Columna3"), show="headings")
    tree.heading("Columna1", text="Código de Tarea")
    tree.heading("Columna2", text="Nombre del Proyecto")
    tree.heading("Columna3", text="Nombre de la Tarea")
    
    style = ttk.Style(ventana_usuario)
    style.configure("Treeview",
                    font=('Arial', 16),
                    background="#f7f7f7",
                    foreground="black",
                    rowheight=25,
                    fieldbackground="#E1E1E1")
    style.configure("Treeview.Heading",
                    font=('Arial', 18, 'bold'),
                    background="#f7f7f7",
                    foreground="Black")
    style.map('Treeview', background=[('selected', '#0388a9')])

    tree.column("#1", width=50, anchor=tk.W)
    tree.column("#2", width=150, anchor=tk.W)
    tree.column("#3", width=300, anchor=tk.W)
    
    tree.pack(side=tk.TOP, anchor=tk.CENTER, padx=10, pady=10, expand=True, fill=tk.BOTH)
    
    def cerrar_sesion():
        ventana_usuario.destroy()
        abrir_ventana_login()
    
    btn_cargar = tk.Button(ventana_usuario, text="Cargar Tareas",  fg="white", font=('Arial', 18, 'bold'), background="#0388a9", command=cargar_tareas)
    btn_cargar.pack(side=tk.BOTTOM, anchor=tk.SW, padx=10, pady=10)
    
    btn_regresar = tk.Button(ventana_usuario, text="Regresar",  fg="white", font=('Arial', 18, 'bold'), background="#0388a9", command=cerrar_sesion)
    btn_regresar.pack(side=tk.BOTTOM, anchor=tk.SE, padx=10, pady=10)
    
    ventana_usuario.mainloop()

def cargar_tareas():
    lista_enlazada.imprimir()
    coincidencias = lista_enlazada.buscar_por_empleado(usuario)
    
    for coincidencia in coincidencias:
        tree.insert("", tk.END, values=(coincidencia.codigo, coincidencia.proyecto, coincidencia.nombre))

abrir_ventana_login()