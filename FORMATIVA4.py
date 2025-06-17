#ENTRADA TURISTAS

opcion=0
DatosTurista=[]
#Turista={"nombre":Nombre,"origen":PaisOrigen,"ingreso":Fecha}

turistas = {"001": ["John Doe", "Estados Unidos", "12-01-2024"],
"002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
"012": ["Julian Martinez", "Argentina", "19-09-2023"],
"014": ["Agustin Morales", "Argentina", "28-03-2024"],
"005": ["Carlos Garcia", "Mexico", "10-05-2024"],
"006": ["Maria Lopez", "Mexico", "08-12-2023"],
"007": ["Joao Silva", "Brasil", "20-06-2024"],
"003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
"004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
"008": ["Ana Santos", "Brasil", "03-10-2023"],
"010": ["Martin Fernandez", "Argentina", "13-02-2023"],
"011": ["Sofia Gomez", "Argentina", "07-04-2024"]}

def buscarTurista(nombre):
    for turista in turistas:
        if turista["nombre"].lower()==nombre.lower():
            return turista
        
    return None

def paisTurista(origen):
    resultado=[]
    for numeroID, datos in turistas.items():
        if datos[1].lower()==origen.lower():
            resultado.append((numeroID,datos))
    return resultado 

def  fechaIngreso(mes):
    resultado=[]
    for numeroID, datos in turistas.items():
        fecha=datos[2]
        mesIngreso=fecha[3:5]
        if mesIngreso==mes:
            resultado.append((numeroID,datos))
        
    return resultado
    
def eliminarTurista(nombre):
    turistaEliminar=buscarTurista(nombre)
    if turistaEliminar!=None:
        turistas.remove(turistaEliminar)
        print("Turista eliminado con exito!")
    else:
        print("Este nombre no está en nuestros registros")

 

while opcion!= "4":
    print("*** MENU PRINCIPAL ***")
    print("1.- Turistas por país.")
    print("2.- Turista por mes.")
    print("3.- Eliminar turista.")
    print("4.- Salir")

    opcion=input("Ingrese la opcion que desea realizar(1-4): ")

    match opcion:

        case "1":
          pais=input("Ingrese el pais de origen que desea buscar: ")
          encontrados=paisTurista(pais)
          print("-"*65)
          print(f"Turistas de {pais.title()}: {len(encontrados)} encontrados.")
          for numeroID, datos in encontrados:
              print(f"Nombre: {datos[0]}")
          print("-"*65)
        case "2":
            mes=input("Ingrese el mes que desea buscar(01-12): ")
            encontrados= fechaIngreso(mes)
            print("-"*65)
            print(f"Turistas ingresados el mes {mes.title()}: {len(encontrados)} encontrados")
            for numeroID, datos in encontrados:
                print(f"Nombre: {datos[0]} | Fecha ingreso: {datos[2]}")
            print("-"*65)
        case "3":
            print(f"Lista de turistas: {datos[0]}")







