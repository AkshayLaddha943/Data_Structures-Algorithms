def movezeroes(arr):
    j = len(arr) - 1
    for i in range(0, len(arr)):
        if i>= j:
            break
        if arr[i] == 0:
            if arr[j] == 0:  # Look for the rightmost non-zero element
                j -= 1
            if j > i:
                arr[i], arr[j] = arr[j], arr[i]
                j = j-1
    return arr

def movezeroes_new(arr):
    j = 0
    for i in range(0, len(arr)):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr

if __name__ == "__main__":
    print(movezeroes_new([1, 2, 0, 0, 3, 0, 6, 7, 2, 0]))