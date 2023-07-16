import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import numpy as np

amount_nums = 25

#Generate random data
arr = np.random.randint(0, 100, amount_nums)

#Create subplots:
fig, (ax1, ax2) = plt.subplots(1, 2)
bubble_sort_bars = ax1.bar(range(len(arr)), arr)
ax1.title.set_text("Bubble Sort")

#Bubble sort, if element is larger move it to the right
def bubble_sort():
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            yield arr.copy()

def update_fig(frame, bubble_sort_bars):
    for rect, val in zip(bubble_sort_bars, frame):
        rect.set_height(val)
    return bubble_sort_bars

anim = FuncAnimation(fig, update_fig, frames=bubble_sort, fargs=(bubble_sort_bars, ), interval=100, blit=True)

plt.show()