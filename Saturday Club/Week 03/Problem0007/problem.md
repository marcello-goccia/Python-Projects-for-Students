## Title
Rotate Array by k Positions

## Description
Given an array of integers, rotate the array by k positions to the right.

给定一个整数数组，将数组向右旋转 k 位。

## Input Description
The first line contains two integers n (1 ≤ n ≤ 100), the number of elements in the array, and k (1 ≤ k ≤ n), the number of positions to rotate. The second line contains n integers, representing the elements of the array.

第一行包含两个整数 n (1 ≤ n ≤ 100)，表示数组中的元素数量，和 k (1 ≤ k ≤ n)，表示旋转的位数。第二行包含 n 个整数，表示数组中的元素。

## Output Description
Output the array after rotating it by k positions.

输出将数组旋转 k 位后的结果。

## Input Samples
5 2  
1 2 3 4 5

## Output Samples
4 5 1 2 3

** Solution

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, k;
    cout << "Enter the number of elements and the rotation positions (n k): ";
    cin >> n >> k;

    vector<int> arr(n);
    cout << "Enter the elements of the array: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    k = k % n;  // Handle cases where k >= n
    vector<int> rotatedArray(n);

    // Rotate the array by shifting elements
    for (int i = 0; i < n; i++) {
        rotatedArray[(i + k) % n] = arr[i];
    }

    cout << "Rotated array: ";
    for (int i = 0; i < n; i++) {
        cout << rotatedArray[i] << " ";
    }
    cout << endl;

    return 0;
}
```

### Explanation:

1. **Modulo Operation**:
   - We use `k = k % n` to handle cases where \( k \) is greater than \( n \). This ensures the rotation is within bounds.

2. **Rotating Elements**:
   - We calculate the new position for each element using `(i + k) % n`, where `i` is the original index, `k` is the rotation amount, and `n` is the array size.
   - This places each element in its new rotated position.

3. **Output**:
   - After the rotation, we print the elements of `rotatedArray` to display the rotated result.

4. **Example**:
   - Input:  
     ```
     5 2
     1 2 3 4 5
     ```
   - Rotation: `[4, 5, 1, 2, 3]`

