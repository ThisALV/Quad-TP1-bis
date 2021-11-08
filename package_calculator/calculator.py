def somme(a, b):
    return a + b


def soustraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


operations = {
    "+": somme,
    "-": soustraction,
    "*": multiplication,
    "/": division
}


def calcule(operation, a, b):
    if operation not in operations:
        raise ValueError(f"Opération {operation} inconnue")

    return operations[operation](a, b)
