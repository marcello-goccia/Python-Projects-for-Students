## Title
Push and Pop


## Description
Implement a simple stack with the following operations:

push X – Push integer X onto the stack.
pop – Remove the top element and print it. If the stack is empty, print "Stack is empty".


实现一个简单的栈，支持以下操作：

push X – 将整数 X 压入栈中。
pop – 移除栈顶元素并打印它。如果栈为空，则输出 "Stack is empty"。


## Input Description
The first line contains an integer N (1 ≤ N ≤ 100), the number of operations.
The next N lines contain stack operations.


第一行包含一个整数 N (1 ≤ N ≤ 100)，表示操作的次数。
接下来的 N 行是栈操作。

## Output Description

Print the result of pop operations.

输出 pop 操作的结果。

## Input Samples
5
push 5
push 10
pop
pop
pop


## Output Samples
10
5
Stack is empty


## Test Cases
###########################
Input:
3
push 1
pop
pop


Output:
1
Stack is empty


###########################

Input:
6
push 7
push 8
push 9
pop
pop
pop


Output:
9
8
7


###########################


Input:
8
push 4
push 5
pop
push 6
push 7
pop
pop
pop


Output:
5
7
6
4


###########################


## Solution


#include <iostream>
#include <stack>
#include <string>

int main() {
    int N;
    std::cin >> N;
    
    std::stack<int> st; // Declare a stack
    std::string command;
    
    for (int i = 0; i < N; ++i) {
        std::cin >> command;
        
        if (command == "push") {
            int x;
            std::cin >> x;
            st.push(x);
        } 
        else if (command == "pop") {
            if (!st.empty()) {
                std::cout << st.top() << std::endl;
                st.pop();
            } 
            else {
                std::cout << "Stack is empty" << std::endl;
            }
        }
    }

    return 0;
}
