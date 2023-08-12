import json
class User:
    def __init__(self):
        self.personal_details={}
        self.order_item = {}

    def register(self):
        name=input("Enter Name : ")
        phone_number=input("Enter Phone Number : ")
        address=input("Enter Address details : ")
        self.email=input("Enter Yor mail id : ")
        self.password=input("Enter Password : ")
        user_details={"Name":name,"Phone_number":phone_number,"Address":address,"Email":self.email,"Password":self.password}
        self.personal_details[self.email]=user_details
        with open ("personal_details.json","w") as f:
            json.dump(self.personal_details,f,indent=4)
        print("Congralution you Registerd Successfully...")
        return self.personal_details
    
    def login(self):
        print("Welcome to login page..")
        with open("personal_details.json","r") as f:
            data = json.load(f)
    
        email=input("Enter mail id:")
        password=input("Enter Password: ")
        if email in data:
            if password==data[email]["Password"]:
                return True
            else:
                return False
        else:
            return False

    def place_order(self):
        order_id = 0
        order_id = order_id+1
        self.order_food_items=[]
        list_of_foods= [{"name":"Tandoori chicken","Quantity":"4 Pieces","Price":240},
                       {"name":"Vegan Burger","Quantity":"1 Pieces","Price":320},
                       {"name":"Truffle Cake","Quantity":"500gm","Price":900}]
                       
        print("Menu Page : ")
        for i in list_of_foods:
            print(i)

        user_input=int(input("Select food for order: "))
        if user_input==0:
            self.order_food_items.append(list_of_foods[0])

        elif user_input==1:
            self.order_food_items.append(list_of_foods[1])
        elif user_input==2:
            self.order_food_items.append(list_of_foods[2])

        else:
            print("Choose the time from the menu..")

        print("Press 1 for order confirmation:")
        print("Press 2 for Order Delection:")

        option=int(input("Enter yor Choice"))
        self.order_item[order_id] = self.order_food_items
        if option==1:
            print("Order Successfully..")
            with open("order_history.json", "w") as f:
                json.dump(self.order_item,f,indent=4)
        else:
            print("Order Cancelled")
            return self.order_item
        
    def order_history(self):
        for k,v in self.order_item.items():
            print(f"Order_id : {k} || Order_details : {v}")

    def Edit_profile(self):
        with open ("personal_details.json","r") as f:
            data=json.load(f)

        for k,v in data.items():
            print(f"user mail id : {k} ||  user deatils : {v}")
        
        mail_id=input("Enter the User mail id which you want to update : ")
        field=input("Enter the field you want to update : ")
        update_value=input("Enter Update value : ")
        data[mail_id][field]=update_value
        with open ("personal_deatils","w") as f:
            json.dump(data,f,indent=4)
        return data
        

# x=User()
# x.register()
# x.login()
# x.place_order()
# x.order_history()
# x.edit_profile()