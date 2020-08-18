# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []
    
    indexA = 0
    indexB = 0

    while indexA < len(arrA) and indexB < len(arrB):
        if arrA[indexA] < arrB[indexB]:
            merged_arr.append(arrA[indexA])
            indexA += 1
        else:
            merged_arr.append(arrB[indexB])
            indexB += 1
    
    # add the remaining elements
    merged_arr.extend(arrA[indexA:])
    merged_arr.extend(arrB[indexB:])
    
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass