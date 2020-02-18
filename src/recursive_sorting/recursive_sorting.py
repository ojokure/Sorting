# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    merged_arr = []

    # TO-DO
    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] < arrB[0]:
            sort = arrA.pop(0)
        else:
            sort = arrB.pop(0)

        # merged_arr.pop(0)
        merged_arr.append(sort)

    merged_arr += arrA
    merged_arr += arrB

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr

    pivot = len(arr) // 2
    arrA = merge_sort(arr[:pivot])
    print(arrA)
    arrB = merge_sort(arr[pivot:])
    print(arrB)

    arr = merge(arrA, arrB)

    return arr


print(merge_sort([5, 6, 8, 5, 2, 7, 1, 12, 14, 20, 9, 9]))


# STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr


# def merge_sort_in_place(arr, l, r):
#     # TO-DO

#     return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort(arr):

#     return arr
