def reverse_arr(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

def reverse_arr_stack(arr):
    stack = []
    for i in range(len(arr)):
        stack.append(arr[i])
    
    
    for i in range(len(arr)):
        arr[i] = stack.pop()
    
    return arr

if __name__ == "__main__":
    arr = [1, 6, 4, 8, 2, 3]
    print(reverse_arr(arr))