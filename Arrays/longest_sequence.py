
#Time complexity - O(NlogN)
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    
    return quicksort(left) + [pivot] + quicksort(right)

def longestseq(arr):
    if not arr:
        return None
    
    sorted_arr = quicksort(arr)
    long_seq = 1
    
    for i in range(1, len(sorted_arr)):
        if sorted_arr[i] == sorted_arr[i-1] + 1:
            long_seq += 1
    
    return long_seq

if __name__ == "__main__":
    arr = [100,4,5,200,7,1,6]
    print(longestseq(arr))