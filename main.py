import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from matplotlib.widgets import Button

amount_nums = 50

# Generate random data
arr = np.random.randint(0, 50, amount_nums)
arr_sorted = sorted(arr)

# Create subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
bubble_sort_bars = ax1.bar(range(len(arr)), arr)
ax1.title.set_text("Bubble Sort")

insertion_sort_bars = ax2.bar(range(len(arr)), arr)
ax2.title.set_text("Insertion Sort")

merge_sort_bars = ax3.bar(range(len(arr)), arr)
ax3.title.set_text("Merge Sort")

# Bubble sort algorithm
def bubbleSort(arr_copy):
    n = len(arr_copy)
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
            yield arr_copy.copy()
        yield arr_copy.copy()
    yield arr_copy.copy()

# Insertion sort algorithim
def insertionSort(arr_copy):
    arr_copy
    n = len(arr_copy)
    for step in range(1, n):
        key = arr_copy[step]
        j = step - 1
              
        while j >= 0 and key < arr_copy[j]:
            arr_copy[j + 1] = arr_copy[j]
            j = j - 1
            yield arr_copy.copy()

        arr_copy[j + 1] = key
        yield arr_copy.copy()

# function to recursively divide the arra
def mergesort(arr_copy, start, end):
    if end <= start:
        return
  
    mid = start + ((end - start + 1) // 2) - 1
      
    # yield from statements have been used to yield 
    # the array from the functions 
    yield from mergesort(arr_copy, start, mid)
    yield from mergesort(arr_copy, mid + 1, end)
    yield from merge(arr_copy, start, mid, end)
  
# function to merge the array
def merge(arr_copy, start, mid, end):
    merged = []
    leftIdx = start
    rightIdx = mid + 1
  
    while leftIdx <= mid and rightIdx <= end:
        if arr_copy[leftIdx] < arr_copy[rightIdx]:
            merged.append(arr_copy[leftIdx])
            leftIdx += 1
        else:
            merged.append(arr_copy[rightIdx])
            rightIdx += 1
  
    while leftIdx <= mid:
        merged.append(arr_copy[leftIdx])
        leftIdx += 1
  
    while rightIdx <= end:
        merged.append(arr_copy[rightIdx])
        rightIdx += 1
  
    for i in range(len(merged)):
        arr_copy[start + i] = merged[i]
        yield arr_copy


# Update figure function
def update_fig(frame, bars):
    for rect, val in zip(bars, frame):
        rect.set_height(val)

    if all(frame[i] == arr_sorted[i] for i in range(len(frame) - 1)):
        for rect, val in zip(bars, frame):
            rect.set_color('green')
    return bars

anim1 = FuncAnimation(fig, update_fig, frames=bubbleSort(arr.copy()), fargs=(bubble_sort_bars,), interval=20, repeat=False, blit=True, save_count=amount_nums)
anim2 = FuncAnimation(fig, update_fig, frames=insertionSort(arr.copy()), fargs=(insertion_sort_bars,), interval=20, repeat=False, blit=True, save_count=amount_nums)
anim3 = FuncAnimation(fig, update_fig, frames=mergesort(arr.copy(), 0, amount_nums - 1), fargs=(merge_sort_bars,), interval=20, repeat=False, blit=True, save_count=amount_nums)

def pause(event):
    try:
        anim1.event_source.stop()
        anim2.event_source.stop()
        anim3.event_source.stop()
    except:
        print("One or more animations is done running")
        

def start(event):
    try:
        anim1.event_source.start()
        anim2.event_source.start()
        anim3.event_source.start()
    except:
        print("One or more animations is done running")
 

axpause = fig.add_axes([0.87, 0.0, 0.1, 0.05])
button_pause = Button(axpause, 'Pause')
button_pause.on_clicked(pause)

axstart = fig.add_axes([0.75, 0.0, 0.1, 0.05])
button_start = Button(axstart, 'Start')
button_start.on_clicked(start)

plt.show()