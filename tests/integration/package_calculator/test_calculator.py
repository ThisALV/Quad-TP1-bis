import pathlib


def test_calculator_calcule(monkeypatch):
    import package_calculator.calculator as mock_calc

    def mock_somme(*_):
        return 0

    def mock_exposant(*_):
        return 0

    monkeypatch.setattr(mock_calc, "exposant", mock_exposant)
    monkeypatch.setattr(mock_calc, "somme", mock_somme)

    logs_chemin = pathlib.Path("logs.txt")

    # On s'assure d'utiliser un nouveau fichier de logs pour chaque test d'intégration
    # missing_ok=True assure qu'il n'y a pas d'erreur s'il n'existait pas déjà
    logs_chemin.unlink(missing_ok=True)

    mock_calc.calcule("+", 1, 2)
    mock_calc.calcule("**", 2, 3)

    with open(logs_chemin, "r") as fentree:
        logs = fentree.readlines()

    assert len(logs) == 2
    assert logs[1].startswith("[")
    assert logs[1].endswith("] 2 ** 3 = 0\n")
    assert logs[0].startswith("[")
    assert logs[0].endswith("] 1 + 2 = 0\n")
