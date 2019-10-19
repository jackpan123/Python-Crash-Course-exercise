pizzas = ['培根披萨', '奥尔良鸡肉披萨', '牛肉披萨']
for pizza in pizzas:
    print("I like " + pizza + ".")
print("I really love pizza")

friend_pizzas = pizzas[:]

pizzas.append('扇贝披萨')
friend_pizzas.append('鱿鱼披萨')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

print(pizza)