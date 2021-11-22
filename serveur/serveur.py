import bottle
from package_calculator import calculator
from random import randint


def entier_aleatoire():
    return randint(-1000, 1000)


@bottle.route("/hello")
def hello():
    a = entier_aleatoire()
    b = entier_aleatoire()

    return f"Hello world {a} + {b} = {calculator.somme(a, b)}"


@bottle.route("/<nom_fichier>")
def servir_fichier_statique(nom_fichier):
    return bottle.static_file(nom_fichier, root="public")


bottle.run()  # Host localhost et port 8080 déjà mis par défaut
