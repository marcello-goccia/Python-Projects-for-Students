## Title
Queue is Empty After operations

## Description
Write a program to check whether a queue is empty. If the queue is empty, print "Queue is empty".
编写程序检查队列是否为空。如果队列为空，打印“队列为空”。

## Input Description
The input will contain:
The first line will contain an integer n (1 ≤ n ≤ 100), the number of operations to perform.
Each of the next n lines will contain an operation:
"enqueue x" adds integer x to the queue.
"dequeue" removes an element from the queue.

输入将包含：
第一行将包含一个整数 n（1 ≤ n ≤ 100），表示要执行的操作数量。
接下来的 n 行将包含操作：
"enqueue x" 表示将整数 x 入队。
"dequeue" 表示从队列中删除一个元素。

## Output Description
After each operation, print "Queue is empty" if the queue is empty, otherwise print nothing.
在每个操作之后，如果队列为空，打印“队列为空”，否则不打印任何内容。

## Input Samples
5
enqueue 10
enqueue 20
dequeue
dequeue
dequeue


## Output Samples

Queue is empty

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

        // After each operation, check if the queue is empty
        if (q.empty()) {
            cout << "Queue is empty" << endl;
        }
    }

    return 0;
}




