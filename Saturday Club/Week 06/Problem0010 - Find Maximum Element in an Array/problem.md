## Title
Find Maximum Element in an Array

## Description
编写一个函数，接收一个整数数组和数组的长度，返回数组中最大的元素。

Write a function that receives an integer array and its length, and returns the largest element in the array.

## Input Description
利用参数的形式传入一个整数N（数组长度），随后输入N个整数作为数组元素。

Pass an integer N (array length) using parameter passing, followed by N integers as array elements.

## Output Description
无任何输出，仅需要向主函数返回数组中的最大值。

No output required; simply return the maximum value in the array to the main function.



## Input Samples
5

1 3 5 7 9

（通过传参的形式传入，你不需要用到任何接收函数）

5

1 3 5 7 9

(Passed as parameters; you don't need any receiving function)

## Output Samples
无任何输出，你仅需要向主函数返回结果9即可。

No output required; simply return the result 9 to the main function.


## Template Code

//PREPEND BEGIN
#include <iostream>
using namespace std;
//PREPEND END

//TEMPLATE BEGIN
__ FindMax(__, __)
{

}
//TEMPLATE END

//APPEND BEGIN
int main() 
{
    int n;
    cin >> n;
    int arr[n];
    for(int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    cout << FindMax(arr, n);
    return 0;
}
//APPEND END

