import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from matplotlib.widgets import Button

amount_nums = 50
# Generate random data, and create global variables shared between all functions
global arr
global anim
arr = np.random.randint(1, 30, amount_nums)

# Bubble sort algorithm
def bubbleSort(arr_copy):
    iterations = 0
    n = len(arr_copy)
    for i in range(0, n):
        yield arr_copy.copy()
        for j in range(0, n - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
            iterations += 1
            yield arr_copy.copy()
# Insertion sort algorithim
def insertionSort(arr_copy):
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
def mergeSort(arr_copy, start = 0, end = amount_nums - 1):
    if end <= start:
        return
  
    mid = start + ((end - start + 1) // 2) - 1
      
    # yield from statements have been used to yield 
    # the array from the functions 
    yield from mergeSort(arr_copy, start, mid)
    yield from mergeSort(arr_copy, mid + 1, end)
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

# Quick sort implementation
# quicksort function
def quickSort(a, l = 0, r = amount_nums - 1):
    if l >= r:
        return
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[j], a[i] = a[i], a[j]
        yield a
    a[l], a[j]= a[j], a[l]
    yield a
 
    # yield from statement used to yield
    # the array after dividing
    yield from quickSort(a, l, j-1)
    yield from quickSort(a, j + 1, r)

# Update figure function
def update_fig(frame, bars):
    arr_sorted = sorted(arr)
    for rect, val in zip(bars, frame):
        rect.set_height(val)
    if all(frame[i] == arr_sorted[i] for i in range(len(frame) - 1)):
        #set all bars to lime, rerender them
        bars = ax.bar(range(len(arr)), frame, color = "lime")
    return bars

fig, ax = plt.subplots()
#show type of sort
def sort_show(sort_type):
    iterations = np.array([0])
    global anim
    if anim is not None and anim.event_source is not None:
        anim.event_source.stop()

    ax.clear()
    if sort_type == "unsorted":
        #set the color to black
        bars = ax.bar(range(len(arr)), arr, color = "black")
        ax.title.set_text("Unsorted Array")
        anim = FuncAnimation(fig, update_fig, frames=[arr], fargs=(bars,), interval=1, repeat=False, blit=True)
    else:
        bars = ax.bar(range(len(arr)), arr, color = "red")
        if sort_type == "bubble":
            ax.title.set_text("Bubble Sort")
            anim = FuncAnimation(fig, update_fig, frames=bubbleSort(arr.copy()), fargs=(bars,), interval=20, repeat=False, blit=True, save_count=amount_nums)
        elif sort_type == "insertion":
            ax.title.set_text("Insertion Sort")
            anim = FuncAnimation(fig, update_fig, frames=insertionSort(arr.copy()), fargs=(bars,), interval=20, repeat=False, blit=True, save_count=amount_nums)
        elif sort_type == "merge":
            ax.title.set_text("Merge Sort")
            anim = FuncAnimation(fig, update_fig, frames=mergeSort(arr.copy()), fargs=(bars,), interval=20, repeat=False, blit=True, save_count=amount_nums)
        elif sort_type == "quick":
            ax.title.set_text("Quicksort")
            anim = FuncAnimation(fig, update_fig, frames=quickSort(arr.copy()), fargs=(bars,), interval=20, repeat=False, blit=True, save_count=amount_nums)
    plt.show()

def randomize(event):
    global arr
    arr = np.random.randint(1, 30, amount_nums)
    ax.clear()
    sort_show("unsorted")

ax_button_unsorted = plt.axes([0.05, 0.01, 0.15, 0.05])
button_unsorted_array = Button(ax_button_unsorted, 'Unsorted Array', 
                               hovercolor='lightgray')
button_unsorted_array.on_clicked(lambda event: sort_show("unsorted"))

ax_button_bubble = plt.axes([0.37, 0.01, 0.15, 0.05])
button_bubble_sort = Button(ax_button_bubble, 'Bubble Sort')
button_bubble_sort.on_clicked(lambda event: sort_show("bubble"))

ax_button_insertion = plt.axes([0.52, 0.01, 0.15, 0.05])
button_insertion_sort = Button(ax_button_insertion, 'Insertion Sort')
button_insertion_sort.on_clicked(lambda event: sort_show("insertion"))

ax_button_merge = plt.axes([0.67, 0.01, 0.15, 0.05])
button_merge_sort = Button(ax_button_merge, 'Merge Sort')
button_merge_sort.on_clicked(lambda event: sort_show("merge"))

ax_button_quick = plt.axes([0.82, 0.01, 0.15, 0.05])
button_quick_sort = Button(ax_button_quick, 'Quicksort')
button_quick_sort.on_clicked(lambda event: sort_show("quick"))


ax_button_random = plt.axes([0.20, 0.01, 0.15, 0.05])
button_randomize = Button(ax_button_random, 'Randomize Array')
button_randomize.on_clicked(randomize)

#to start, run the unsorted_array function (defualt menu)
anim = None
sort_show("unsorted")
plt.show()