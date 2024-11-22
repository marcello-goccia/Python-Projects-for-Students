## Title
Reverse a String

## Description
编写一个函数，反转传入的字符串并返回结果。

Write a function to reverse the string passed as a parameter and return the result.


## Input Description
利用参数的形式传入一个字符串。

Pass a string using parameter passing.

## Output Description
无任何输出，仅需要向主函数返回反转后的字符串。

No output required; simply return the reversed string to the main function.

## Input Samples
hello

（通过传参的形式传入，你不需要用到任何接收函数）

hello

(Passed as a parameter; you don't need any receiving function)

## Output Samples
无任何输出，你仅需要向主函数返回结果olleh即可。

No output required; simply return the result olleh to the main function.


## Template Code

//PREPEND BEGIN
#include <iostream>
#include <string>
using namespace std;
//PREPEND END

//TEMPLATE BEGIN
__ ReverseString(__)
{

}
//TEMPLATE END

//APPEND BEGIN
int main() 
{
    string s;
    getline(cin, s);
    cout << ReverseString(s);
    return 0;
}
//APPEND END

