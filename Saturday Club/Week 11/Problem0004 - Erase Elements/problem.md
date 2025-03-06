## Title
Erase Elements

## Description
Given a vector of n elements, remove the element at position p (0-based index).

给定一个长度为 n 的向量，删除索引为 p 的元素。

## Input Description
The first line contains two integers n and p (1 ≤ n ≤ 1000, 0 ≤ p < n)。
The second line contains n space-separated integers。

第一行包含两个整数 n 和 p (1 ≤ n ≤ 1000, 0 ≤ p < n)。
第二行包含 n 个用空格分隔的整数。

## Output Description
Print the modified vector after deleting the p-th element.

输出删除索引 p 后的向量。


## Input Samples
5 2
10 20 30 40 50


## Output Samples
10 20 40 50


## Test Cases

6 3
1 2 3 4 5 6
#### Output
1 2 3 5 6

4 0
99 88 77 66
#### Output
88 77 66

7 6
5 10 15 20 25 30 35
#### Output
5 10 15 20 25 30
