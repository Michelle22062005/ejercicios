from inventory_management import(register, consult,update,remove_product,inventory,sales_inquiry,best_selling_producto)

def menu_principal():
    while True:
        print("---Inventory Menu---")
        
        print("1. Register product")
        print("2. View product")
        print("3. Update product")
        print("4. Remove product")
        print("5. top 3")

        option=input("Seleciona una opcion (1-4): ")
        if option == "1":
            sales_inquiry()
            return menu_principal()
        elif option == "2":
            consult()
        elif option == "3":
            update(inventory)
        elif option == "4":
            remove_product(inventory)
        elif option == "5":
            best_selling_producto()
        else:
            print("Opcion invalida, intente nuevamente")
menu_principal()
