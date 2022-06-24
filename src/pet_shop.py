# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_name):
    return pet_name["name"]

def get_total_cash(admin_cash):
    cash = admin_cash["admin"]["total_cash"]
    return cash

def add_or_remove_cash(admin_cash, money):
    admin_cash["admin"]["total_cash"] += money

def get_pets_sold(sold):
    return sold["admin"]["pets_sold"]

def increase_pets_sold(more_pets, sold):
    more_pets["admin"]["pets_sold"] += sold

def get_stock_count(pet_stock):
    return len(pet_stock["pets"])

def get_pets_by_breed(shop, pet_breed):
    count = []
    for pet in shop["pets"]:
        if pet["breed"] == pet_breed:
            count.append(pet["name"])
    return count

def find_pet_by_name(shop, pet_name):
    for right_name in shop["pets"]:
        if right_name["name"] == pet_name:
            return right_name

def remove_pet_by_name(shop, remove_pet):
    for gone_pet in shop["pets"]:
        if gone_pet["name"] == remove_pet:
            shop["pets"].remove(gone_pet)

def add_pet_to_stock(shop, new_pet):
    shop["pets"].append(new_pet)

def get_customer_cash(customer_total):
        if customer_total["cash"] == 1000:
            return customer_total["cash"]

def remove_customer_cash(customer,less_cash):
    customer["cash"] -= less_cash

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)
    return len(customer["pets"])

def customer_can_afford_pet(customer, new_pet_value):
    return customer["cash"] >=  new_pet_value["price"] 

def sell_pet_to_customer(shop, pet, customer):
    customer["pets"].append(pet)
    shop["admin"]["pets_sold"] += 1
    customer["cash"] -= pet["price"]
    

    


