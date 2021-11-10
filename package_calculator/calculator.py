import datetime


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
        instant = datetime.datetime.now().strftime("%d/%m/%Y %H/%M/%S")
        print(f"[{instant}] {a} {operation} {b} = {resultat}", file=fsortie)

    return resultat


def dis_bonjour():
    return "Bonjour"
