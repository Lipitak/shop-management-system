import json
# ye ek lhali list hai isme apn product ka data input krenge 
products = []
sales = []
def save_data():
    with open("data.json","w") as f:
         json.dump({"products":products,"sales":sales},f)

def load_data():
        global products, sales
        try:
                with open("data.json","r") as f:
                        data = json.load(f)
                        products = data["products"]
                        sales = data["sales"]
        except:
                pass
load_data()                
                
while True:
            print("WELCOME TO MY SHOP")
            print("\n1. add products")
            print("2. exit")
            print("3. view product")
            print("4. sell product")
            print("5. sales report")
            print("6. low stock alert")
            print("7. update price")
            choice = input("enter your choice")

            if choice == "1":
             name = input("enter the product name :")
             price = float(input("enter the product's price:"))
             quantity = int(input("enter the product's quantity"))
             found = False
             for product in products:
              if product[0] == name:
                  product[2] = product[2]+quantity
                  print("quantity is updated")
                  found = True
                  save_data()
                  break
             if found == False:
#append is function which will add proucts in the list 
              products.append([name,price,quantity])
              print("products added")
              save_data()
 # File se data load karta hai

            elif choice == "3":
                print("product list check",products)
                total_value = 0
                for product in products:
                    print(product)
                    if product[2]< 10:
                      print("low stock alert",product[0])
                    total_value = total_value + product[1]*product[2]
                print("total inventory value:",total_value)


            elif choice == "4":
                 sell_name = input("enter the sell product name")
                 sell_quantity = int(input("enter the quantity of sell product"))
                 found = False
                 for product in products:
                     if product[0] == sell_name:
                         found = True
                         if sell_quantity > product[2]:
                              print("stock not available")
                         else:    
                              total = product[1]*sell_quantity
                              print("total amount:",total)          
                              discount = float(input("how many % discount:"))
                              final = total - (total*discount/100)
                              print("final amount after discount:",final) 
                              product[2] = product[2]-sell_quantity 
                              sales.append([sell_name, sell_quantity, final]) 
                              save_data()
                              if product[2] < 10:
                                print("low stock alert",product[0])
                         break
                 if found == False:
                     print("product not found")


            elif choice == "5":
                  grand_total = 0
                  for sale in sales:
                      print(sale)
                      grand_total = grand_total+sale[2]
                  print("total kamai:",grand_total)


            elif choice == "6":
                  for product in products:
                      if product[2] < 10:
                         print("low stock products",product)


            elif choice == "7":
                  update_name = input("enter the product name whose price wanted to be updated:")
                  update_price = float(input("update the price:"))
                  for product in products:
                      if product[0] == update_name:
                          product[1] = update_price
                          print("new price is updated")
                          save_data()


            elif choice == "2":
                  print("thank you adding products")
                  break




