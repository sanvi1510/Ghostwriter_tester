# Calculator

A simple Python calculator library.

## Installation

To use this library, you should save it as a Python file, for example, `calculator.py`, with the following content:
```python
# calculator.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b
```
Then you can use it in your Python scripts.

## Usage

### Addition

```python
from calculator import add

def main():
    result = add(2, 3)
    print(result)  # Output: 5

if __name__ == "__main__":
    main()
```

### Multiplication

```python
from calculator import multiply

def main():
    result = multiply(4, 5)
    print(result)  # Output: 20

if __name__ == "__main__":
    main()
```

### Subtraction

```python
from calculator import subtract

def main():
    result = subtract(10, 3)
    print(result)  # Output: 7

if __name__ == "__main__":
    main()
```
Note: The function 'remain' which was renamed to 'remain_fn' is not present in the provided README content. If 'remain' or 'remain_fn' is used elsewhere in the documentation, it should be updated to reflect the new function name. 

To fix the code examples, we need to make sure the `calculator.py` file exists and has the necessary functions defined. The above code examples assume that the `calculator.py` file is in the same directory as the script that is using it. 

If you want to use the `calculator` library as a separate module, you should structure your project like this:
```markdown
project/
|---- calculator.py
|---- main.py
```
Then, in your `main.py` file, you can use the `calculator` library like this:
```python
# main.py
from calculator import add

def main():
    result = add(2, 3)
    print(result)  # Output: 5

if __name__ == "__main__":
    main()
```