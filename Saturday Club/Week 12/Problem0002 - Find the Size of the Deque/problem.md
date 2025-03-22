## Title
Find the Size of the Deque

## Description
You need to implement a deque and perform several operations. After each operation, print the size of the deque.
你需要实现一个双端队列，并执行多个操作。在每个操作后，打印队列的大小。

## Input Description
The first line contains an integer n (1 ≤ n ≤ 100), the number of operations.
Each of the next n lines contains one of the following commands:
"push_front x" (push x to the front)
"push_back x" (push x to the back)
"pop_front" (remove the front element)
"pop_back" (remove the back element)

第一行是整数 n（1 ≤ n ≤ 100），表示要执行的操作数。
接下来的 n 行包含以下命令：
"push_front x"（在前端插入 x）
"push_back x"（在后端插入 x）
"pop_front"（删除前端元素）
"pop_back"（删除后端元素）


## Output Description
After each operation, print the size of the deque.
在每个操作后，打印双端队列的大小。

## Input Samples
5
push_back 10
push_front 20
pop_front
push_back 30
pop_back

## Output Samples
1
2
1
2
1

## Test Cases
Input:
3
push_front 5
push_back 8
pop_front

Output:
1
2
1

#####################
Input:
4
push_back 1
push_front 2
pop_back
pop_front

Output:
1
2
1
0

#####################
Input:
5
push_front 3
push_front 4
push_back 5
pop_front
pop_back

Output:
1
2
3
2
1


## Solution

#include <iostream>
#include <deque>
#include <string>

int main() {
    int n;
    std::cin >> n;
    
    std::deque<int> dq; // Declare a deque
    std::string command;
    
    for (int i = 0; i < n; ++i) {
        std::cin >> command;
        
        if (command == "push_front") {
            int x;
            std::cin >> x;
            dq.push_front(x);
        } 
        else if (command == "push_back") {
            int x;
            std::cin >> x;
            dq.push_back(x);
        } 
        else if (command == "pop_front") {
            if (!dq.empty()) {
                dq.pop_front();
            }
        } 
        else if (command == "pop_back") {
            if (!dq.empty()) {
                dq.pop_back();
            }
        }
        
        // Print the size of the deque after each operation
        std::cout << dq.size() << std::endl;
    }

    return 0;
}
