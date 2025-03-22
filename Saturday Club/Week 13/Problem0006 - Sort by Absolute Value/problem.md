## Title
Sort by Absolute Value / 按绝对值排序

## Description
**English**:  
You are given N integers. Sort these integers in ascending order based on their **absolute value**. If two integers have the same absolute value, place the smaller integer first (e.g., -2 should come before 2). Then print all the integers in a single line, separated by spaces. If N = 0, print nothing.

给定 N 个整数，请按照它们的**绝对值**从小到大进行排序。如果两个整数的绝对值相同，则将较小的整数排在前面（例如，-2 排在 2 之前）。排序完成后，将所有整数用空格分隔输出在同一行。如果 N = 0，则不输出任何内容。

## Input Description
**English**:  
- The first line contains an integer N (0 <= N <= 100).  
- The next N lines each contain one integer.

  
- 输入的第一行是一个整数 N (0 <= N <= 100)。  
- 接下来的 N 行中，每行包含一个整数。

## Output Description
**English**:  
Print the integers sorted by absolute value in one line, separated by spaces, with no trailing space at the end. If N=0, print nothing.

将按照绝对值排序后的整数在一行中用空格分隔输出，末尾不留空格。如果 N=0，则不输出任何内容。

## Input Samples
**English Example**:
```
5
-2
-3
2
0
2
```
**Explanation**:
- Absolute values are [2, 3, 2, 0, 2].  
- Sorted by absolute value: 0, -2, 2, -3, 2.  
  - Here, 0 (abs=0) comes first.  
  - -2 and 2 both have abs=2, but -2 < 2, so -2 is placed before 2.  
  - -3 (abs=3) comes next, followed by 2 (abs=2) — but note we already had a 2 in the list, so they appear in the order we compare them.  
- Final order: `0 -2 2 2 -3` or `0 -2 2 -3 2`? Let's clarify carefully:
  - We have: [-2, -3, 2, 0, 2].
  - Sort by absolute value:
    - 0 (abs=0)
    - -2, 2, 2 (all abs=2), among them the smaller actual integer is -2, then 2, then 2.  
    - -3 (abs=3)
  - So final: **0 -2 2 2 -3**
  
**中文示例**:
```
5
-2
-3
2
0
2
```
**说明**:
- 各数的绝对值分别为 [2, 3, 2, 0, 2]  
- 按绝对值从小到大排序：0 (绝对值0), -2 (绝对值2), 2 (绝对值2), 2 (绝对值2), -3 (绝对值3)  
  - 当绝对值相同时，以数值较小者在前。例如 -2 比 2 小，所以 -2 在 2 之前。  
- 最终顺序：`0 -2 2 2 -3`

## Output Samples
**English / 中文**:
```
0 -2 2 2 -3
```

---

## Test Cases (Hidden to Students)

**Test Case 1**  
- Input:
```
4
1
-1
2
-2
```
- Sorted by absolute value:
- abs(1)=1, abs(-1)=1, abs(2)=2, abs(-2)=2
- So, among abs=1, -1 < 1 → -1, then 1
- Among abs=2, -2 < 2 → -2, then 2
- Final order: -1 1 -2 2
- Output:
```
-1 1 -2 2
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
3
-3
-3
3
0
```
- Absolute values: 3, 3, 3, 3, 0  
- Sorted order:
- 0 (abs=0)
- Then among the 3’s: -3 < 3, so -3 comes before 3
- We have two -3s and two 3s: all are abs=3, so both -3s come first (order among identical numbers is not distinct here, but typically it’s just the same value repeated), then both 3s.
- Final: `0 -3 -3 3 3`
- Output:
```
0 -3 -3 3 3
```