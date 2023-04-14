import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font_path = "SourceHanSansCN-Regular.otf"
font = FontProperties(fname=font_path)
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

# 设置参数
num_intersections = 4
max_time = 200
noise_std = 1
arrivals = np.random.randint(0, 10, (num_intersections, max_time))

# 添加高斯噪音
arrivals = np.maximum(
    arrivals
    + np.random.normal(0, noise_std, (num_intersections, max_time)).astype(int),
    0,
)


def traffic_control(arrivals):
    green_time_range = (25, 35)
    red_time_range = (5, 15)
    light_states = np.zeros((num_intersections, max_time))
    waiting_times = np.zeros((num_intersections, max_time))

    for i in range(num_intersections):
        time = 0
        light_state = 1
        light_time = np.random.randint(*green_time_range)
        while time < max_time:
            if light_time == 0:
                light_state = 1 - light_state
                if light_state == 1:
                    light_time = np.random.randint(*green_time_range)
                else:
                    light_time = np.random.randint(*red_time_range)
            else:
                light_time -= 1

            throughput = min(arrivals[i, time], 10) if light_state == 1 else 0
            arrivals[i, time] = np.maximum(arrivals[i, time] - throughput, 0)
            arrivals[i, min(time + light_time, max_time - 1)] += throughput
            light_states[i, time] = light_state
            waiting_times[i, time] = arrivals[i, time]

            time += 1

    return arrivals, light_states, waiting_times


arrivals, light_states, waiting_times = traffic_control(arrivals)

# 绘制车辆通过时间图
for i in range(num_intersections):
    plt.plot(arrivals[i, :], label="Intersection {}".format(i + 1))
plt.legend()
plt.title("车辆通过时间", fontproperties=font)
plt.show()

# 绘制红绿灯状态图
for i in range(num_intersections):
    plt.plot(light_states[i, :], label="Intersection {}".format(i + 1))
plt.legend()
plt.title("红绿灯状态", fontproperties=font)
plt.show()

# 绘制车辆等待时间图
for i in range(num_intersections):
    plt.plot(waiting_times[i, :], label="Intersection {}".format(i + 1))
plt.legend()
plt.title("车辆等待时间", fontproperties=font)
plt.show()
