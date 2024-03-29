from die import Die
import pygal

# 创建两个D6
die_1 = Die()
die_2 = Die()
die_3 = Die()

# 掷几次骰子，并将结果存储在一个列表中
# results = []
# for roll_num in range(50000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)

results = [die_1.roll() + die_2.roll() + die_3.roll() for roll_num in range(1000)]

print(results)

# 分析结果

max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
# for value in range(2, max_result + 1):
#     frequency = results.count(value)
#     frequencies.append(frequency)

frequencies = [results.count(value) for value in range(3, max_result + 1)]

print(frequencies)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling three D6 dice 1000 times"
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.x_labels = list(range(3, max_result + 1))
hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('three_dice_visual.svg')