#Time complexity: O(n)
def minmaxarr(arr):
    min = arr[0]
    max = arr[0]
    
    for i in range(len(arr)):
        if (arr[i] < min):
            min = arr[i]
        
        if (arr[i] > max):
            max = arr[i]
        
    return min, max

#Time complexity: 

if __name__ == "__main__":
    print(minmaxarr([1,4,6,2,7,23,9]))