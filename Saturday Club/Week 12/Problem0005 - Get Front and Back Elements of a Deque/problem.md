## Title
Get Front and Back Elements of a Deque

## Description
A deque allows accessing both front and back elements. Your task is to implement a deque and perform the following operations:
Insert elements at the front or back.
Print the front and back element after each operation.
If the deque is empty, print "Deque is empty" instead of the front or back element.

双端队列允许访问前端和后端的元素。您的任务是实现一个双端队列，并执行以下操作：
在前端或后端插入元素。
在每个操作后，打印前端和后端的元素。
如果双端队列为空，则打印 "Deque is empty"。

## Input Description
First line contains an integer n (1 ≤ n ≤ 100), the number of operations.
Each of the next n lines contains one of the following commands:
"push_front x" (push x to the front)
"push_back x" (push x to the back)
"pop_front" (remove front element)
"pop_back" (remove back element)
输入将包含：

第一行是整数 n（1 ≤ n ≤ 100），表示要执行的操作数。
接下来的 n 行包含以下命令之一：
"push_front x"（在前端插入 x）
"push_back x"（在后端插入 x）
"pop_front"（删除前端元素）
"pop_back"（删除后端元素

## Output Description
After each operation, print the front and back element separated by a space. If the deque is empty, print "Deque is empty".
在每个操作后，打印前端和后端的元素，用空格分隔。如果双端队列为空，则打印 "Deque is empty"。

## Input Samples
4
push_back 10
push_front 20
pop_front
pop_back


## Output Samples
10 10
20 10
10 10
Deque is empty

## Test Cases

Input:
3
push_front 5
push_back 8
pop_front

Output:
5 5
5 8
8 8

################################

Input:
2
push_back 1
pop_back

Output:
1 1
Deque is empty

################################

Input:
4
push_front 3
push_front 4
push_back 5
pop_front

Output:
3 3
4 3
4 5
3 5


