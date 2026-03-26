data_base = []
msg = ("opcion invalida")

def validacion (msg ,tipo) :
    seguir =True
    while seguir :
            try :
                if tipo == "int" :
                     
                      pedir =int (input(msg))
                elif tipo == "float":
                    pedir =float (input(msg))

                elif tipo  < 0 :
                     print ("DIGITE UN NUMERO POSITIVO")     
                else :
                    
                 return pedir

            except ValueError :
                 print (msg)            


def  costo_total () :
     valorgeneral = 0
     for producto, precio, cantidad in data_base:

            print (f"NOMBRE DEL PRODUCTO: {producto}")
            print ("------------------------------")
            print (f"PRECIO DEL PRODUCTO: {precio}")
            print ("-------------------------------")
            print (f"CANTIDAD DEL PRODUCTO: {cantidad}")
            print ("-------------------------------")
            print (f"Valor total : {cantidad * precio}")
            subtotal = cantidad * precio
            valorgeneral += subtotal
            
            print(f"EL VALOR GENERAL ES {valorgeneral}")      
                            

def inicio () :
  
     
    nombre = str(input("Ingresa el nombre del producto: " ))
    precio = float(input(f"Ingresa el precio {nombre} " ))
    cantidad = int(input(f"Ingresa la cantidad {nombre} "))
    return nombre , precio , cantidad, 

def menu () :
    print ("BIENVENIDOS")
    seguir = True
    while seguir :
          
        datos = inicio () 
      
        data_base.append (datos)
        opcion = input("¿Deseas agregar otro producto? (s/n): ").lower()
        if opcion == "n":
            seguir = False

    costo_total ()
         

menu ()
