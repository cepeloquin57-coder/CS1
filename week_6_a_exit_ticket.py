order = {"drink":"Latte", "size":"Large", "price":5.50, "quantity":2}
print(f"The customer ordered a {order['drink']} in size {order['size']}.\n")

print(order.keys())
print(order.values(),f"\n")

for key in order.keys():
    print(f"{key}: {order[key]}")

order["drink"] = "Iced Coffee"
order["size"] = "Medium"
order["whipped_cream"] = "Yes"
order["flavor"] = "Vanilla"
#if asked for order[milk] using indexing, Python should return an error
#it does.
#when trying to get the 'milk' key with .get, python should return a nul result
print(order.get("milk"),"\n")
#it does!
order["flavor"] = "Caramel"
order["quantity"] = 3
order["pickup"] = "10:30 AM"
for key in order.keys():
    print(f"{key}: {order[key]}")