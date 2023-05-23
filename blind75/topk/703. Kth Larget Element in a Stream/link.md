## 703. Kth Largest Element in a Stream ([URL](https://leetcode.com/problems/kth-largest-element-in-a-stream/))

Design a class to find the `k<sup>th</sup>` largest element in a stream. Note that ir is the `k<sup>th</sup>` largest element in the sorted order, not the `k<sup>th</sup>` distinct element.

Implement `KthLargest` class:

- `KthLargest(int k, int[] nums)` initializes the object with the integer `k` and the stream of integers `nums`.
- `int add(int val)` appends the integer `val` to the stream and returns the element representing the `k<sup>th</sup>` largest element in the stream.

It is guaranteed that there will be at least `k` elements in the array when you search for the `k<sup>th</sup>` element.
It is guaranteed that $-10^4\le val\le 10^4$.
