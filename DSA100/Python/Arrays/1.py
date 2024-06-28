def arr_prod(arr):
    pref = [1] * len(arr)
    suf = [1] * len(arr)
    
    for i in range(0, len(arr)):
        pref[i] = pref[i-1] * arr[i-1]
    
    for i in range(n-2, -1, -1):
        suf[i] = suf[i + 1] * arr[i + 1]
    
    answer = [pref[i] * suf[i] for i in range(len(arr))]

if __name__ == "__main__":
    arr = [1,2,4,6]
    