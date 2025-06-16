"""
Acciones del menú:

Agregar producto
Buscar producto
Actualizar cantidad/precio
Mostrar inventario completo
Eliminar producto
Salir
"""
opcion=0
ListaProductos=[]
#producto={"nombre":nombre,""}

def SolicitarProducto():
    nombreProd= input("Ingrese el nombre del nuevo producto: ")
    try:
        stockProd= int(input("Ingrese el stock del nuevo producto: "))
        precioProd= int(input("Ingrese el precio del nuevo producto: "))
        if precioProd<0 or stockProd<0:
            raise ValueError
        else:
            return[nombreProd,stockProd,precioProd]
        
    except ValueError:
        print("Debe ingresar valores númericos positivos")

def buscarProducto(nombre):

    for producto in ListaProductos:
        if producto["nombre"].lower()==nombre.lower():
            return producto
    
    return None

def guardarProducto(nombre,stock,precio):

    if buscarProducto(nombre)==None:
        producto={"nombre":nombre,"cantidad":stock,"precio":precio}
        ListaProductos.append(producto)
        print("Producto guardado con éxito")
    else:
        print("Ya existe un producto con ese nombre")

def actualizarProducto(nombre,NuevoStock,NuevoPrecio):
    productoBuscado=buscarProducto(nombre)
    if productoBuscado!=None:
        indice= ListaProductos.index(productoBuscado)
        productoBuscado["cantidad"]=NuevoStock
        productoBuscado["precio"]=NuevoPrecio
        ListaProductos[indice]=productoBuscado
        print(f"El producto {nombre} fué actualizado correctamente")
    else:
        print("El producto que desea actualizar no existe")

def mostrarInventarioCompleto():
    if len(ListaProductos)==0:
        print("No hay productos aún")
    else: 
        for producto in ListaProductos:
            print(f"{producto["nombre"]} \t\t Stock: ${producto["cantidad"]} \t\t Precio: {producto["precio"]}")

while opcion!="6":
    print("**************Menu de gestión de inventario**************")
    print("1.- Agregar producto")
    print("2.- Buscar producto")
    print("3.- Actualizar cantidad/precio")
    print("4.- Mostrar inventario completo")
    print("5.- Eliminar producto")
    print("6.- Salir")

    opcion= input("Ingrese la opción que desea(1-6): ")

    match opcion:
        case "1":
            infoProducto=SolicitarProducto()
            if infoProducto!=None:
                guardarProducto(infoProducto[0],infoProducto[1],infoProducto[2])
        case "2":
            nombre=input("Ingrese el nombre del producto a actualizar: ")
            productoEncontrado=buscarProducto(nombre)
            if productoEncontrado!=None:
                print("-"*60)
                print(f"Nombre: {productoEncontrado["nombre"]} \t\t Stock: ${productoEncontrado["cantidad"]} \t\t Precio: {productoEncontrado["precio"]}")
                print("-"*60)
        case "3":
            infoProducto=SolicitarProducto()
            if infoProducto!= None:
                actualizarProducto(infoProducto[0],infoProducto[1],infoProducto[2])
        case "4":
            mostrarInventarioCompleto()

       

