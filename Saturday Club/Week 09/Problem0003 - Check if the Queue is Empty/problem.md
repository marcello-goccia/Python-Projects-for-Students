## Title
Check if the Queue is Empty

## Description
You are given a queue. Your task is to check if the queue is empty. Print "YES" if the queue is empty, and "NO" if it is not empty.
给定一个队列，您的任务是检查队列是否为空。如果队列为空，打印 "YES"；如果队列不为空，打印 "NO"。

## Input Description
The input will contain:
The first line will contain an integer n (1 ≤ n ≤ 100), the number of elements in the queue.
The next n lines will each contain an integer to enqueue into the queue.

输入将包含：
第一行将包含一个整数 n（1 ≤ n ≤ 100），表示队列中元素的数量。
接下来的 n 行将包含要入队的整数。

## Output Description
Print "YES" if the queue is empty after the operations, otherwise print "NO".
如果操作后队列为空，打印 "YES"；否则，打印 "NO"。

## Input Samples
3
10
20
30


## Output Samples
NO


## Solution

#include <iostream>
#include <queue>
using namespace std;

int main() {
    int n;
    cin >> n;  // Number of elements to enqueue
    queue<int> q;

    // Enqueue elements
    for (int i = 0; i < n; ++i) {
        int x;
        cin >> x;
        q.push(x);  // Enqueue the element
    }

    // Check if the queue is empty
    if (q.empty()) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }

    return 0;
}
