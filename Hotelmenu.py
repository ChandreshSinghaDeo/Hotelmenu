menu={"Pizza":40,
        "Pasta":50,
        "Burger":60,
        "Salad":70,
        "Cofee":80
}

print("Welcome to Restro")
print("Pizza:40\nPasta:50\nBurger:60\nSalad:70\nCofee:80")

Order_Total = 0
item_1 = str(input("Enter the name of item you want to order =" ))
if item_1 in menu:
    Order_Total+= menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"ordered item {item_1} is not available at the moment,Please add something from the above menu \nThank you for your understanding")

another_order= str(input("Do you want to add another item in this order? (Yes/No) "))
if another_order == "Yes":
    item_2 =str(input("Enter the name of second item you want to order="))
    if item_2 in menu:
        Order_Total +=menu [item_2]
        print(f"Your item {item_2} has been added to your order")
    else:
        print(f"ordered item {item_2} is not available at the moment,Please add sometime from the above menu \n Thank you for your understanding")
print(f"The total amount to pay is :",Order_Total)