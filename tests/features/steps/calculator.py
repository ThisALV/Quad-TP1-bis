import behave
from package_calculator.calculator import *


@behave.given("Deux nombres {a:d} et {b:d}")
def step_impl(context, a, b):
    context.a = a
    context.b = b


@behave.when("Le calculateur les additionne")
def step_impl(context):
    context.resultat = calcule("+", context.a, context.b)


@behave.then("Le résultat est {resultat_attendu:d}")
def step_impl(context, resultat_attendu):
    assert resultat_attendu == context.resultat
