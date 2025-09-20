""" tests/test_calculator.py """
import sys
from io import StringIO
from app.calculator import calculator


# Helper function to capture print statements
def run_calculator_with_input(monkeypatch, inputs):
    """
    Simulates user input and captures output from the calculator REPL.
    
    :param monkeypatch: pytest fixture to simulate user input
    :param inputs: list of inputs to simulate
    :return: captured output as a string
    """
    input_iterator = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))

    # Capture the output of the calculator
    captured_output = StringIO()
    sys.stdout = captured_output
    calculator()
    sys.stdout = sys.__stdout__  # Reset stdout
    return captured_output.getvalue()


# Positive Tests
def test_addition(monkeypatch):
    """Test addition operation in REPL."""
    inputs = ["add 9 10", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 19.0" in output


def test_subtraction(monkeypatch):
    """Test subtraction operation in REPL."""
    inputs = ["subtract 6 4", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 2.0" in output


def test_multiplication(monkeypatch):
    """Test multiplication operation in REPL."""
    inputs = ["multiply 3 7", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 21.0" in output


def test_division(monkeypatch):
    """Test division operation in REPL."""
    inputs = ["divide 16 4", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 4.0" in output


# Negative Tests
def test_invalid_operation(monkeypatch):
    """Test invalid operation in REPL."""
    inputs = ["modulus 11 2", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Unknown operation" in output


def test_invalid_input_format(monkeypatch):
    """Test invalid input format in REPL."""
    inputs = ["add eight nine", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Invalid input. Please follow the format" in output


def test_division_by_zero(monkeypatch):
    """Test division by zero in REPL."""
    inputs = ["divide 9 0", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Division by zero is not allowed" in output
