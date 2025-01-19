## Title
Find the First Occurrence of a Number in an Array

## Description
Given an array of integers and a target number, find the index of the first occurrence of the target number. If the number does not exist, return -1.
给定一个整数数组和一个目标数字，找到目标数字第一次出现的索引。如果数字不存在，则返回-1。

## Input Description
The first line contains an integer ( n ), the size of the array (1 ≤ ( n ) ≤ 100).  
The second line contains ( n ) integers representing the array.  
The third line contains the target number ( x ).  
第一行是整数 ( n )，表示数组的大小（1 ≤ ( n ) ≤ 100）。  
第二行包含 ( n ) 个整数，表示数组。  
第三行是目标数字 ( x )。  


## Output Description
The index of the first occurrence of the target number, or `-1` if it is not present.  
目标数字第一次出现的索引，如果不存在，则输出`-1`。


## Input Samples
6
2 4 6 4 5 7
4

5
1 3 5 7 9
2

## Output Samples 
```
1
```  
```
-1
```  

**Hidden Test Cases:**  
Input:  
```
10  
1 2 3 4 5 6 7 8 9 10  
5  
```  
Output:  
```
4  
```  

Input:  
```
4  
0 0 0 0  
1  
```  
Output:  
```
-1  
```  

Input:  
```
7  
5 1 5 7 5 9 5  
9  
```  
Output:  
```
5  
```