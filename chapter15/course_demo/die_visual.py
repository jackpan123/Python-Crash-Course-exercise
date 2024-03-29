from die import Die
import pygal

# 创建一个D6
die = Die()

# 掷几次骰子，并将结果存储在一个列表中
# results = []
# for roll_num in range(1000):
#     result = die.roll()
#     results.append(result)

results = [die.roll() for roll_num in range(1000)]

print(results)

# 分析结果
# frequencies = []
# for value in range(1, die.num_sides + 1):
#     frequency = results.count(value)
#     frequencies.append(frequency)

frequencies = [results.count(value) for value in range(1, die.num_sides + 1)]

print(frequencies)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.x_labels = list(range(1, die.num_sides + 1))
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')