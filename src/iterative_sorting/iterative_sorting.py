import time


# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
            # TO-DO: swap

        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
        # temp = arr[i]
        # arr[i] = arr[smallest_index]
        # arr[smallest_index] = temp

    return arr


print(selection_sort([5, 6, 8, 5, 2, 7, 1]))

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    for i in range(len(arr), 0, -1):
        max_index = i
        for j in range(i):
            if arr[j] > arr[max_index - 1]:
                arr[j], arr[max_index - 1] = arr[max_index - 1], arr[j]
                # temp = arr[j]
                # arr[j] = arr[max_index - 1]
                # arr[max_index - 1] = temp

    return arr


# def bubble_sort(arr):
#     for i in range(0, len(arr)):
#         max_index = i
#         for j in range(i):
#             if arr[j] > arr[max_index]:
#                 temp = arr[j]
#                 arr[j] = arr[max_index]
#                 arr[max_index] = temp

#     return arr


print(bubble_sort([5, 6, 8, 5, 2, 7, 1, 12, 14, 20, 9, 9]))


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
