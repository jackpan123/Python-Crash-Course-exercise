age = 11

if age < 2:
    stage = 'baby'
elif age < 4:
    stage = 'big baby'
elif age < 13:
    stage = 'child'
elif age < 20:
    stage = 'teens'
elif age < 65:
    stage = 'adult'
else:
    stage = 'elderly'

print("He is a " + stage + ".")