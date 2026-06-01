
# ye ek lhali list hai isme apn product ka data input krenge 
products = []
sales = []
while True:
    print("WELCOME TO MY SHOP")
    print("\n1. add products")
    print("2. exit")
    print("3. view product")
    print("4. sell product")
    print("5. sales report")
    choice = input("enter your choice")

    if choice == "1":
        name = input("enter the product name :")
        price = float(input("enter the product's price:"))
        quantity = int(input("enter the product's quantity"))
#append is function which will add proucts in the list 
        products.append([name,price,quantity])
        print("products added")
    elif choice == "3":
        for product in products:
                 print(product)
    elif choice == "4":
         sell_name = input("enter the sell product name")
         sell_quantity = int(input("enter the quantity of sell product"))
         for product in products:
                if product[0] == sell_name:
                   total = product[1]*sell_quantity
                   print("total amount:",total) 
                   product[2] = product[2]-sell_quantity 
                   sales.append([sell_name, sell_quantity, total]) 
    elif choice == "5":
            grand_total = 0
            for sale in sales:
              print(sale)
              grand_total = grand_total+sale[2]
            print("total kamai:",grand_total)
    elif choice == "2":
            print("thank you adding products")
            break




