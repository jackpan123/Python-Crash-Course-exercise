sandwich_orders = ['tuna sandwich', 'chicken sandwich', 'tomato sandwich']
finished_sandwich = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich)
    finished_sandwich.append(sandwich)

print(finished_sandwich)