### **Title:**  
Fibonacci Sequence Generator  
斐波那契数列生成器

### **Description:**  
Write a program that generates the first n  numbers in the Fibonacci sequence.  
编写一个程序，生成斐波那契数列的前 n  个数字。

### **Input Description:**  
A single integer n ( 1 ≤ n ≤ 50 ).  
一个整数 n ( 1 ≤ n ≤ 50 )。

### **Output Description:**  
The first  n  Fibonacci numbers, separated by spaces.  
前  n  个斐波那契数，用空格分隔。

### **Input Samples:**  
`5`

### **Output Samples:**  
`0 1 1 2 3`


** Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of Fibonacci numbers to generate: ";
    cin >> n;

    vector<int> fibonacci(n);
    if (n > 0) fibonacci[0] = 0;  // First Fibonacci number
    if (n > 1) fibonacci[1] = 1;  // Second Fibonacci number

    for (int i = 2; i < n; i++) {
        fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2];
    }

    cout << "Fibonacci sequence: ";
    for (int i = 0; i < n; i++) {
        cout << fibonacci[i] << " ";
    }
    cout << endl;

    return 0;
}
```

### Explanation:

1. **Initial Conditions**:
   - If `n` is 1 or more, initialize the first number as `0`.
   - If `n` is 2 or more, initialize the second number as `1`.

2. **Iterative Calculation**:
   - Use a loop starting from index 2 to calculate each Fibonacci number as the sum of the previous two numbers.
   - Store each result in the `fibonacci` vector.

3. **Output**:
   - Print the contents of the `fibonacci` vector to show the first \( n \) numbers in the sequence.

4. **Example**:
   - Input: `5`
   - Fibonacci sequence: `0 1 1 2 3`
