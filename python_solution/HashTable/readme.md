# Hash Table

This is a data structure which establishes <key, value> pairs to retrieve value through key. **Hash table** is an array which stores values and the indexes of array is the result of **hash function** to key. By hash talbe, we could insert and retrieve items in O(1) time complexity.

## Hash function

Because of that the range of array is usually much less than the range of key, so some keys may have the same hash table index. We call this phenomenon **collision**.Hence, a good hash function could decrease the chance of collision and is efficiently computable.

## Collision Handling

When collision occurs, we usually use three skills to handle it.

1. **Open	addressing**. Just store or find the element one by one starting from the collision index until the index associated with the desired value is found.
2. **Chaining**. The hash table stores a linked list which contains pointers pointed to desired value. Keys sharing with the same index have pointers in the same linked list.