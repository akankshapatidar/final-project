food={}
FoodID = len(food) + 1
admin_database={}
user_database={}
ordered_item=[]

def admin_registration():
    email = input("\nEnter your email ID for registering with the app: ")
    passord = input("Enter your password ID for registering with the app: ")
    
    admin_database["email"] = email
    password_database["password"] = password
    
    print("Admin registration is done Successfully!")
    
    
def admin_login():
    email = input("Enter your email ID to login: ")
    password = input("Enter your password: ")
    
    if bool(admin_database):
        if admin_database["email"] == email and admin_database["password"] == password:
            admin_functionalities()
        else:
            print("\nPlease check your credentials and try again")
    else:
        print("\nAdmin need to register first\n")
        
        
def admin_functionalities():   
    print("Hello Admin! What would you like to do?")
    while True:
        try:
            options = int(input("\n1.Add Food Items\n2.Edit Food Items\n3.Viwe Food Items\n4.Remove Food Items \n5.Exit\n:"))
            
            if options == 1:
                add-food_item()
                
            elif options == 2:
                edit_food_item()
                
            elif options == 3:
                viwe_food_item()   
            elif options == 4:
                remove_food_item()
            elif options == 5:
                break
                
            else:
                print("Select from the available option")
        except ValueError:
                print("Please enter valid input")
                
def add_food_item():
    try:
        name = input("\nEnter tha name of the food to add: ")
        quantity = float(input("Enter the quantity value: "))
        price = float(input("Enter the price in INR: "))
        discount = float(input("How much discount: "))
        stock = float(input("Stock left: "))
        
        food_list = {
            "Name": name,
            "Quantity": quantity,
            "Price": price,
            "Discount": discount,
            "Stock": stock,
        }
        FoodID = len(food) + 1

        food[FoodID] = food_list
        
        print("\nFood items been added successfully.")
    except ValueError:
        print("\nPlease re-check your input & try again.")
        
def edit_food_item():
    
    try:
        FoodID = len(food) + 1 

        while FoodID > 1:

            id = int(input("Enter the FoodID you want to update the food of:"))
            if id in food.keys():
                update_val = int(input("\nWhat would you like to update: \n1.Food Name\n2.Quantity\n3.Price\n4.Discount\n5.Stock: \n"))

                if update_val == 1:
                    food[id]["Name"] = input("Update the food name: ")
                    print("Food Name updated successfully")
                    break

                elif update_val == 2:
                    food[id]["Quantity"] = float(input("Update the quantity of the food: "))
                    print("Food Quantity updated successfully")
                    break
                    
                elif update_val == 3:
                    food[id]["Price"] = float(input("update food's price: "))
                    print("Food Price updated successfully")
                    break

                elif update_val == 4:
                    food[id]["Discount"] = float(input("Update food's discount: "))
                    print("Food Discount value updated successfully")
                    break

                elif update_val == 5:
                    food[id]["Stock"] = float(input("Update food's stock value: "))
                    print("Food Stock value updated successfully")
                    break

                else:
                    print("Please select from the available options")
                    break
                    
            else:
                print(f"\n{id} ID doesn't exist.")
                break
        else:
            print("\nCurrently the food items is empty. Add items first then try again.")

    except ValueError:
        print("Enter the valid input")   
        
        
        
def view_food_item():
    print("\nFollowing is the current food items we have: ")
    if len(food)>0:    
        for id in food:
            print(f"Food Id : {id}")
            for items in food[id]:
                print(f"{items} : {food[id][items]}")
            print()
    else:
        print("\nFood items is currently empty\n")
        
        
        
def remove_food_item():
    try:
        id = int(input("\nEnter the FoodID to remove its food items: "))
        if id in food:
            food.pop(id)
            print(f"\nFood item with ID:{id} is deleted successfully!")
        else:
            print(f"\nFoodID:{id} doesn't exist.")
    except ValueError:
        print("\nPlease enter a valid input.")      
        
        
        
        
def admin():

    print("\nHello Admin!!")
    while True:
        try:
            options = int(input("\nPlease select from the following options:\n1.Registration\n2.Login\n3.Exit\n:"))
            if options == 1:
                admin_registration()
            elif options == 2:
                admin_login()
            elif options == 3:
                break
            else:
                print("\nPlease enter from the available options.\n")
        except ValueError:
            print("\nEnter valid input to continue")
            
            
            
            
            
