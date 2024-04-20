### Control Flow Statements in Python

Control flow statements in Python are used to alter the flow of program execution based on certain conditions. The primary control flow statements include `break`, `continue`, and `pass`.

#### 1. `break` Statement:

The `break` statement is used to exit a loop prematurely, halting the execution of the loop's block of code.

##### Syntax:

```python
for item in sequence:
    if condition:
        break
    # Code block
```

##### Example:

```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        break
    print(num)
# Output: 1 2
```

#### 2. `continue` Statement:

The `continue` statement is used to skip the remaining code inside a loop for the current iteration and move to the next iteration.

##### Syntax:

```python
for item in sequence:
    if condition:
        continue
    # Code block
```

##### Example:

```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        continue
    print(num)
# Output: 1 2 4 5
```

#### 3. `pass` Statement:

The `pass` statement is a null operation that does nothing when executed. It is often used as a placeholder when a statement is syntactically required but no action is needed.

##### Syntax:

```python
for item in sequence:
    if condition:
        pass
    # Code block
```

##### Example:

```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        pass
    print(num)
# Output: 1 2 3 4 5
```

#### Additional Examples:

1. **`break` in Nested Loop:**

```python
for i in range(3):
    for j in range(3):
        if j == 2:
            break
        print(i, j)
# Output:
# 0 0
# 0 1
# 1 0
# 1 1
# 2 0
# 2 1
```

2. **`continue` in Loop with `if` Statement:**

```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        continue
    print(num)
# Output: 1 3 5
```

#### Conclusion:

Control flow statements such as `break`, `continue`, and `pass` provide flexibility in altering the flow of program execution in Python. By using these statements effectively, you can control the behavior of loops and conditionals to achieve desired outcomes in your code.