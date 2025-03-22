## Title
Descending Sort / 降序排序

## Description
**English**:  
You are given N integers. You must sort them in **descending** order and then print them on a single line separated by spaces. If N = 0, print nothing.
  
给定 N 个整数，将它们从大到小排序并在一行中用空格分隔输出。如果 N = 0，则不输出任何内容。

## Input Description
**English**:  
- The first line contains an integer N (0 <= N <= 100).  
- The next N lines each contain one integer.

- 输入的第一行是一个整数 N (0 <= N <= 100)。  
- 接下来的 N 行中，每行包含一个整数。

## Output Description
**English**:  
Print the integers sorted in descending order on one line, separated by spaces. Do not include a trailing space at the end. If N=0, print nothing.

将排序后的整数从大到小输出在同一行，每个整数之间用空格分隔。末尾不留空格。如果 N=0，则不输出任何内容。

## Input Samples
**English Example**:  
```
5
2
1
5
3
4
```

**中文示例**:  
```
5
2
1
5
3
4
```

## Output Samples
**English / 中文**:  
```
5 4 3 2 1
```

---

## Test Cases (Hidden to Students)

**Test Case 1**  
- Input:
```
3
10
10
5
```
- Output:
```
10 10 5
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
4
-1
100
0
100
```
- Output:
```
100 100 0 -1
```