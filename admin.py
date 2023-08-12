import json

class Admin:
    def __init__(self):
        self.food_id=0
        self.food_item={}

    def add_new_food(self):
        self.food_id+=1
        name=input("Enter food name : ")
        qty=int(input("Enter food qty : "))
        stock=int(input("Enter Stock : "))
        price=float(input("Enter Price : "))
        dis=float(input("Enter dis : "))
        food_item={"Food Name":name,"Food Qty":qty,"Stock":stock,"Price":price,"Discount":price - ((price*dis)/100 )}
        self.food_item[self.food_id]=food_item
        with open("food_item.json","w") as f:
            json.dump(self.food_item,f,indent=4)
        print("Food Item Added successfully...")
    

    def Edit_food_items(self):
        with open("food_item.json","r") as f:
            data=json.load(f)
        for k,v in data.items():
            print(f"food id :{k}  food item: {v}")
        id=input("Enter the food id for edit : ")
        item=input("Enter the food name for edit : ")
        update_value=input("Enter the update value : ")
        data[id][item] = update_value
        with open("food_item.json","w") as f:
            json.dump("food_item.json",f,indent=4)
        print("food item update successfully..")
        return data
    
    def show_food_items(self):
        with open("food_item.json","r") as f:
            data=json.load(f)
        for k,v in data.items():
            print(f"food id : {k}  ||  food item {v}")

    def remove_food_items(self):
        with open("food_item.json","r") as f:
            data=json.load(f)
        for k,v in data.items():
            print(f"food id : {k}  ||  food item {v}  ")
        id=input("Enter the food id for delete...")
        del data[id]
        with open("food_item.json","w") as f:
            json.dump(data,f,indent=4)
        print("food item update successfully..")
        return data
