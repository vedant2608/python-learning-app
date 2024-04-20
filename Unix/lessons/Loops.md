### Examples of Loops with Various Data Structures

#### 1. `for` Loop with List:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry
```

#### 2. `for` Loop with Tuple:

```python
colors = ("red", "green", "blue")
for color in colors:
    print(color)
# Output:
# red
# green
# blue
```

#### 3. `for` Loop with Set:

```python
unique_numbers = {1, 2, 3, 4, 5}
for num in unique_numbers:
    print(num)
# Output:
# 1
# 2
# 3
# 4
# 5
```

#### 4. `for` Loop with Dictionary:

```python
student_grades = {"Alice": 85, "Bob": 90, "Charlie": 80}
for name, grade in student_grades.items():
    print(name, "scored", grade, "marks")
# Output:
# Alice scored 85 marks
# Bob scored 90 marks
# Charlie scored 80 marks
```

#### 5. Infinite Loop Example:

```python
# Infinite loop example (DO NOT RUN THIS CODE HERE)
while True:
    print("This is an infinite loop!")
```

#### Explanation:

An infinite loop occurs when the condition of the loop is always true, causing the loop to run indefinitely. In the above example, `while True:` creates a loop that continues endlessly because the condition `True` is always true. It's essential to avoid infinite loops as they can consume system resources and may lead to system instability. If accidentally executed, the code may need to be forcefully terminated or the environment refreshed to regain control.

#### `Warning: DO NOT EXECUTE THE INFINITE LOOP CODE HERE, OTHERWISE YOU HAVE TO REFRESH PAGE`
