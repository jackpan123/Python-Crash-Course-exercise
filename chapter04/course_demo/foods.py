my_foods = ['pizza', 'falafel', 'carrot', 'cake']
#friend_foods = my_foods[:]

friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
print(friend_foods)
for food in friend_foods:
    print(food)

print("The first three items in the list are:")
for food in my_foods[:3]:
    print(food)

print("Three items from the middle of the list are:")
for food in my_foods[1:4]:
    print(food)

print("The last three items in the list are:")
for food in my_foods[-3:]:
    print(food)