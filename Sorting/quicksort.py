def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    
    return quicksort(left) + [pivot] + quicksort(right)

if __name__ == "__main__":
    arr = [5,3,9,12,98,56,789]
    print(quicksort(arr=arr))