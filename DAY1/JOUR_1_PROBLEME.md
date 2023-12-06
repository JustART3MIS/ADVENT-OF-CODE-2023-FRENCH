# --- Jour 1: Trebuchet?! ---

Quelque chose ne va pas avec la production mondiale de neige, et vous avez été sélectionné pour jeter un oeil. Les elfes vous ont même donné une carte; sur elle, ils ont utilisé des étoiles pour marquer les cinquante premiers endroits qui sont susceptibles d’avoir des problèmes.

Vous le faites depuis assez longtemps pour savoir que pour réparer les chutes de neige, vous devez gagner les **cinquante étoiles** d’ici le 25 décembre.

Collecter des étoiles en résolvant des énigmes.  Deux puzzles seront disponibles chaque jour dans le calendrier de l’Avent; le deuxième puzzle est débloqué lorsque vous terminez le premier.  Chaque puzzle octroie **une étoile**. Bonne chance!

Vous essayez de demander pourquoi ils ne peuvent pas simplement utiliser une [machine météorologique](https://adventofcode.com/2015/day/1) (« pas assez puissant ») et où ils vous envoient même (« le ciel ») et pourquoi votre carte semble principalement vide (« Vous posez certainement beaucoup de questions ») *et* attendez, vous venez de dire le ciel ? (« Bien sûr, d’où pensez-vous que vient la neige »). Puis, vous vous rendez compte que les elfes vous chargent déjà dans un [trébuchet](https://en.wikipedia.org/wiki/Trebuchet) (« Ne bougez pas, nous devons vous attacher »).

Pendant qu’ils font les derniers ajustements, ils découvrent que leur document d’étalonnage (votre entrée de puzzle) a été **modifié** par un très jeune elfe qui était apparemment juste excité de montrer ses compétences artistiques. Par conséquent, les Elfes ont du mal à lire les valeurs sur le document.

Le document d’étalonnage nouvellement amélioré se compose de lignes de texte; chaque ligne contenait à l’origine une **valeur d’étalonnage** spécifique que les Elfes doivent maintenant récupérer. Sur chaque ligne, la valeur d’étalonnage peut être trouvée en combinant le **premier chiffre** et le **dernier chiffre** (dans cet ordre) pour former un seul **nombre à deux chiffres**.

Par exemple :
```
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
```

Dans cet exemple, les valeurs de calibration de ces quatre lignes sont `12`, `38`, `15` et `77`. En les additionnant, on obtient `142`.

En prenant en compte l'entièreté de votre document de calibration, **quelle est la somme des valeurs de calibration ?**

## --- Partie Deux ---

Votre calcul n'est pas encore bon. On dirait que certains des chiffres sont en fait **écrits en lettres**: `one` 1, `two` 2, `three` 3, `four` 4, `five` 5, `six` 6, `seven` 7, `eight` 8, and `nine` 9 **comptent aussi** comme des chiffres valides !

En prenant compte de ces nouvelles informations, vous devez désormais trouver les vrais premiers et derniers chiffres de chaque ligne. Par exemple :

```
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
```

Dans cet exemple, les valeurs de calibration sont `29`, `83`, `13`, `24`, `42`, `14`, et `76`. En les additionnant, on obtient `281`.

**Que vaut la somme des valeurs de calibration ?**
