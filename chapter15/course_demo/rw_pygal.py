import pygal

from random_walk import RandomWalk

# 创建一个RandomWalk实例，并将其包含的点都绘制出来
# rw = RandomWalk()
# rw.fill_walk()
# plt.scatter(rw.x_values, rw.y_values, s=15)

# plt.show()

# 只要程序处于活动状态，就不断的模拟随机漫步

# 创建一个RandomWalk实例，并将其包含的点都绘制出来
rw = RandomWalk(1000)
rw.fill_walk()

# points_numbers = list(range(rw.num_points))

hist = pygal.Bar()
hist.title = "Results of run walk 1000 times"
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.x_labels = rw.x_values
hist.add('run walk', rw.y_values)
hist.render_to_file('run_walk_visual.svg')


   
