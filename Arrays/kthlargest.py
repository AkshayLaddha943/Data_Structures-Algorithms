  
import heapq
 
# Function to find the kth smallest array element
def kthSmallest(arr, K):
    # Create a max heap (priority queue)
    min_heap = []
 
    # Iterate through the array elements
    for num in arr:
        # Push the negative of the current element onto the max heap
        heapq.heappush(min_heap, num)
 
        # If the size of the max heap exceeds K, remove the largest element

    for _ in range(K - 1):
        heapq.heappop(min_heap)
 
    # Return the Kth smallest element (top of the max heap, negated)
    return min_heap[0]
 

if __name__ == "__main__":
    arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
    K = 4
 
    # Function call
    print("Kth Smallest Element is:", kthSmallest(arr, K))