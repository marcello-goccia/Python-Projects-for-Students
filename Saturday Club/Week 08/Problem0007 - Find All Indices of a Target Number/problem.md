### **Find All Indices of a Target Number**

### **Title:** Find All Indices of a Target Number / 找到目标数字的所有索引  

---

### **Description:**  
You are given an array of integers and a target number. Your task is to find all the indices in the array where the target number occurs. If the target number does not exist in the array, output `-1`.  
给定一个整数数组和一个目标数字，你需要找到目标数字在数组中出现的所有索引。如果目标数字不存在于数组中，则输出 `-1`。

---

### **Input Description:**  
- The first line contains an integer `n`, the size of the array (1 ≤ n ≤ 100).  
- The second line contains `n` integers representing the array.  
- The third line contains the target number `x`.  
输入描述:  
- 第一行是整数 `n`，表示数组的大小（1 ≤ n ≤ 100）。  
- 第二行包含 `n` 个整数，表示数组。  
- 第三行是目标数字 `x`。

---

### **Output Description:**  
- If the target number exists, output all its indices separated by spaces (indices are 0-based).  
- If the target number does not exist, output `-1`.  
输出描述:  
- 如果目标数字存在，输出其所有索引，用空格分隔（索引从0开始）。  
- 如果目标数字不存在，输出 `-1`。

---

### **Input Samples:**  

Input 1:  
```
6  
1 2 3 2 4 2  
2  
```  
Output 1:  
```
1 3 5  
```  

Input 2:  
```
4  
5 6 7 8  
10  
```  
Output 2:  
```
-1  
```  

---

### **Hidden Test Cases:**  
Input:  
```
5  
1 1 1 1 1  
1  
```  
Output:  
```
0 1 2 3 4  
```  

Input:  
```
7  
10 20 30 40 50 60 70  
25  
```  
Output:  
```
-1  
```  

Input:  
```
8  
3 5 7 3 3 8 3 9  
3  
```  
Output:  
```
0 3 4 6  
```
