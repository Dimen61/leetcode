[**Binary search**](https://en.wikipedia.org/wiki/Binary_search_algorithm), a simple idea, but needs subtle implement. The idea is simple that we only search the target in the range where target could possible occurs.

The normal situation is that we search the target in the sorted array. If the array's order is uncomfortable for that way, we could binary search the value in the value range.

The keys of binary search:

* when to end the search or sure the search must stop
* determine the range where the target possible occurs
* If we want to find the last element in the orderd, duplicated array, we need to implement subtly.