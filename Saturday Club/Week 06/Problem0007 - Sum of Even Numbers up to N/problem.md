## Title
Sum of Even Numbers up to N

## Description
编写一个函数，计算并返回从1到传入的正整数N之间所有偶数的和。

Write a function to compute and return the sum of all even numbers between 1 and the positive integer N passed as a parameter.

## Input Description
利用参数的形式传入一个正整数N。

Pass a positive integer N using parameter passing.

## Output Description
无任何输出，仅需要向主函数返回计算得到的偶数之和。

No output required; simply return the calculated sum of even numbers to the main function.


## Input Samples
10

（通过传参的形式传入，你不需要用到任何接收函数）

10

(Passed as a parameter; you don't need any receiving function)

## Output Samples
无任何输出，你仅需要向主函数返回结果30即可。

No output required; simply return the result 30 to the main function.


## Template code

//PREPEND BEGIN
#include <iostream>
using namespace std;
//PREPEND END

//TEMPLATE BEGIN
__ SumEvenNumbers(__)
{

}
//TEMPLATE END

//APPEND BEGIN
int main() 
{
    int n;
    cin >> n;
    cout << SumEvenNumbers(n);
    return 0;
}
//APPEND END

