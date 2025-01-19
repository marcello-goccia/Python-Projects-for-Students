## Title
Enqueue Queue


## Description
You are given a queue that starts empty. Your task is to simply enqueue a series of integers into the queue. After the enqueue operations, print the elements in the queue from front to back in the same order they were added.
给定一个空队列，您的任务是将一系列整数入队。入队操作完成后，按添加的顺序从前到后打印队列中的元素。



## Input Description
The input will contain:
The first line will contain an integer n (1 ≤ n ≤ 100), the number of elements to enqueue.
The next n lines will each contain an integer to enqueue into the queue.

输入将包含：
第一行将包含一个整数 n（1 ≤ n ≤ 100），表示要入队的元素数量。
接下来的 n 行将包含要入队的整数。

## Output Description
Print all the elements in the queue, from front to back, in the same order they were added. Each element should be printed on the same line, separated by a space.
打印队列中所有的元素，从前到后，按添加的顺序。每个元素应该打印在同一行，元素之间用空格分隔。

## Input Samples
3
10
20
30

## Output Samples
10 20 30

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

    // Print all elements in the queue
    while (!q.empty()) {
        cout << q.front() << " ";  // Print the front element of the queue
        q.pop();  // Remove the front element from the queue
    }

    return 0;
}
