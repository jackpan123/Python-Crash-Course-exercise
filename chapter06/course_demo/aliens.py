# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

# 创建一个用于存储外星人的空列表
aliens = []

# 创建30个绿色外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for number in range(3):
    alien_0 = aliens[number]
    if alien_0['color'] == 'green':
        alien_0['color'] = 'yellow'
        alien_0['speed'] = 'medium'
        alien_0['points'] = 10

# 显示前五个外星人
for alien in aliens[0:5]:
    print(alien)
print("...")

# 显示创建了多少个外形人
print("Total number of aliens: " + str(len(aliens)))