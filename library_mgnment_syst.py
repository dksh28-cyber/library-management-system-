# Hotel Management System
'''
show full menu with prices for eg.
burger , fries , cold drinks (give ids : help in adding combos )
( with prices ) 
there should be a cart system:
def cart ( *n )
price * quantity [ use for loop here]
return sum items 
at last print Bill

'''
menu = {
    1: ["Burger", 80],
    2: ["Fries", 50],
    3: ["Cold Drink", 30],
    4: ["Combo (Burger + Fries + Drink)", 140]
}

print("menu : ")
for item_id in menu:
    item = menu[item_id]
    name = item[0]
    price = item[1]
    print(item_id, name,"name: ", "₹", price)

def cart(*items):
    total = 0
    print("cart : ")
    for item in items:
        item_id, quantity = item
        item_name = menu[item_id][0]
        item_price = menu[item_id][1]
        cost = item_price*quantity
        total += cost
        print(item_name, "x", quantity, "=", "₹", cost)
    return total

selected_items = []

while True:
    item_id = int(input("enter items to cart or 0 to exit"))
    
    if item_id == 0:
        if selected_items:
            total_bill = cart(*selected_items)
            print("total bill = ", total_bill) 
        exit()
    
    if item_id in menu:
        item_name = menu[item_id][0]
        quantity = int(input("Enter quantity for " + item_name + ": "))
        selected_items.append((item_id, quantity))
    else:
        print("Invalid item number.")