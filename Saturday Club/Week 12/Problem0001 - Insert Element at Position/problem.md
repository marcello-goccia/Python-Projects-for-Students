## Title
Insert Element at Position

## Description
Given a vector of n elements, insert a value x at position p (0-based index).

给定一个长度为 n 的向量，在索引 p 处插入值 x。


## Input Description
The first line contains three integers n, p, and x (1 ≤ n ≤ 1000, 0 ≤ p ≤ n, -1000 ≤ x ≤ 1000)。

The second line contains n space-separated integers。

第一行包含三个整数 n、p 和 x (1 ≤ n ≤ 1000, 0 ≤ p ≤ n, -1000 ≤ x ≤ 1000)。

第二行包含 n 个用空格分隔的整数。


## Output Description
Print the vector after inserting x at position p。

输出在索引 p 插入 x 之后的向量。


## Input Samples
5 2 99
10 20 30 40 50


## Output Samples
10 20 99 30 40 50


## Test Cases

Input:
3 1 7
1 2 3


Output:
1 7 2 3


###########################

Input:
4 0 -5
10 20 30 40


Output:
-5 10 20 30 40


###########################

Input:
2 2 100
1 2


Output:
1 2 100


###########################


## Solution


#include <iostream>
#include <vector>

int main() {
    int n, p, x;
    std::cin >> n >> p >> x;
    
    std::vector<int> vec(n);
    
    // Read the input elements into the vector
    for (int i = 0; i < n; ++i) {
        std::cin >> vec[i];
    }

    // Insert x at position p
    vec.insert(vec.begin() + p, x);

    // Print the updated vector
    for (int num : vec) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}

