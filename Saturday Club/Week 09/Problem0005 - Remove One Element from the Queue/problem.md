## Title
Remove One Element from the Queue

## Description
You are given a queue that contains a series of integers. Your task is to remove the front element of the queue, and then print the remaining elements in the queue from front to back.
给定一个包含一系列整数的队列，您的任务是删除队列中的第一个元素，然后打印队列中剩余的元素，从前到后。

## Input Description
The input will contain:
The first line will contain an integer n (1 ≤ n ≤ 100), the number of elements in the queue.
The next n lines will each contain an integer to enqueue into the queue.

输入将包含：
第一行将包含一个整数 n（1 ≤ n ≤ 100），表示队列中元素的数量。
接下来的 n 行将包含要入队的整数。

## Output Description
After removing the front element from the queue, print all the remaining elements in the queue from front to back, separated by spaces. If the queue becomes empty, print nothing.
删除队列中的第一个元素后，打印剩余的队列元素，从前到后，元素之间用空格分隔。如果队列为空，则不打印任何内容。

## Input Samples
3
10
20
30


## Output Samples
20 30


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

    // Remove the front element from the queue
    if (!q.empty()) {
        q.pop();  // Dequeue the front element
    }

    // Print the remaining elements in the queue
    if (!q.empty()) {
        while (!q.empty()) {
            cout << q.front() << " ";  // Print the front element
            q.pop();  // Remove the front element
        }
        cout << endl;
    }

    return 0;
}

