## Title
Armstrong Number Checker

## Description
编写一个函数，判断传入的整数是否为阿姆斯特朗数。如果是，返回'Y'（一个字符，大写字母Y），否则返回'N'（一个字符，大写字母N）。阿姆斯特朗数是指一个n位数，其各位数字的n次方之和等于该数本身。

Write a function to determine whether an integer passed as a parameter is an Armstrong number. If it is, return 'Y' (a single character, uppercase Y); otherwise, return 'N' (a single character, uppercase N). An Armstrong number is a n-digit number that is equal to the sum of its own digits each raised to the power of n.

## Input Description
利用参数的形式传入一个整数。

Pass an integer using parameter passing.

## Output Description
无任何输出，仅需要向主函数返回判断结果。

No output required; simply return the result to the main function.

## Input Samples
153

（通过传参的形式传入，你不需要用到任何接收函数）

153

(Passed as a parameter; you don't need any receiving function)

## Output Samples
无任何输出，你仅需要向主函数返回字母Y即可。

No output required; simply return the letter 'Y' to the main function.

## Template Code

//PREPEND BEGIN
#include <iostream>
#include <cmath>
using namespace std;
//PREPEND END

//TEMPLATE BEGIN
__ IsArmstrong(__)
{

}
//TEMPLATE END

//APPEND BEGIN
int main() 
{
    int n;
    cin >> n;
    cout << IsArmstrong(n);
    return 0;
}
//APPEND END

