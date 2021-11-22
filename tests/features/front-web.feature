# language: fr
Fonctionnalité: Front-end Web
  Teste l'interface web de l'application calculator

  Plan du Scénario: Ouverture navigateur
    Étant donné Un navigateur ouvert
    Quand On charge une page web <url>
    Alors Elle s'affiche
    Exemples:
      | url                               |
      | "https://www.google.com/"         |
      | "http://www.chezmoicamarche.org/" |

  Plan du Scénario: Calculatrice
    Étant donné La calculatrice ouverte dans un navigateur
    Quand On rempli le formulaire avec <a>, <b> et on sélectionne l'opération <op>
    Alors Elle affiche le calcul <calcul>
    Exemples:
      | a   | b   | op             | calcul        |
      | 12  | -8  | Addition       | 12 + -8 = 4   |
      | -4  | 10  | Soustraction   | -4 - 10 = -14 |
      | 0   | 999 | Multiplication | 0 * 999 = 0   |
      | 25  | 5   | Division       | 25 / 5 = 5.0  |
