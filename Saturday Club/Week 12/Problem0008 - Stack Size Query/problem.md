## Title
Stack Size Query

## Description
Create a stack that supports the following operations:

push X – Push integer X onto the stack.
pop – Remove the top element from the stack.
size – Print the number of elements currently in the stack.


创建一个支持以下操作的栈：

push X – 将整数 X 压入栈中。
pop – 从栈中移除顶部元素。
size – 输出当前栈的大小。

## Input Description
The first line contains an integer N (1 ≤ N ≤ 100), the number of operations.
The next N lines contain stack operations.


第一行包含一个整数 N (1 ≤ N ≤ 100)，表示操作的次数。
接下来的 N 行是栈操作。


## Output Description
Print the result of size operations.


输出 size 操作的结果。

## Input Samples
6
push 5
push 10
size
pop
size
pop


## Output Samples
2
1
0

## Test Cases

Input:
4
push 1
size
push 2
size

Output:
1
2

###########################

Input:
7
push 3
push 4
push 5
size
pop
pop
size

Output:
3
1

###########################

Input:
5
push 100
pop
size
push 200
size

Output:
0
1

