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

  Scenario Outline: Différence entre deux nombres
    Given Deux nombres <a> et <b>
    When Le calculateur soustrait le 2ème terme au 1er
    Then Le résultat est <resultat_attendu>
    Examples:
        | a  | b  | resultat_attendu |
        | -2 | 1  | -3               |
        | 3  | 2  | 1                |
        | 5  | 5  | 0                |

  Scenario Outline: Division d'un nombre par 0
    Given Un nombre <x>
    When Le calculateur divise le nombre par 0
    Then Une erreur arithmétique est levée
    Examples:
        | x  |
        | -5 |
        | 1  |
        | 0  |
