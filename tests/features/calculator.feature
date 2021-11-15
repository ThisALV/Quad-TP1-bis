Feature: calculator.calcule
  Calculer le résultat d'une opération entre deux nombres a et b donnés,
  l'opération étant déterminée par l'opérateur choisi en paramètre

  Scenario Outline: Somme de deux nombres
    Given Deux nombres <a> et <b>
    When Le calculateur les additionne
    Then Le résultat est <resultat_attendu>
    Examples:
        | a  | b  | resultat_attendu |
        | -2 | 1  | -1               |
        | 2  | 3  | 5                |
        | 5  | 5  | 10               |
