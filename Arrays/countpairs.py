import numpy as np

#Time complexity - O(n2)
def countpairs(arr, ans):
    count = 0
    pairs = []
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == ans:
                count += 1
                pairs.append([arr[i], arr[j]])
    
    return pairs, count

#Time complexity
# def count_pairs_slidingwindow(arr, ans):
#     start = 0
#     current_sum = arr[0]
#     for i in range(1, len(arr)):
#         current_sum = current_sum + arr[i]
#         if current_sum > ans:
#              current_sum = current_sum - arr[i]
#              start += 1
#         if current_sum == sum:
#             return start, i-1

#Time complexity -  O(n) 
#Hashing
def countpairs_hash(arr, ans):
    unordered_map = {}
    count = 0
    pairs = []
    for i in range(0, len(arr)):
        if ans-arr[i] in unordered_map:
            count += unordered_map[ans - arr[i]]
            pairs.append([arr[i], ans - arr[i]])
        if arr[i] in unordered_map:
            unordered_map[arr[i]] += 1
        else:
            unordered_map[arr[i]] = 1
            
    return pairs, count
        

if __name__ == "__main__":
    arr = [1, 5, 7, -2, -1, 8, 9]
    ans = 6
    print(countpairs_hash(arr, ans))