## Title
First Element of a Queue

## Description
You are given a queue that contains a series of integers. Your task is to access the first element of the queue and print it.
给定一个包含一系列整数的队列，您的任务是访问队列中的第一个元素并打印它

## Input Description
The input will contain:
The first line will contain an integer n (1 ≤ n ≤ 100), the number of elements in the queue.
The next n lines will each contain an integer to enqueue into the queue.

输入将包含：
第一行将包含一个整数 n（1 ≤ n ≤ 100），表示队列中元素的数量。
接下来的 n 行将包含要入队的整数。

## Output Description
Print the first element of the queue.
打印队列中的第一个元素。

## Input Samples
3
10
20
30


## Output Samples
10


## Solution
#include <iostream>
#include <queue>
using namespace std;

int main() {
    int n;
    cin >> n;  // Number of elements to enqueue
    queue<int> q;  // Declare a queue

    // Enqueue elements
    for (int i = 0; i < n; ++i) {
        int x;
        cin >> x;  // Input the element to enqueue
        q.push(x);  // Enqueue the element
    }

    // Print the first element of the queue
    if (!q.empty()) {
        cout << q.front() << endl;  // Access and print the first element
    }

    return 0;
}


