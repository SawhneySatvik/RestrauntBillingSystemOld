import pickle


admin_pass = "helloworld"


start_page = """Welcome to our restaurant management system!\nPlease choose one of the following options to proceed:\n
[A] Admin panel: View & edit the menu, past orders and customers!
[M] Menu: View & order our specialties!
[Q] Quit
"""


admin_page = """\nWelcome to the admin panel!\nPlease choose one of the following options to proceed:\n
[M] Menu: View & edit the restaurant menu.
[F] Food items: View & edit the food items available.
[O] Orders: View previous orders & bills.
[C] Customers: View all customers.
[P] Password: Edit & update the password for the admin panel.
[B] Back to main menu
"""


menu_page = """\nWelcome to our Menu!"""


admin_menu_page = """Do you want to edit the menu?\nPlease choose one of the following options to proceed:\n
[A] Add: Add a food item to the menu.
[R] Remove: Remove a food item from the menu.
[B] Back to the admin panel
"""


admin_food_item_page = """Do you want to edit the food items?\nPlease choose one of the following options to proceed:\n
[C] Create: Create a new food item.
[E] Edit: Edit an existing food item.
[R] Remove: Remove an existing food item.
[B] Back to the admin panel
"""


# name, price, desc, special, spicy, egg
menu = [1, 2, 3]
orders = {}
food = {1: ["Chicken Momos", 150, "6 fresh Chicken Momos served with Red Chilli Chutney.", True, True, False],
       2: ["Chicken Tacos", 200, "3 tacos in flour tortillas with pico, avocado, Jack cheese, jalapeño aioli, cilantro, queso fresco. Served with Mexican rice & black beans.", False, True, False],
       3: ["Molten Chocolate Cake", 100, "Warm chocolate cake with chocolate fudge filling. Served without ice cream.", True, False, True]}
data = {'menu': menu, 'orders': orders, 'food': food}


def init():
   global data, menu, orders, food
   with open('data.dat', 'rb+') as F:
       try:
           file_data = pickle.load(F)
           data = file_data
           menu = data['menu']
           orders = data['orders']
           food = data['food']
       except:
           pickle.dump(data, F)


def update():
   global data
   data['menu'] = menu
   data['orders'] = orders
   data['food'] = food
   with open('data.dat', 'wb+') as F:
       pickle.dump(data, F)


def admin_menu_add():
   print("\nHere are all the food items:")
   display_all_food_items()
   add_index = int(input("Enter the item number of the food item to be added: "))
   if add_index in menu:
       print("The food item is already present in the menu.")
   else:
       if add_index in food:
           menu.append(add_index)
           print("Food item added!")
       else:
           print("Invalid item number.")
   return 0


def admin_menu_remove():
   remove_index = int(input("Enter the item number of the food item to be removed: "))
   if remove_index in menu:
       menu.remove(remove_index)
       print("Food item removed!")
   else:
       print("Invalid item number.")
   return 0


def admin_menu():
   print("Here is the current menu:")
   display_menu()
   while True:
       print(admin_menu_page)
       choice = input("Enter your choice: ").upper()
       if choice == 'A':
           admin_menu_add()
       elif choice == 'R':
           admin_menu_remove()
       elif choice == 'B':
           return 0
       else:
           print("\nPlease choose only one of A/R/B.\n")


def admin_create_food_item():
   food_item_arr = []
   food_item_arr.append(input("Enter the name of the food item: "))
   food_item_arr.append(int(input("Enter the price of the food item in rupees: ")))
   food_item_arr.append(input("Enter the description of the food item: "))
   choice = input("Is the food item a Chef's special? [Y - Yes, N - No]: ").upper()
   food_item_arr.append((choice == 'Y'))
   choice = input("Is the food item spicy? [Y - Yes, N - No]: ").upper()
   food_item_arr.append((choice == 'Y'))
   choice = input("Does the food item contain egg? [Y - Yes, N - No]: ").upper()
   food_item_arr.append((choice == 'Y'))
   food[len(food)+1] = food_item_arr
   print("\nFood item added!\n")
   return 0


def admin_edit_food_item():
   item = int(input("Enter the item number of the food item to be edited: "))
   if item in food:
       print("Here is the current food item: ")
       display_food_item(food[item])
       print("Please enter the following information: ")
       food_item_arr = []
       food_item_arr.append(input("Enter the name of the food item: "))
       food_item_arr.append(int(input("Enter the price of the food item in rupees: ")))
       food_item_arr.append(input("Enter the description of the food item: "))
       choice = input("Is the food item a Chef's special? [Y - Yes, N - No]: ").upper()
       food_item_arr.append((choice == 'Y'))
       choice = input("Is the food item spicy? [Y - Yes, N - No]: ").upper()
       food_item_arr.append((choice == 'Y'))
       choice = input("Does the food item contain egg? [Y - Yes, N - No]: ").upper()
       food_item_arr.append((choice == 'Y'))
       food[item] = food_item_arr
       print("\nFood item updated!\n")
   else:
       print("Invalid item number.")
   return 0


def admin_remove_food_item():
   item = int(input("Enter the item number of the food item to be removed: "))
   if item in menu:
       menu.remove(item)
   if item in food:
       food.pop(item)
       print("\nFood item removed!\n")
   else:
       print("Invalid item number.")
   return 0


