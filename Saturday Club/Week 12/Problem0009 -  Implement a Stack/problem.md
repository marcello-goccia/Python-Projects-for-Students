## Title
Implement a Stack

## Description
Implement a stack using an array. The stack should support the following operations:

push X – Push integer X onto the stack.
pop – Remove and print the top element. If the stack is empty, print "Stack is empty".
top – Print the top element of the stack without removing it. If the stack is empty, print "Stack is empty".


使用数组实现一个栈。栈需要支持以下操作：

push X – 将整数 X 压入栈中。
pop – 移除并打印栈顶元素。如果栈为空，则输出 "Stack is empty"。
top – 打印栈顶元素但不移除它。如果栈为空，则输出 "Stack is empty"。

## Input Description

The first line contains an integer N (1 ≤ N ≤ 100), the number of operations.
The next N lines contain stack operations.


第一行包含一个整数 N (1 ≤ N ≤ 100)，表示操作的次数。
接下来的 N 行是栈操作。

## Output Description
Print the output of pop and top operations.

输出 pop 和 top 操作的结果。

## Input Samples
5
push 10
push 20
top
pop
pop


## Output Samples
20
20
10


## Test Cases
###########################
Input:
6
push 5
push 15
push 25
pop
top
pop


Output:
25
15
15


###########################

Input:
7
push 1
push 2
push 3
pop
pop
pop
pop


Out put:
3
2
1
Stack is empty


###########################
Input:
8
top
push 100
push 200
pop
push 300
top
pop
pop


Output:
Stack is empty
200
300
300
100


## Solution


#include <iostream>
#include <string>

#define MAX_SIZE 100 // Maximum size of the stack

class Stack {
private:
    int arr[MAX_SIZE]; // Array to store elements
    int topIndex; // Index of the top element

public:
    Stack() {
        topIndex = -1; // Initialize stack as empty
    }

    void push(int x) {
        if (topIndex < MAX_SIZE - 1) {
            arr[++topIndex] = x;
        }
    }

    void pop() {
        if (topIndex >= 0) {
            std::cout << arr[topIndex--] << std::endl;
        } else {
            std::cout << "Stack is empty" << std::endl;
        }
    }

    void top() {
        if (topIndex >= 0) {
            std::cout << arr[topIndex] << std::endl;
        } else {
            std::cout << "Stack is empty" << std::endl;
        }
    }
};

int main() {
    int N;
    std::cin >> N;
    
    Stack st; // Create a stack instance
    std::string command;

    for (int i = 0; i < N; ++i) {
        std::cin >> command;
        
        if (command == "push") {
            int x;
            std::cin >> x;
            st.push(x);
        } 
        else if (command == "pop") {
            st.pop();
        } 
        else if (command == "top") {
            st.top();
        }
    }

    return 0;
}
