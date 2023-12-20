# 2706. Buy Two Chocolates

**Problem Statement:** https://leetcode.com/problems/buy-two-chocolates/description/?envType=daily-question&envId=2023-12-20

### Approach:
- Sort the array
- check the sum of first tow array elements are less than or equal to the `money`
- return the `money` if the condition **does not satisfy**, otherwise return `money - (prices[0] + prices[1])`

### Time Complexity: **O**(nlogn)
The most significant operation in your code is the sorting operation, which is done using Arrays.sort(prices). The time complexity of the sorting algorithm used by Arrays.sort is O(n log n), where n is the length of the array.

### Space Complexity: **O**(n)
The space complexity is determined by the auxiliary space used by the sorting algorithm. The Arrays.sort method typically uses a variant of merge sort or TimSort, both of which have a space complexity of O(n).