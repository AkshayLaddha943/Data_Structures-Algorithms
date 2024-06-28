def arrayoccurence(arr, n):
    count = {}
    
    for i in range(len(arr)):
        if arr[i] in count:
            count[arr[i]] += 1
        else:
            count[arr[i]] = 1
    
    for key, val in count.items():
        if key == n:
            print(val)


if __name__ == "__main__":
    arrayoccurence([1,2,2,3,5,5,5,6,7,6,6,1], 5)