## Title
Print Middle Element(s) after Sorting / 排序后打印中间元素

## Description
**English**:  
You are given N integers. Sort them in ascending order.  
- If N is 0, print nothing.  
- If N is odd, print the single middle element in the sorted list.  
- If N is even, print the two middle elements in the sorted list on one line separated by a space.


给定 N 个整数，将它们从小到大排序，并根据以下规则输出：  
- 如果 N = 0，则不输出任何内容。  
- 如果 N 为奇数，则输出排序后列表中的中间元素。  
- 如果 N 为偶数，则输出排序后列表中的两个中间元素，并用空格分隔。

## Input Description
**English**:  
- The first line contains an integer N (0 <= N <= 100).  
- The next N lines each contain one integer.

- 输入的第一行是一个整数 N (0 <= N <= 100)。  
- 接下来的 N 行中，每行包含一个整数。

## Output Description
**English**:  
- If N=0, print nothing.  
- If N is odd, print the single middle element.  
- If N is even, print the two middle elements separated by a space.
 
- 如果 N=0，则不输出任何内容。  
- 如果 N 为奇数，则输出一个中间元素。  
- 如果 N 为偶数，则输出两个中间元素，用空格分隔。

## Input Samples
**English Example**:  
```
5
1
3
2
10
8
```
**Explanation**:  
- After sorting: 1, 2, 3, 8, 10  
- N=5 (odd), the middle is the 3rd element (index 2, 0-based) → 3  

**中文示例**:  
```
5
1
3
2
10
8
```
**说明**:  
- 排序结果：1, 2, 3, 8, 10  
- N=5 (奇数)，中间元素是第 3 个 (从 0 开始索引为 2) → 3  

## Output Samples
**English / 中文**:  
```
3
```

---

## Test Cases (Hidden to Students)

**Test Case 1**  
- Input:
```
4
10
5
2
2
```
- Sorted order: 2, 2, 5, 10  
- N=4 (even), so the two middle elements are the 2nd and 3rd elements (2, 5).  
- Output:
```
2 5
```

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
3
-1
100
50
```
- Sorted order: -1, 50, 100  
- N=3 (odd), middle element is the 2nd element (50).  
- Output:
```
50
  ```