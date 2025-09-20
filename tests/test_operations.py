""" tests/test_operations.py """
import pytest
from app.operations import addition, subtraction, multiplication, division


def test_addition_positive():
    """Test positive cases for addition."""
    assert addition(2, 3) == 5
    assert addition(0, 0) == 0
    assert addition(-1, 1) == 0


def test_addition_negative():
    """Test negative cases for addition."""
    assert addition(-3, -4) == -7
    assert addition(-6, 0) == -6


def test_subtraction_positive():
    """Test positive cases for subtraction."""
    assert subtraction(5, 3) == 2
    assert subtraction(0, 0) == 0
    assert subtraction(10, 5) == 5


def test_subtraction_negative():
    """Test negative cases for subtraction."""
    assert subtraction(-11, -7) == -4
    assert subtraction(7, 11) == -4


def test_multiplication_positive():
    """Test positive cases for multiplication."""
    assert multiplication(2, 3) == 6
    assert multiplication(0, 8) == 0
    assert multiplication(-2, -3) == 6


def test_multiplication_negative():
    """Test negative cases for multiplication."""
    assert multiplication(5, -6) == -30
    assert multiplication(-5, 6) == -30


def test_division_positive():
    """Test positive cases for division."""
    assert division(12, 4) == 3
    assert division(-12, -4) == 3


def test_division_negative():
    """Test negative cases for division."""
    assert division(12, -4) == -3
    assert division(-12, 4) == -3


def test_division_by_zero():
    """Test division by zero."""
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        division(2, 0)
