from package_calculator import calculator
import pytest


def test_calculator_somme():
    assert calculator.somme(1, 1) == 2
    assert calculator.somme(-3, 1) == -2
    assert calculator.somme(4, -5) == -1


def test_calculator_soustraction():
    assert calculator.soustraction(1, 1) == 0
    assert calculator.soustraction(17, -5) == 22
    assert calculator.soustraction(-5, 5) == -10


def test_calculator_multiplication():
    assert calculator.multiplication(5, 1) == 5
    assert calculator.multiplication(10, -2) == -20
    assert calculator.multiplication(-6, 6) == -36


def test_calculator_division():
    assert calculator.division(5, 2) == 2.5
    assert calculator.division(30, -3) == -10
    assert calculator.division(-10, 4) == -2.5

    with pytest.raises(ArithmeticError):
        calculator.division(10, 0)


def test_calculator_calcule():
    with pytest.raises(ValueError):
        calculator.calcule("", 1, 2)

    with pytest.raises(ArithmeticError):
        calculator.calcule("/", 1, 0)

    assert calculator.calcule("+", 1, 2) == 3
    assert calculator.calcule("-", 1, 2) == -1
    assert calculator.calcule("*", 2, 0) == 0
    assert calculator.calcule("/", 1, 2) == 0.5
