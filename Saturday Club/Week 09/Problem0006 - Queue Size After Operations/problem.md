## Title
Queue Size After operations

## Description
Implement a queue and print the size of the queue after performing several enqueue and dequeue operations.
实现一个队列，并在执行多个入队和出队操作后打印队列的大小。

## Input Description
The input will contain:
The first line will contain an integer n (1 ≤ n ≤ 100), the number of operations to perform.
Each of the next n lines will describe an operation:
"enqueue x" means to add integer x to the queue.
"dequeue" means to remove an element from the queue.

输入将包含：
第一行将包含一个整数 n（1 ≤ n ≤ 100），表示要执行的操作数量。
接下来的 n 行将描述操作：
"enqueue x" 表示将整数 x 入队。
"dequeue" 表示从队列中删除一个元素。

## Output Description
After each operation, print the size of the queue.
在每个操作之后，打印队列的大小。

## Input Samples
5
enqueue 10
enqueue 20
dequeue
enqueue 30
dequeue

## Output Samples
1
2
1
2
1


## Solution

#include <iostream>
#include <queue>
using namespace std;

int main() {
    int n;
    cin >> n;  // Number of operations
    queue<int> q;  // Declare a queue to hold integers

    string operation;
    int x;

    // Process each operation
    for (int i = 0; i < n; ++i) {
        cin >> operation;  // Read the operation
        if (operation == "enqueue") {
            cin >> x;  // Read the integer to enqueue
            q.push(x);  // Enqueue the element
        } else if (operation == "dequeue") {
            if (!q.empty()) {
                q.pop();  // Dequeue the front element
            }
        }

        // Print the size of the queue after each operation
        cout << q.size() << endl;
    }

    return 0;
}