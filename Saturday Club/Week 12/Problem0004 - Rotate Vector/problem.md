## Title
Rotate Vector

## Description
Given a vector of n elements, rotate it k places to the left.

给定一个长度为 n 的向量，将其左旋转 k 位。

## Input Description
The first line contains two integers n and k (1 ≤ n ≤ 1000, 0 ≤ k ≤ 1000)。

The second line contains n space-separated integers。

第一行包含两个整数 n 和 k (1 ≤ n ≤ 1000, 0 ≤ k ≤ 1000)。

第二行包含 n 个用空格分隔的整数。

## Output Description
Print the vector after rotating k places to the left.

输出左旋转 k 位后的向量。

## Input Samples
5 2
1 2 3 4 5


## Output Samples
3 4 5 1 2


## Test Cases

Input:
6 3
10 20 30 40 50 60


Output:
40 50 60 10 20 30


###########################

Input:
4 1
-1 -2 -3 -4


Output:
-2 -3 -4 -1


###########################

Input:
7 7
5 10 15 20 25 30 35


Output:
5 10 15 20 25 30 35


###########################


## Solution

#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int n, k;
    std::cin >> n >> k;
    
    std::vector<int> vec(n);
    
    for (int i = 0; i < n; ++i) {
        std::cin >> vec[i];
    }

    // Handle cases where k is greater than n
    k = k % n; 

    // Rotate the vector left by k positions
    std::rotate(vec.begin(), vec.begin() + k, vec.end());

    // Print the rotated vector
    for (int num : vec) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}


## Solution without ROTATE methos:

#include <iostream>
#include <vector>

int main() {
    int n, k;
    std::cin >> n >> k;
    
    std::vector<int> vec(n);
    
    for (int i = 0; i < n; ++i) {
        std::cin >> vec[i];
    }

    // Handle cases where k is greater than n
    k = k % n; 

    // Create a new vector to store the rotated result
    std::vector<int> rotated(n);

    // Move elements to the rotated positions
    for (int i = 0; i < n; ++i) {
        rotated[i] = vec[(i + k) % n];
    }

    // Print the rotated vector
    for (int num : rotated) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}
