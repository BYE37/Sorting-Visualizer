import matplotlib.pyplot as plt
import numpy as np

amount_nums = 25

arr = np.random.randint(0, 100, amount_nums)
x = np.arange(0, amount_nums, 1)
n = len(arr)

#Bubble sort, if element is larger move it to the right
for i in range(0, n):
    for j in range(0, n-i-1):
        plt.bar(x, arr)
        plt.pause(0.01)
        plt.clf()
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

plt.show()
