## Title
Sort Even Numbers First, Then Odd Numbers / 先偶后奇排序

## Description
**English**:  
You are given N integers. You must sort them such that all **even** numbers come first (in ascending order) and all **odd** numbers come after (also in ascending order). Then print all the integers in a single line separated by spaces. If N = 0, print nothing.
 
给定 N 个整数，需要将所有**偶数**排在前面（从小到大排序），然后将所有**奇数**排在后面（从小到大排序），最后将结果用空格分隔输出在同一行。如果 N=0，则不输出任何内容。

## Input Description
**English**:  
- The first line contains an integer N (0 <= N <= 100).  
- The next N lines each contain one integer.


- 输入的第一行是一个整数 N (0 <= N <= 100)。  
- 接下来的 N 行中，每行包含一个整数。

## Output Description
**English**:  
Print the sorted integers in one line, with even numbers in ascending order first, followed by odd numbers in ascending order. Separate numbers with a space. If N=0, print nothing.


在同一行按顺序输出排序后的整数：先输出偶数（从小到大），再输出奇数（从小到大），用空格分隔。如果 N=0，则不输出任何内容。

## Input Samples
**English Example**:
```
5
4
7
2
9
10
```
**Explanation**:  
- Even numbers are: 2, 4, 10 (in ascending order: 2, 4, 10)  
- Odd numbers are: 7, 9 (in ascending order: 7, 9)  
- Final output: `2 4 10 7 9`

**中文示例**:
```
5
4
7
2
9
10
```
**说明**:  
- 偶数: 2, 4, 10（升序为 2, 4, 10）  
- 奇数: 7, 9（升序为 7, 9）  
- 输出: `2 4 10 7 9`

## Output Samples
**English / 中文**:
```
2 4 10 7 9
```

---

## Test Cases (Hidden to Students)

**Test Case 1**  
- Input:
```
3
2
2
1
```
- Even numbers: 2, 2 → sorted: 2, 2  
- Odd numbers: 1 → sorted: 1  
- Final: `2 2 1`  
- Output:
```
2 2 1
```

**Test Case 2**  
- Input:
```
0
```
- Output: *(no output)*

**Test Case 3**  
- Input:
```
5
-4
-3
0
1
2
```
- Even numbers: -4, 0, 2 → sorted ascending: -4, 0, 2  
- Odd numbers: -3, 1 → sorted ascending: -3, 1  
- Final: `-4 0 2 -3 1`  
- Output:
```
-4 0 2 -3 1
```

## Solution
