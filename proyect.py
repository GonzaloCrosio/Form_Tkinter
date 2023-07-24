from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Create the screen
screen = Tk()
screen.title("Menú Superior")

def add_products():
    products.append([
        name_data.get(),
        price_data.get(),
        add_description_entry.get("1.0", "1.100")       # It will store a description of a maximum of 100 characters (from 1 to 100)
    ])
    # After saving the information, clear the fields
    name_data.set("")
    price_data.set("")
    add_description_entry.delete("1.0", END)


# Important global variables
products = []
name_data = StringVar()
price_data = StringVar()

# Define screen fields. I need them to be global variables in order to clear the screens and prevent them from overlapping.
home_label = Label(screen, text="Inicio")
add_label = Label(screen, text="Añadir Producto")
info_label = Label(screen, text="Información")
data_label = Label(screen, text="Creado por Gonzalo Crosio")
data_label_second = Label(screen, text="Creado en Valencia, España")
products_table = Frame(screen, width=250)

Label(products_table).grid(row=0)
products_box = ttk.Treeview(height=12, columns=2)
products_box.grid(row=1, column=0, columnspan=2)
products_box.heading("#0", text="Producto", anchor=CENTER)
products_box.heading("#1", text="Precio", anchor=CENTER)

# Form fields. To create a frame to place all the fields inside and later be able to clear them in the other screens
add_frame = Frame(screen)

add_name_label = Label(add_frame, text="Nombre del producto")
add_name_entry = Entry(add_frame, textvariable=name_data)

add_price_label=Label(add_frame, text="Precio del producto")
add_price_entry=Entry(add_frame,textvariable=price_data)

add_description_label = Label(add_frame, text="Descripción")
add_description_entry = Text(add_frame)

boton = Button(add_frame, text="Guardar", command=add_products)

# Define screens

# Home screen
def home(): 
    # To hide previous screens
    add_frame.grid_remove()
    add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    products_box.grid_remove()
    home_label.grid_remove()
    
    
    # Set up the function
    home_label.config(fg="white", bg="black", font=("Arial", 30), padx=200, pady=20)
    home_label.grid(row=0, column=0)

    def cargar_producto():
        productos_insertados = set()

        products_box.delete(*products_box.get_children())
        for product in products:
            if product[0] not in productos_insertados:
                products_box.insert("", "end", text=product[0], values=(product[1]))
                productos_insertados.add(product[0])
                products_box.grid(row=1)
    cargar_producto()

    return True

def opcion_salir():
    if messagebox.askyesno("Salir", "¿Estás seguro que quieres salir?"):
        screen.destroy()

# Add screen
def add():
    # To hide previous screens
    products_box.grid_remove()
    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

    # Set up the function
    add_label.config(fg="white", bg="black", font=("Arial", 30), padx=190, pady=20)
    add_label.grid(row=0, column=0, columnspan=2)
    # Form fields
    add_frame.grid(row=1)

    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5,sticky=W)

    add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    add_price_entry.grid(row=2, column=1, padx=5, pady=5,sticky=W)

    add_description_label.grid(row=3, column=0, padx=5, pady=5, sticky=NE)
    add_description_entry.grid(row=3, column=1, padx=5, pady=5,sticky=W)
    add_description_entry.config(width=30, height=5, font=("consolas", 12), padx=15,pady=15)

    boton.grid(row=5, column=1, sticky=NW)
    boton.config(padx=15, pady=5, bg="white", fg="black")

    return True

# Info screen
def info():
    # To hide previous screens
    products_box.grid_remove()
    add_frame.grid_remove()
    home_label.grid_remove()
    add_label.grid_remove()
    data_label.grid_remove()
    data_label_second.grid_remove()
  
    # Set up the function
    info_label.config(fg="white", bg="black", font=("Arial", 30), padx=220, pady=20)
    info_label.grid(row=0, column=0)

    data_label.grid(row=1, column=0)
    home_label.grid_remove()
    add_label.grid_remove()

    return True

def info_second():
    # To hide previous screens
    products_box.grid_remove()
    add_frame.grid_remove()
    home_label.grid_remove()
    add_label.grid_remove()
    data_label.grid_remove()
    data_label_second.grid_remove()
  
    # Set up the function
    info_label.config(fg="white", bg="black", font=("Arial", 30), padx=220, pady=20)
    info_label.grid(row=0, column=0)

    data_label_second.grid(row=1, column=0)
    home_label.grid_remove()
    add_label.grid_remove()

    return True

# Call screen
home()

# Create the menu line
menu_superior = Menu(screen)
screen.config(menu=menu_superior)

# CCreate the menu options
menu_inicio = Menu(menu_superior, tearoff=0)
menu_anadir = Menu(menu_superior, tearoff=0)
menu_informacion = Menu(menu_superior, tearoff=0)

# Create a menu with dropdowns
menu_superior.add_cascade(label="Inicio", menu=menu_inicio)
menu_superior.add_cascade(label="Añadir", menu=menu_anadir)
menu_superior.add_cascade(label="Información", menu=menu_informacion)

# Add options to each dropdown menu
menu_inicio.add_command(label="Abrir Productos Guardados", command=home)
menu_inicio.add_command(label="Salir", command=opcion_salir)

menu_anadir.add_command(label="Añadir", command=add)

menu_informacion.add_command(label="Información Autor", command=info)
menu_informacion.add_command(label="Información Sitio", command=info_second)

# Run the main loop
screen.mainloop()