## Title
Check Perfect Number

## Description
编写一个函数，判断传入的正整数是否为完美数。如果是，返回'Y'（一个字符，大写字母Y），否则返回'N'（一个字符，大写字母N）。完美数是指一个数等于其所有正因子（不包括自身）之和的数。

Write a function to determine whether a positive integer passed as a parameter is a perfect number. If it is, return 'Y' (a single character, uppercase Y); otherwise, return 'N' (a single character, uppercase N). A perfect number is a number that is equal to the sum of its positive divisors excluding itself.

## Input Description
利用参数的形式传入一个正整数。

Pass a positive integer using parameter passing.

## Output Description
无任何输出，仅需要向主函数返回判断结果。

No output required; simply return the result to the main function.

## Input Samples
6

（通过传参的形式传入，你不需要用到任何接收函数）

6

(Passed as a parameter; you don't need any receiving function)

## Output Samples
无任何输出，你仅需要向主函数返回字母Y即可。

No output required; simply return the letter 'Y' to the main function.


## Template Code

//PREPEND BEGIN
#include <iostream>
using namespace std;
//PREPEND END

//TEMPLATE BEGIN
__ IsPerfectNumber(__)
{

}
//TEMPLATE END

//APPEND BEGIN
int main() 
{
    int n;
    cin >> n;
    cout << IsPerfectNumber(n);
    return 0;
}
//APPEND END

