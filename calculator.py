"""Simple calculator module."""


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
    """Return the remainder of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a % b

def power(a,b)
    """Returns Power"""
    return a**b
