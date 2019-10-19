sandwich_orders = ['tuna sandwich', 'pastrami', 'chicken sandwich', 'pastrami', 'tomato sandwich', 'pastrami']
print("pastrami sell out")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

