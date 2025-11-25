import datetime


inventory=[({"title":"Alicia del universo","author":"loren","category":"fantasia","price":60000,"quantity_in_stock":10,
    "title":"Gatuno","author":"fern","category":"Terror","price":80000,"quantity_in_stock":5,
    "title":"este oeste del universo","author":"saeh","category":"Misterio","price":50000,"quantity_in_stock":7,
    "title":"Abeja nadadora","author":"nastina","category":"fantasia","price":20000,"quantity_in_stock":8,
    "title":"Hacia un nuevo mundo","author":"limeash","category":"ROmantico","price":90000,"quantity_in_stock":12}
    )]

#INVENTORY MANAGEMENT
def register():
    print("---Register product---")
    while True:

        title=input("Enter the product title: ")
        if title != "":
            break
        print("The title cannot be left empty")
    while True:
        author=input("I:Enter the product author ")
        if author != "":
            break
        print("The author cannot remain empty.")
    while True:
        try:
            opciones=input(("Categories:\n Fantasy\n Action\n Horror\n Comedy\n Romance\n Mystery\n "))
            category=(input("CWhat is the category?: "))
            if category != "":  
                break
            print("The category cannot be left empty.")                 
        except Exception:
            print("Error: You can only enter letters")
    while True:
        try:
            price=int(input("Enter the price: "))
            if price != "":
                break
            print("The price cannot be left emptyo")
        except Exception:
            print("Error: You can only enter numbers")
    while True:
        try:
            
            quantity_in_stock=int(input("Enter the amount: "))
            if quantity_in_stock != "":
                break
            print("The quantity cannot be left empty.")
        except Exception:
            print("Error: You can only enter numbers")

#Create a product dictionary
    product={
    "title":title,
    "author":author,
    "category":category,
    "price":float(price),
    "quantity_in_stock":int(quantity_in_stock),
}
    inventory.append(product)
    print("Product added successfully")

    return title, author, category, price, quantity_in_stock

def consult():
    print("---View Product---")
    title_cosult=input("Enter the title of the product you wish to inquire about.: ")
    found= False

    for prod in inventory:
        if prod["title"].lower() == title_cosult.lower():
            print("\n---View product---")
            print(f"Title: {prod['title']}")
            print(f"Author: {prod['author']}")
            print(f"Category: {prod['category']}")
            print(f"Price: {prod['price']}")
            print(f"Quantity_in_stock: {prod['quantity_in_stock']}")
            found =True
            break
    if not found:
        print("Product not found. \n")

def update(inventory):
    print("---Update product---")
    title_look_for=input("Enter the product title:" \
    "")
    found=False
    for prod in inventory:
        if prod["title"].lower() == title_look_for.lower():
            print("Product found")

            new_author=int(input("Enter new author: "))
            new_category=int(input("Enter the new category: "))
            new_price=int(input("Enter the new price: "))
            new_quantity_in_stock=int(input("Enter the new amount: "))

            #Actualizar los datos
            prod["author"]=new_author
            prod["category"]=new_category
            prod["price"]=new_price
            prod["quantity_in_stock"]=new_quantity_in_stock

            print("It updated successfully")
            found=True
            break
    if not found:
        print("The product was not found.")

def remove_product():
    print("---Remove Product---")
    remove_title=input("Enter the title of the product to be deleted:" \
    "")
    found=False
    for prod in inventory:
        if prod["title"].lower() == remove_title.lower():
            inventory.remove(prod)
            print("Product successfully removed")
            found= True
            break
    if not found:
        print("The product was not found")

#SALES REGISTRATION AND INQUIRY
def sales_inquiry():
    while True:
        print("Customer type is:")
        print("Associated")
        print("Not associated")
        option=input("Select an option (A/N): ").lower()
        if option == "a":
            register()
            
            break
        elif option == "n":
            print("You cannot register sales")
    
    while True:
    
        product_sold=input("What product did he/she sell?: ")
        if product_sold != "":
            break
        print("The product box cannot be empty.")
    
    while True:
        try:
            quantity=int(input("Enter the amount: "))
            if quantity >=0:
                break
            print("The box must not be left empty.")
        except Exception:
            print("Error: You should only enter numbers")
    while True:
        try:
            date=int(input("Enter the date: "))
            if date != "":
                break
            print("The box must not be left empty.")
        except Exception:
            print("Error: You should only enter numbers")

    while True:
        try:
            discount=input("Discount applies (Y/N)").lower()
            if discount == "s":
                for prod in inventory:
                    process= prod["price"]*0.10
                    total= prod["price"]-process
                    print(f"The discount is {total}")
                    break
            else:
                print("It does not have a discount.")
        except Exception:
            print("Error: You can only type letters")
            
        


#Validate stock (in progress)
def stock():
    while True:


                quantity_in_stocks=50
                total= quantity_in_stocks- inventory["quantity_in_stock"]
                
                inventory["quantity_in_stock"]=total
                print(f"the stock quantity is {inventory["quantity_in_stock"]}")

#REPORTS MODULE
def best_selling_producto():
    #top
    print("---best_selling_producto---")
    print("1. Fantasy")
    print("2. Action")
    print("3. Comedy")
























