#Lista para almacenar productos
inventario = []

#Funciones
def agregar_producto ():
    """Pide los datos y los guarda en un diccionario dentro de la lista """
    print("\n Registro de producto")
    nombre = str(input("nombre: "))
    # Usamos un bucle interno para que no salga hasta que ponga un número válido
    precio_valido = False
    while precio_valido == False:
        try:
            # Intentamos convertir la entrada a decimal
            precio = float(input("Precio (usa números): "))
            # Si llega aquí, es que no hubo error
            precio_valido = True 
        except ValueError:
            # Si el usuario puso letras, se ejecuta esto:
            print("Error: Debes digitar un numero para el precio.")
    #Hacemos lo mismo para la cantidad
    cantidad_valida = False
    while cantidad_valida == False:
        try:
            cantidad = int(input("Cantidad (usa números enteros): "))
            cantidad_valida = True
        except ValueError:
            print("Error: La cantidad debe ser un número entero.")

    #Creamos el diccionasrio
    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)
    print(f"{nombre} producto agregado")

def mostrar_inventario ():
    """Recorre el inventario con un bucle for"""
    print("\n Inventario completo")
    if len(inventario) == 0:
        print("el inventario esta vacío")
    else:
        for p in inventario:
            print(f"producto: {p['nombre']} precio: {p['precio']} cantidad: {p['cantidad']}")

def calcular_estadisticas ():
    """calcula unidades y total de dinero"""
    total_valor = 0
    total_productos = 0
    for p in inventario:
        total_valor += p["precio"] * p["cantidad"]
        total_productos += p["cantidad"]

    print(f"valor total: {total_valor}")
    print(f"productos totales: {total_productos}")

#Menu principal con variable de control
def ejecutar_menu():
    continuar = True
    while continuar == True:
        print("\n menu")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadisticas")
        print("4. Salir")

        opcion = input("elija una opcion: ")

        #Procesar informacion con condicionales
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            calcular_estadisticas()
        elif opcion == "4":
            print("Adios")
            #Cambiamos la variable para que el bucle termine
            continuar = False
        else:
            print("Opcion invalida, intentelo otra vez")

#iniciamos el programa
ejecutar_menu()
