## Title
Sort by Digit Sum / 按数字和排序

## Description
**English**:  
You are given N integers. For each integer, calculate the **sum of its digits** (ignore the negative sign if any, so -12 has a digit sum of 1+2=3). Sort the integers based on this digit sum in ascending order. If two integers have the same digit sum, place the smaller integer first. After sorting, print all integers on one line, separated by spaces. If N=0, print nothing.

给定 N 个整数。对每个整数计算其**数字之和**（如果有负号则忽略，如 -12 的数字和是 1+2=3）。根据数字和从小到大对整数进行排序。如果两个整数的数字和相同，则将数值较小的整数排在前面。排序完成后，将所有整数用空格分隔输出在同一行。如果 N=0，则不输出任何内容。

## Input Description
**English**:  
- The first line contains an integer N (0 <= N <= 100).  
- The next N lines each contain one integer (which may be negative, zero, or positive).


- 输入的第一行是一个整数 N (0 <= N <= 100)。  
- 接下来的 N 行中，每行包含一个整数（可能为负数、零或正数）。

## Output Description
**English**:  
Print the integers sorted by their digit sum in ascending order. If two integers share the same digit sum, the smaller integer appears first. Separate numbers with a space in a single line and do not include a trailing space. If N=0, print nothing.


将整数按数字和从小到大输出在同一行。如果两个整数的数字和相同，则数值较小的整数排在前面。用空格分隔输出，末尾不留空格。如果 N=0，则不输出任何内容。

## Input Samples
**English Example**:
```
5
12
2
-5
3
11
```
**Explanation**:
- Digit sums (ignoring signs):  
  - 12 → 1 + 2 = 3  
  - 2 → 2  
  - -5 → 5  
  - 3 → 3  
  - 11 → 1 + 1 = 2  
- Sorted by digit sum in ascending order, and by numerical value if sums are the same:  
  - Integers with sum=2: [2, 11] → (2 < 11)  
  - Integers with sum=3: [3, 12] → (3 < 12)  
  - Integer with sum=5: [-5]  
- Final order: `2 11 3 12 -5`

**中文示例**:
```
5
12
2
-5
3
11
```
**说明**:
- 忽略负号后计算数字和：  
  - 12 → 1 + 2 = 3  
  - 2 → 2  
  - -5 → 5  
  - 3 → 3  
  - 11 → 1 + 1 = 2  
- 先按数字和从小到大排序，若数字和相同，则数值较小的整数在前：  
  - 数字和为 2 的有 [2, 11] → (2 < 11)  
  - 数字和为 3 的有 [3, 12] → (3 < 12)  
  - 数字和为 5 的有 [-5]  
- 最终顺序：`2 11 3 12 -5`

## Output Samples
**English / 中文**:
```
2 11 3 12 -5
```

---

## Test Cases (Hidden to Students)

**Test Case 1**  
- Input:
```
3
-1
10
2
```
- Digit sums:
- -1 → sum=1  
- 10 → sum=1 (1+0=1)  
- 2 → sum=2  
- Sorting by digit sum:
- Both -1 and 10 have sum=1, so smaller integer (-1) comes first, then 10  
- Next is 2 (sum=2)  
- Final order: `-1 10 2`  
- Output:
```
-1 10 2
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
5
999
-10
-99
0
100
```
- Digit sums:
- 999 → 9+9+9=27  
- -10 → 1+0=1  
- -99 → 9+9=18  
- 0 → 0  
- 100 → 1+0+0=1  
- Sort by digit sum, then by numeric value if needed:
- 0 (sum=0)  
- -10 (sum=1), 100 (sum=1) → -10 < 100  
- -99 (sum=18)  
- 999 (sum=27)  
- Final order: `0 -10 100 -99 999`  
- Output:
```
0 -10 100 -99 999
```


## Solution
