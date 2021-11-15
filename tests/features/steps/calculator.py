import behave
from package_calculator.calculator import *


@behave.given("Deux nombres {a:d} et {b:d}")
def step_impl(context, a, b):
    context.a = a
    context.b = b


@behave.given("Un nombre {x:d}")
def step_impl(context, x):
    context.x = x


@behave.when("Le calculateur les additionne")
def step_impl(context):
    context.resultat = calcule("+", context.a, context.b)


@behave.when("Le calculateur soustrait le 2ème terme au 1er")
def step_impl(context):
    context.resultat = calcule("-", context.a, context.b)


@behave.when("Le calculateur divise le nombre par 0")
def step_impl(context):
    try:
        calcule("/", context.x, 0)
        context.erreur_arithmetique = False
    except ArithmeticError:
        context.erreur_arithmetique = True


@behave.then("Le résultat est {resultat_attendu:d}")
def step_impl(context, resultat_attendu):
    assert resultat_attendu == context.resultat


@behave.then("Une erreur arithmétique est levée")
def step_impl(context):
    assert context.erreur_arithmetique