def admin_fooditems():
   print("\nHere are all the existing food items:")
   display_all_food_items()
   while True:
       print(admin_food_item_page)
       choice = input("Enter your choice: ").upper()
       if choice == 'C':
           admin_create_food_item()
       elif choice == 'E':
           admin_edit_food_item()
       elif choice == 'R':
           admin_remove_food_item()
       elif choice == 'B':
           return 0
       else:
           print("\nPlease choose only one of C/E/R/B.\n")


def admin_orders():
   grand_grand_total = 0
   for order in orders:
       print("Order #" + str(order) + ":")
       generate_bill(orders[order])
       grand_grand_total += orders[order]["total"]
       print("\n")
   print("Number of orders:", len(orders))
   print("Total across all orders: ₹" + str(grand_grand_total))
   return 0


def admin_customers():
   all_customers = []
   for order in orders:
       if orders[order]["name"] not in all_customers:
           all_customers.append(orders[order]["name"])
   if len(all_customers) == 0:
       print("There are no customers!")
       return 0
   print("List of customers: ")
   curr = 1
   for customer in all_customers:
       print(str(curr) + ". " + customer)
       curr += 1
   return 0


def admin_password_reset():
   global admin_pass
   print("Current password is: " + admin_pass)
   new_pass = input("Enter new password: ")
   print("Your password has been reset")
   admin_pass = new_pass
   return 0


def admin_panel():
   while True:
       pass_in = input("Enter password for admin: ")
       if pass_in == admin_pass:
           break
       else:
           choice = input("\nSorry, that was incorrect. Do you want to try again? [Y: Yes, N: No]: ").upper()
           print()
           if choice == "Y":
               continue
           else:
               return
   while True:
       print(admin_page)
       choice = input("Enter your choice: ").upper()
       if choice == 'M':
           admin_menu()
           update()
       elif choice == 'F':
           admin_fooditems()
           update()
       elif choice == 'O':
           admin_orders()
           update()
       elif choice == 'C':
           admin_customers()
           update()
       elif choice == 'P':
           admin_password_reset()
           update()
       elif choice == 'B':
           return 0
       else:
           print("\nPlease choose only one of M/F/O/C/P/B.\n")


def display_food_item(food_item):
   print("["+str(food_item)+"]", food[food_item][0], end=" ")
   if food[food_item][3]:
       print("⭐", end=' ')
   if food[food_item][4]:
       print("🌶️", end=' ')
   if food[food_item][5]:
       print("🥚", end=' ')
   print()
   print(food[food_item][2])
   print("Cost: ₹" + str(food[food_item][1]))
   print()
  
def display_all_food_items():
   print("Number of food items:", len(food))
   print()
   for food_item in food:
       display_food_item(food_item)
   print("⭐ : Chef's special.")
   print("🌶️ : Contains spice.")
   print("🥚 : Contains egg.")
   print()
   return 0


def display_menu():
   print("Number of items in our menu:", len(menu))
   print()
   for food_item in menu:
       display_food_item(food_item)
   print("⭐ : Chef's special.")
   print("🌶️ : Contains spice.")
   print("🥚 : Contains egg.")
   print()
   return 0


def generate_bill(order):
   print("-"*60)
   print("Name:", order["name"])
   print("Mobile Number:", order["number"])
   print("-"*60)
   curr = 1
   for item in order["order"]:
       print(str(curr) + ". " + str(food[item[0]][0]) + ":  " + str(item[1]) + " serving(s) worth ₹" + str(item[1]*food[item[0]][1]))
       curr += 1
   print("-"*60)
   print("Grand Total: ₹" + str(order["total"]))
   print("-"*60)
   return 0


def take_order():
   order_spec = {}
   name = input("Please enter your name: ")
   mobile_no = int(input("Please enter your mobile number: "))
   counter = {}
   for item in menu:
       counter[item] = 0
   order_spec["name"] = name
   order_spec["number"] = mobile_no
   order_spec["order"] = []
   total = 0
   while True:
       while True:
           item = int(input("Enter the item you wish to order: "))
           if item in menu:
               break
           else:
               print("That item is not available in our menu, please try again.")
       quantity = int(input("Enter the desired quantity: "))
       if quantity == 1:
           print(str(quantity) + " serving of " + food[item][0] + " has been added.")
       else:
           print(str(quantity) + " servings of " + food[item][0] + " have been added.")
       total += quantity*food[item][1]
       print("Order total is now ₹" + str(total))
       print()
       counter[item] += quantity
       more = False
       while True:
           choice = input("Do you want to add more items? [Y - Yes, N - No]: ").upper()
           if choice == 'Y':
               more = True
               break
           elif choice == 'N':
               more = False
               break
           else:
               print("\nPlease choose only one of Y/N.\n")
       if not more:
           break
   for x in counter:
       if counter[x] != 0:
           order_spec["order"].append([x, counter[x]])
   order_spec["total"] = total
   orders[len(orders)+1] = order_spec
   print("\nYour order has been placed! Here is your bill: ")
   generate_bill(order_spec)
   return 0


def menu_panel():
   print(menu_page)
   display_menu()
   while True:
       choice = input("Do you want to place an order? [Y - Yes, N - No]: ").upper()
       if choice == 'Y':
           break
       elif choice == 'N':
           return 0
       else:
           print("\nPlease choose only one of Y/N.\n")
   take_order()
   print("Thank you!\n")


while True:
   init()
   print(start_page)
   choice = input("Enter your choice: ").upper()
   if choice == 'A':
       admin_panel()
       update()
   elif choice == 'M':
       menu_panel()
       update()
   elif choice == 'Q':
       break
   else:
       print("\nPlease choose only one of A/M/Q.\n")
