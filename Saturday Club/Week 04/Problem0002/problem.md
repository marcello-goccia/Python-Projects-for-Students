
### Title:  
Triangle Type Determination

### Description:

Given the lengths of three sides of a triangle, determine the type of triangle:

给定三角形的三边长度，判断三角形的类型：

- If all sides are equal, output "Equilateral"

  如果三边都相等，输出“Equilateral”

- If two sides are equal, output "Isosceles"

  如果有两边相等，输出“Isosceles”

- If no sides are equal, output "Scalene"

  如果三边都不相等，输出“Scalene”

- If the three sides cannot form a triangle, output "Invalid"

  如果三边不能构成三角形，输出“Invalid”

*Note:* For three sides to form a triangle, the sum of any two sides must be greater than the third side.

*注意：*三边能构成三角形的条件是任意两边之和大于第三边。

### Input Description:

Three positive integers representing the lengths of the sides.

三个正整数，表示三边的长度。

### Output Description:

A string indicating the type of triangle or "Invalid".

一个字符串，指示三角形的类型或“Invalid”。

### Input Samples:

```
3 3 3
```

### Output Samples:

```
Equilateral
```

---

**Hidden Test Cases:**

- **Test Case 1:**

  - **Input:**

    ```
    3 4 5
    ```

  - **Output:**

    ```
    Scalene
    ```

- **Test Case 2:**

  - **Input:**

    ```
    1 2 3
    ```

  - **Output:**

    ```
    Invalid
    ```

- **Test Case 3:**

  - **Input:**

    ```
    5 5 8
    ```

  - **Output:**

    ```
    Isosceles
    ```
