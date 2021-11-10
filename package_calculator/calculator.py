def somme(a, b):
    return a + b


def soustraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def exposant(a, n):
    if n < 0:
        raise ValueError("n doit être supérieur ou égal à 0")

    if n == 0:
        return 1
    if n == 1:
        return a
    if n % 2 == 0:
        return exposant(a * a, n / 2)

    return a * exposant(a * a, (n - 1) / 2)


operations = {
    "+": somme,
    "-": soustraction,
    "*": multiplication,
    "/": division,
    "**": exposant
}


def calcule(operation, a, b):
    if operation not in operations:
        raise ValueError(f"Opération {operation} inconnue")

    resultat = operations[operation](a, b)

    with open("logs.txt", "a") as fsortie:
        fsortie.write(f"{a} {operation} {b} = {resultat}")

    return resultat


def dis_bonjour():
    return "Bonjour"
