## Title
Sort and Remove Duplicates / 去重排序

## Description
**English**:  
You are given N integers. First, remove all duplicate values so that each distinct integer only appears once. Then sort these distinct integers in ascending order and print them in a single line separated by spaces. If there are no integers (N = 0), print nothing.
 
给定 N 个整数，首先去除所有重复的数字，使每个不同的整数只出现一次。然后将这些不重复的整数从小到大进行排序，并在一行内用空格分隔输出。如果没有整数 (N=0)，则不输出任何内容。

## Input Description
**English**:  
- The first line contains an integer N (0 <= N <= 100).  
- The next N lines each contain one integer.
 
- 输入的第一行是一个整数 N (0 <= N <= 100)。  
- 接下来的 N 行中，每行包含一个整数。

## Output Description
**English**:  
Print the distinct integers in ascending order on one line, separated by spaces, with no trailing space at the end. If N=0, print nothing.

将不重复的整数按从小到大的顺序输出在同一行，每个数字之间以空格分隔，末尾不留空格。如果 N=0，则不输出任何内容。

## Input Samples
**English Example**:  
```
5
2
2
1
3
1
```

**中文示例**:  
```
5
2
2
1
3
1
```

## Output Samples
**English / 中文**:  
```
1 2 3
```

---

## Test Cases (Hidden to Students)

**Test Case 1**  
- Input:
```
5
10
10
5
5
10
```
- Output:
```
5 10
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
100
0
```
- Output:
```
-1 0 100
```

## Solution
