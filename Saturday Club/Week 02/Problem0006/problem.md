### **Title:**  
Find GCD of Two Numbers  
求两个数的最大公约数

### **Description:**  
Write a program that finds the greatest common divisor (GCD) of two given integers.  
编写一个程序，求两个给定整数的最大公约数（GCD）。

### **Input Description:**  
Two integers separated by a space.  
两个用空格分隔的整数。

### **Output Description:**  
The GCD of the two integers.  
这两个整数的最大公约数。

### **Input Samples:**  
`18 24`

### **Output Samples:**  
`6`



** Solution

#include <iostream>
using namespace std;

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main() {
    int a, b;
    cout << "Enter two integers separated by a space: ";
    cin >> a >> b;

    cout << "GCD: " << gcd(a, b) << endl;
    return 0;
}

** Explanation

Explanation:
Euclidean Algorithm:

The loop continues until b becomes zero. In each iteration, we update a to b and b to the remainder of a % b.
Once b is zero, a will hold the GCD.
Example:

Input: 18 24
Iterations:
a = 18, b = 24
a = 24, b = 18 % 24 = 18
a = 18, b = 24 % 18 = 6
a = 6, b = 18 % 6 = 0
Output: 6