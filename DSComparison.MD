1. Arrays vs LinkedLists - 
** Linked lists are preferable over arrays when ** :
 - you need constant-time insertions/deletions from the list (such as in real-time computing where time predictability is absolutely critical)
 - you don't know how many items will be in the list. With arrays, you may need to re-declare and copy memory if the array grows too big
 - you don't need random access to any elements
 - you want to be able to insert items in the middle of the list (such as a priority queue)

** Arrays are preferable when **:
 - you need indexed/random access to elements
 - you know the number of elements in the array ahead of time so that you can allocate the correct amount of memory for the array
 - you need speed when iterating through all the elements in sequence. You can use pointer math on the array to access each element, whereas you need to lookup the node based on the pointer for each element in linked list, which may result in page faults which may result in performance hits.
 - memory is a concern. Filled arrays take up less memory than linked lists. Each element in the array is just the data. Each linked list node requires the data as well as one (or more) pointers to the other elements in the linked list.

Arrays allocate a fixed-size, contiguous block of memory at compile time, providing efficient indexing for direct access to elements. Linked lists, on the other hand, allocate memory dynamically at runtime, allowing for flexible size adjustments. While arrays excel in fast element access and are ideal for scenarios where size remains constant, linked lists shine in dynamic data scenarios, enabling efficient insertion and deletion operations. However, linked lists consume more memory due to node overhead, and their elements are interdependent, making them less suitable for scenarios where direct element access is crucial


2. Heaps


3. Stacks
- Linear Data Structure
- LIFO order
- real life eg: reversing or stack of clothes

4. Queue
- Linear data structure
- Data ended at rear end and removed from front (FIFO)
- used when users want to hold an item for longer time, 
- job/disk scheduling
- When data is transferred asynchronously between two processes.The queue is used for synchronization. For example: IO Buffers, pipes, file IO, etc
- Handling of interrupts in real-time systems.

5. LinkedLists
- linear data structure that includes a series of connected nodes. Here, each node stores the data and the address of the next node. 

6. Set vs List
- 
