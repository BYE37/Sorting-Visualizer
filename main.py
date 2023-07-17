import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from matplotlib.widgets import Button

amount_nums = 200
# Generate random data, and create global variables shared between all functions
global arr
global anim
arr = np.random.randint(1, 30, amount_nums)

# Bubble sort algorithm
def bubbleSort(arr_copy):
    n = len(arr_copy)
    for i in range(0, n):
        yield arr_copy.copy()
        for j in range(0, n - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
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
    global arr
    arr_sorted = sorted(arr)
    for rect, val in zip(bars, frame):
        rect.set_height(val)

    if all(frame[i] == arr_sorted[i] for i in range(len(frame) - 1)):
        for rect, val in zip(bars, frame):
            rect.set_color('lime')
    return bars

fig, ax = plt.subplots()
ax.bar(range(len(arr)), arr, color = "black")
ax.title.set_text("Unsorted Array")

def bubble_sort_show(event):
    global arr
    global anim
    try:
        anim.event_source.stop()
    except:
        print('animation is not running')
    finally:
        ax.clear()
        bubble_sort_bars = ax.bar(range(len(arr)), arr, color = "black")
        ax.title.set_text("Bubble Sort")
        anim = FuncAnimation(fig, update_fig, frames=bubbleSort(arr.copy()), fargs=(bubble_sort_bars,), interval=20, repeat=False, blit=True, save_count=amount_nums)

def insertion_sort_show(event):
    global arr
    global anim
    try:
        anim.event_source.stop()
    except:
        print('animation is not running')
    finally:
        ax.clear()
        insertion_sort_bars = ax.bar(range(len(arr)), arr, color = "black")
        ax.title.set_text("Insertion Sort")
        anim = FuncAnimation(fig, update_fig, frames=insertionSort(arr.copy()), fargs=(insertion_sort_bars,), interval=20, repeat=False, blit=True, save_count=amount_nums)
        plt.show()

def merge_sort_show(event):
    global arr
    global anim
    try:
        anim.event_source.stop()
    except:
        print('animation is not running')
    finally:
        ax.clear()
        merge_sort_bars = ax.bar(range(len(arr)), arr, color = "black")
        ax.title.set_text("Merge Sort")
        anim = FuncAnimation(fig, update_fig, frames=mergesort(arr.copy(), 0, amount_nums - 1), fargs=(merge_sort_bars,), interval=20, repeat=False, blit=True, save_count=amount_nums)
        plt.show()

def unsorted_array_show(event):
    global arr
    global anim
    try:
        anim.event_source.stop()
    except:
        print('animation is not running')
    finally:
        ax.clear()
        unsorted_array_bars = ax.bar(range(len(arr)), arr, color = "black")
        ax.title.set_text("Unsorted Array")
        anim = FuncAnimation(fig, update_fig, frames=[arr], fargs=(unsorted_array_bars,), interval=1, repeat=False, blit=True)
        plt.show()

def randomize(event):
    global arr
    arr = np.random.randint(1, 30, amount_nums)
    ax.clear()
    unsorted_array_show(None)

button_unsorted = plt.axes([0.02, 0.01, 0.15, 0.05])
button_unsorted_array = Button(button_unsorted, 'Unsorted Array')
button_unsorted_array.on_clicked(unsorted_array_show)

button_bubble = plt.axes([0.2, 0.01, 0.15, 0.05])
button_bubble_sort = Button(button_bubble, 'Bubble Sort')
button_bubble_sort.on_clicked(bubble_sort_show)

button_insertion = plt.axes([0.4, 0.01, 0.17, 0.05])
button_insertion_sort = Button(button_insertion, 'Insertion Sort')
button_insertion_sort.on_clicked(insertion_sort_show)

button_merge = plt.axes([0.6, 0.01, 0.15, 0.05])
button_merge_sort = Button(button_merge, 'Merge Sort')
button_merge_sort.on_clicked(merge_sort_show)

button_random = plt.axes([0.8, 0.01, 0.20, 0.05])
button_randomize = Button(button_random, 'Generate New Array')
button_randomize.on_clicked(randomize)

plt.show()