## Title
Simple Sorting / 简易排序

## Description
**English**:  
You are given N integers. You must sort them in ascending order and then print them on a single line separated by spaces. If N = 0, print nothing.

给定 N 个整数，将它们从小到大排序并在一行中用空格分隔输出。如果 N = 0，则不输出任何内容。

## Input Description
**English**:  
- The first line contains an integer N (0 <= N <= 100).  
- The next N lines each contain one integer.

- 输入的第一行是一个整数 N (0 <= N <= 100)。  
- 接下来的 N 行中，每行包含一个整数。

## Output Description
**English**:  
Print the sorted integers in ascending order on one line, separated by spaces. Do not include a trailing space at the end. If N=0, print nothing.
 
将排序后的整数从小到大输出在同一行，每个整数之间用空格分隔。末尾不留空格。如果 N=0，则不输出任何内容。

## Input Samples
**English Example**:  
```
5
2
1
5
3
2
```


## Output Samples
**English / 中文**:  
```
1 2 2 3 5
```

---

~~## Test Cases (Hidden to Students)

**Test Case 1**  
- Input:
```
3
10
3
10
```
- Output:
```
3 10 10
```

**Test Case 2**  
- Input:
```
0
```
- Output:
*(no output)*

**Test Case 3**  
- Input:
```
4
-5
100
-5
0
```
- Output:
```
-5 -5 0 100
```~~
  
## Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N;
    cin >> N;  // Number of integers / 读取整数数量
    
    // If N=0, print nothing and end
    // 如果 N=0，则不输出任何内容并结束
    if (N == 0) {
        return 0;
    }
    
    // Read N integers into a vector
    // 读取 N 个整数存入 vector
    vector<int> arr(N);
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }
    
    // Bubble sort (simple but O(N^2))
    // 冒泡排序（简单，但时间复杂度为 O(N^2)）
    for (int i = 0; i < N - 1; i++) {
        for (int j = 0; j < N - i - 1; j++) {
            // Compare adjacent elements
            // 比较相邻元素
            if (arr[j] > arr[j + 1]) {
                // Swap if out of order
                // 如果顺序不对则交换
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
    
    // Print the sorted array in ascending order
    // 从小到大输出排序后的数组
    for (int i = 0; i < N; i++) {
        cout << arr[i];
        if (i < N - 1) {
            cout << " "; // Separate by space / 用空格分隔
        }
    }
    cout << endl;
    
    return 0;
}

```