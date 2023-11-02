class Restaurant:
    def __init__(self):
        self.menu = []
        self.customers = {}

    def add_food_item(self, food_item):
        self.menu.append(food_item)

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def view_customer_carts(self, restaurant_instance):
        print("Customers and their carts:")
        for username, customer in restaurant_instance.customers.items():
            print(f"{username}'s Cart:")
            customer.view_cart()
            print("Oga patapata ni seh")

class Fooditem:
    def __init__(self,name,price):
        self.name=name
        self.price=price
class customer:
    def __init__(self,name,username,password):
        self.username = username
        self.password= password
        self.cart= []
    def add_to_cart(self,food_item):
        self.cart.append(food_item)
    def view_cart(self):
        for item in self.cart:
            print(f"{item.name}:#{item.price}")
class restaurant:
    def __init__(self):
        self.menu =[]
        self.customers={}
    def add_food_item(self,food_item):
        self.menu.append(food_item)
restaurant_instance = Restaurant()

food_item1 = Fooditem("Jollof_Rice", 150.91)
food_item2 = Fooditem("Fried_Rice", 100.90)
food_item3 = Fooditem("Salad", 150.95)
food_item4 = Fooditem("Egusi", 4.99)
food_item5 = Fooditem("pounded_yam", 12.99)
food_item6 = Fooditem("Snail", 20.5)




restaurant_instance.add_food_item(food_item1)
restaurant_instance.add_food_item(food_item2)
restaurant_instance.add_food_item(food_item3)
restaurant_instance.add_food_item(food_item4)
restaurant_instance.add_food_item(food_item5)
restaurant_instance.add_food_item(food_item6)


halaga = {}

admin_instance = Admin("oyebaba", "1234")
app_on = True
while app_on:
    print("Welcome to Halaga Foods,what would you like to do?")
    todo = input("Todo(signup, login, admin,close):")
    if todo =='signup':
        name = input("Name:")
        username=input("Enter your username:")
        passw =input("Enter your password:")
        while username in restaurant_instance.customers:
            print(f"Username {username} has been taken.")
            username = input("Enter a different username: ")
        else:
            new_customer = customer(name, username, passw)
            restaurant_instance.customers[username] = new_customer
           # restaurant_instance.customers[username] = customer(name, username, passw)
            print(f"{username} account created successfully.")


    elif todo=='login':
        username = input("Username:")
        passw = input("password:")
        if username in restaurant_instance.customers and passw == restaurant_instance.customers[username].password:
            current_user = restaurant_instance.customers[username]
            print("Welcome", current_user.username)
            while True:
                action = input("Choose an action (menu, cart, logout): ")

                if action == 'menu':
                    print("Menu:")
                    for item in restaurant_instance.menu:
                        print(f"{item.name}: #{item.price}")

                    item_name = input("Enter the name of the food to add to your cart (or type 'done' to finish): ")
                    while item_name.lower() != 'done':
                        for item in restaurant_instance.menu:
                            if item.name == item_name:
                                current_user.add_to_cart(item)
                                print(f"{item.name} added to your cart.")
                                break
                        else:
                            print("Item not found in the menu.")

                        item_name = input("Enter the name of the food to add to your cart (or type 'done' to finish): ")

                elif action == 'cart':
                    print("Your Cart:")
                    current_user.view_cart()

                elif action == 'logout':
                    print(" Thank You For Choosing Halaga Foods, Logged out Successfully.")
                    break


                else:
                    print("Invalid action. Please choose 'menu', 'cart', or 'logout'.")

    elif todo == 'admin':
        admin_username = input("Admin Username: ")
        admin_passw = input("Admin Password: ")

        if admin_username == admin_instance.username and admin_passw == admin_instance.password:
            admin_instance.view_customer_carts(restaurant_instance)
        else:
            print("Invalid admin credentials.")