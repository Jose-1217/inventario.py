
data_base = []

def pedirNumero(msg, tipo):
    terminate = True
    while terminate:
        try:
            if tipo == "int":
                pedir = int(input(msg))
            elif tipo == "float":
                pedir = float(input(msg))
            
            if pedir < 0:
                print("ENTER POSITIVE NUMBER")
                continue

            return pedir

        except ValueError:
            print("Opcion  invalido")
def menu():
    print("\n--- PRODUCT MANAGEMENT MENU ---")
    print("1. Add product")
    print("2. Show products")
    print("3. Search product")
    print("4. Update product")
    print("5. Delete product")
    print("6. Statistics")
    print("7. Exit")
    try:
        return int(input("ENTER AN OPTION (1-7): "))
    except ValueError:
        return 0

def add_product():
    # Corregido: El input debe pedir el dato al usuario
    producto = input("PRODUCT NAME: ")
    precio = pedirNumero(input(f"ADD PRICE FOR {producto}: "))
    cantidad = pedirNumero(input(f"AMOUNT OF {producto}: "))
    nueva_lista = [producto, precio, cantidad]
    data_base.append(nueva_lista)
    print("Product added successfully!")

def show_product():
    if not data_base:
        print("\nThe database is empty.")
        return
    print("\n--- INVENTORY ---")
    for product, price, amount in data_base:
        print(f"PRODUCT: {product} | PRICE: ${price} | QTY: {amount} | TOTAL: ${amount * price}")

def product_search():
    search = input("Enter product name to search: ")
    for p in data_base:
        if p[0].lower() == search.lower():
            print(f"\nFOUND: Name: {p[0]}, Price: {p[1]}, Amount: {p[2]}")
            return
    print("Product not found.")

def product_update():
    # Una actualización simple: borra el viejo y pide el nuevo
    search = input("Name of the product to update: ")
    for p in data_base:
        if p[0].lower() == search.lower():
            data_base.remove(p)
            print("Enter new data:")
            add_product()
            return
    print("Product not found.")

def product_delete():
    name = input("Name of product to remove: ")
    for p in data_base:
        if p[0].lower() == name.lower():
            data_base.remove(p)
            print("Product removed.")
            return
    print("Product not found.")

def calculate_statistics():
    if not data_base:
        print("No data available.")
        return
    valorgeneral = 0
    print("\n--- STATISTICS ---")
    for product, price, amount in data_base:
        total_producto = amount * price
        valorgeneral += total_producto
        print(f"{product}: ${total_producto}")
    print(f"------------------------------------")
    print(f"TOTAL GENERAL VALUE: ${valorgeneral}")
def main():
    
    while True:
      
        option = menu()
        if option == 1: add_product()
        elif option == 2: show_product()
        elif option == 3: product_search()
        elif option == 4: product_update()
        elif option == 5: product_delete()
        elif option == 6: calculate_statistics()
        elif option == 7:
            print("Program finished.")
            break
        else:
            print("Invalid option, try again.")


main()