def user_registration():
    try:
        full_name = input("Enter your full name: ")
        phone_number = int(input("Enter your phone number(10 digit): "))
        email = input("Enter your email ID: ")
        address = input("Enter your address: ")
        password = input("Enter your password: ")

        user_database["full_name"] = full_name
        user_database["phone_number"] = phone_number
        user_database["email"] = email
        user_database["address"] = address
        user_database["password"] = password

        print("User registration is done Successfully!")
    except ValueError:
        print("Please enter valid input")

    for i in user_database:
        print(f"{i}: {user_database[i]}")
        
        
        
        
        
        
def user_login():
    email = input("Enter your email ID to login: ")
    password = input("Enter your password: ")

    if bool(user_database):
        if user_database["email"] == email and user_database["password"] == password:
            print("Welcome User")
            user_functionalities()
        else:
            print("\nPlease check your credentials and try again")
    else:
        print("\nUser need to register first\n")
        
        
        
        
        
        
def user_functionalities():
    print("Hello User! What would you like to do?")

    while True:
        try:
            options = int(input("\n1.Place New Order\n2.Order History\n3.Update Profile\n4.Exit\n:"))

            if options == 1:
                place_new_order()

            elif options == 2:
                order_history()

            elif options == 3:
                update_profile()
            
            elif options == 4: 
                break

            else:
                print("Select valid option")
        except ValueError:
            print("Please enter valid input")
            
            
            
            
            
def place_new_order():
    try:
        if len(food)>0:

            print("Following is the current menu we offer: ")
            menu=[]
            for id in food:
                menu.append([food[id]["Name"], food[id]["Quantity"], food[id]["Price"]]) 
            for i in range(len(menu)):
                print(f"{i+1}. {menu[i]}")

            while True:
                options = int(input("\n1.Order\n2.Go Back\n:"))

               
                if options == 1:
                    food_order = input("Enter the number of the food you want to order separated by comma: ").split(",")
                    
                    for i in food_order:
                        food_list = int(i)
                        print(food_list)
                        if food_list <= len(menu):
                            ordered_item.append(menu[food_list-1])
                        else:
                            print(f"\nThe opted food item {food_list} is not available")
                            
                            print("\nFollowing is the food items selected : \n")
                    for food_selected in ordered_item:
                        print(food_selected)

                elif options == 2:
                    break
                else:
                    print("Please enter valid option")
            
        else:
            print("\nFood menu is currently empty\n")
    except ValueError:
        print("Please enter valid input")
        
        
        
        
        
def order_history():

    if len(ordered_item)>0:
            print("\nHere is the list of ordered food so far: \n")
            for item in ordered_item:
                print(item)
    else:
        print("\nThere is no Ordered History!!")
        
        
        
def update_profile():
    for i in user_database:
         print(f"{i}: {user_database[i]}")

    while True:
    
        try:
            print("What would you like to update from the options below: ")
            options = int(input("\n1.Name\n2.Phone Number\n3.Email ID\n4.Password\n5.Address\n6.GO BACK\n:"))

            if options == 1:
                user_database["full_name"] = input("Enter your updated full name: ")
                print("\nName updated successfully\n")

            elif options == 2:
                user_database["phone_number"] = input("Enter your updated phone number: ")
                print("\Phone Number updated successfully\n")

            elif options == 3:
                user_database["email"] = input("Enter your updated email: ")
                print("\nEmail updated successfully\n")

            elif options == 4:
                user_database["password"] = input("Enter your updated password: ")
                print("\Password updated successfully\n")
                
            elif options == 5:
                user_database["address"] = input("Enter your updated address: ")
                print("\nAddress updated successfully\n")
                
            elif options == 6: 
                break

            else:
                print("\nPlease choose from the available options")
        except ValueError:
            print("\nPlease enter a valid input")
            
            
            
def user():
    print("\nHello User!!")

    while True:

        try:
            options = int(input("\nPlease select from the following options:\n1.Registration\n2.Login\n3.Exit\n:"))
            if options == 1:
                user_registration()

            elif options == 2:
                user_login()

            elif options == 3:
                break

            else:
                print("\nEnter from the available options\n")

        except ValueError:
            print("Please enter valid input")
            
            
            
def main():
    print("Welcome to the Aakanksha's store\n")

    while True:
        try:
            options = int(input("Please select from the following options:\n1.Admin\n2.User\n3.Exit\n:"))
            if options == 1:
                admin()
            elif options == 2:
                user()
            elif options == 3:
                break
            else:
                print("\nEnter from the available options.\n")
        except ValueError:
            print("\nEnter valid options to proceed with the app\n")


if __name__=="__main__":
    main()

print("Thank you for visiting Aakanksha's store!")
