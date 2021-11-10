from package_calculator import calculator
import pathlib


def test_calculator_calcule():
    logs_chemin = pathlib.Path("logs.txt")

    # On s'assure d'utiliser un nouveau fichier de logs pour chaque test d'intégration
    # missing_ok=True assure qu'il n'y a pas d'erreur s'il n'existait pas déjà
    logs_chemin.unlink(missing_ok=True)

    calculator.calcule("+", 1, 2)
    calculator.calcule("**", 2, 3)

    with open(logs_chemin, "r") as fentree:
        logs = fentree.readlines()

    assert len(logs) == 2
    assert logs[0] == "1 + 2 = 3"
    assert logs[1] == "2 ** 3 = 8"
