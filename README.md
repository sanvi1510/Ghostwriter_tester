# Calculator

A simple Python calculator library.

## Installation

To use this library, you should save it as a Python file, for example, `calculator.py`, with the following content:
```python
# calculator.py
def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def product(a, b):
    """Return the product of two numbers."""
    return a * b

def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

def divide(a, b):
    """Return the division of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def remainder(a, b):
    """Return the remainder of a divided by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a % b
```
Then you can use it in your Python scripts.

## Usage

### Addition

To use the `add` function, save the following code in a file, for example, `main_add.py`:
```python
# main_add.py
from calculator import add

def main():
    result = add(2, 3)
    print(result)  # Output: 5

if __name__ == "__main__":
    main()
```
Run the script using `python main_add.py`.

### Multiplication

To use the `product` function, save the following code in a file, for example, `main_product.py`:
```python
# main_product.py
from calculator import product

def main():
    result = product(4, 5)
    print(result)  # Output: 20

if __name__ == "__main__":
    main()
```
Run the script using `python main_product.py`.

### Subtraction

To use the `subtract` function, save the following code in a file, for example, `main_subtract.py`:
```python
# main_subtract.py
from calculator import subtract

def main():
    result = subtract(10, 3)
    print(result)  # Output: 7

if __name__ == "__main__":
    main()
```
Run the script using `python main_subtract.py`.

### Division

To use the `divide` function, save the following code in a file, for example, `main_divide.py`:
```python
# main_divide.py
from calculator import divide

def main():
    result = divide(10, 2)
    print(result)  # Output: 5.0

if __name__ == "__main__":
    main()
```
Run the script using `python main_divide.py`.

### Remainder

To use the `remainder` function, save the following code in a file, for example, `main_remainder.py`:
```python
# main_remainder.py
from calculator import remainder

def main():
    result = remainder(10, 3)
    print(result)  # Output: 1

if __name__ == "__main__":
    main()
```
Run the script using `python main_remainder.py`.

To use the `calculator` library as a separate module, you should structure your project like this:
```markdown
project/
|---- calculator.py
|---- main_add.py
|---- main_product.py
|---- main_subtract.py
|---- main_divide.py
|---- main_remainder.py
```
Make sure the `calculator.py` file is in the same directory as the script that is using it. 

Note: The `calculator.py` file should be in the same directory as the scripts that are using it. If the `calculator.py` file is in a different directory, you need to adjust the import statement accordingly.

However, upon reviewing the provided calculator.py file in the repository context, it appears there is a duplicate function definition for `divide(a, b)`. The second definition seems to be intended for the `remainder(a, b)` function. Here is the corrected version of `calculator.py`:
```python
# calculator.py
def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def product(a, b):
    """Return the product of two numbers."""
    return a * b

def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

def divide(a, b):
    """Return the division of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def remainder(a, b):
    """Return the remainder of a divided by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a % b
```