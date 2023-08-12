from admin import *
from user import *
import sys

admin = Admin()
user = User()

print("Welcome to the Food Ordering App")
while True:
    print("Press 1 for Admin login ")
    print("Press 2 for User login")
    print("Press 3 for Exit")
    choice = int(input("Enter your choice : "))
    if choice==1:
        print("Welocme to Admin Login page....")
        print("Press 1 for Add Food Items")
        print("Press 2 for Edit Food Items")
        print("Press 3 for Show Food Items")
        print("Press 4 for Removing Food Items")
        option = int(input("Enter your choice : "))
        if option==1:
            admin.add_new_food()
        elif option==2:
            admin.Edit_food_items()
        elif option==3:
            admin.show_food_items()
        elif option==4:
            admin.remove_food_items()
        else:
            print("Please provide valid Input")
    elif choice==2:
        print("Welcome to User login...")
        print("Press 1 for Registration")
        print("Press 2 for login")
        choice=int(input("Enter your choice"))
        if choice==1:
            user.register()
        elif choice==2:
            temp = user.login()
            if temp:
                print("Press 1 for place order")
                print("press 2 for order history")
                print("press 3 for profile update")
                option = int(input("Enter your choice "))
                if option==1:
                    user.place_order()
                elif choice == 2:
                    user.order_history()
                elif choice==3:
                    user.Edit_profile()
                else:
                    print("please provide valid input")
            else:
                print("please provide valid credentials")
        else:
            print("please provide valid input")
    elif option==3:
        print("Thank you for using Application...")
        sys.exit()
    else:
        print("Please provide valid input")



