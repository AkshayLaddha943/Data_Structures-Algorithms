#Time complexity: O(n)
def move_negative(arr):
    j = 0
    for i in range(len(arr)):
        while (arr[i] < 0):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j = j+1
    return arr


#Time complexity: O(n), two-pointer approach
# def move_negative_twopointer(arr, left, right):
#     while left <= right:
#         if (arr[left] < 0 and arr[right] < 0):
#             left +=1
        
#         else if (arr[left] > 0 and arr[right]) < 0:
#             arr[left], arr[right] = arr[right], arr[left]
        
#         else if ()

if __name__ == "__main__":
    arr = [1, 2, -4, -5, 3, -9, 6]
    print(move_negative(arr))
    