import matplotlib.pyplot as plt
from die import Die
import pygal
die_1 = Die(8)
die_2 = Die(8)

x_values = [die_1.roll() for roll_num in range(1000)]
y_values = [die_2.roll() for roll_num in range(1000)]
plt.scatter(x_values, y_values, c=x_values, cmap=plt.cm.Blues, s=40)

#设置图表标题并给坐标轴加上标签
plt.title("Dice Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.show()

# 设置刻度标记的大小
# plt.axis([0, 1100, 0, 1100000])

# plt.savefig('squares_plot.png', bbox_inches='tight')
