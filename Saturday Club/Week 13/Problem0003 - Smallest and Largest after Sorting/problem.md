## Title
Smallest and Largest after Sorting / 排序后最小值与最大值

## Description
**English**:  
You are given N integers. Sort them in ascending order. Then print the **smallest** integer and the **largest** integer on a single line separated by a space. If there are no integers (N = 0), print nothing. If there is only one integer (N = 1), both the smallest and largest are the same, so print that integer twice (separated by a space).
 
给定 N 个整数，将它们从小到大排序，然后在同一行输出最小值和最大值，两者之间用空格分隔。如果没有任何整数 (N=0)，则不输出任何内容。如果只有一个整数 (N=1)，最小值和最大值相同，因此需输出这个整数两次（用空格分隔）。

## Input Description
**English**:  
- The first line contains an integer N (0 <= N <= 100).  
- The next N lines each contain one integer.

- 输入的第一行是一个整数 N (0 <= N <= 100)。  
- 接下来的 N 行中，每行包含一个整数。

## Output Description
**English**:  
- If N = 0, print nothing.  
- Otherwise, after sorting in ascending order, print the smallest integer and the largest integer, separated by a space.  
- If N = 1, print the single integer twice.  
  
- 如果 N = 0，则不输出任何内容。  
- 如果 N >= 1，在从小到大排序之后，输出最小值和最大值，用空格分隔。  
- 如果 N = 1，则将该整数打印两次。

## Input Samples
**English Example**:  
```
5
2
5
3
3
1
```
**Explanation**:  
- Sorted order: 1, 2, 3, 3, 5  
- Smallest = 1, Largest = 5  

**中文示例**:  
```
5
2
5
3
3
1
```
**说明**:  
- 排序结果：1, 2, 3, 3, 5  
- 最小值 = 1，最大值 = 5  

## Output Samples
**English / 中文**:  
```
1 5
```

---

## Test Cases (Hidden to Students)

**Test Case 1**  
- Input:
```
1
7
```
- Output:
```
7 7
```
*(One integer, so print it twice.)*

**Test Case 2**  
- Input:
```
0
```
- Output:
*(no output)*

**Test Case 3**  
- Input:
```
4
10
10
-1
5
```
- Output:
```
-1 10
```
*(Sorted: -1, 5, 10, 10. Smallest=-1, Largest=10.)*

## Solution

