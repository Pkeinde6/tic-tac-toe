# Tic Tac Toe

Un jeu de morpion (Tic Tac Toe) classique en Python avec interface en ligne de commande.

## Fonctionnalités

- Jeu PvP (joueur vs joueur)
- Affichage du plateau de jeu intuitif
- Vérification automatique des victoires et des matchs nuls
- Système de tours alternés

## Comment jouer

```bash
python main.py
```

### Règles

- Le plateau est une grille 3x3 numérotée de 1 à 9
- Le joueur 1 commence avec des "X", le joueur 2 joue avec des "O"
- Pour placer un symbole, saisissez le numéro de la case (1-9)
- Le premier à aligner 3 symboles (horizontal, vertical ou diagonal) gagne
- Si toutes les cases sont remplies, c'est un match nul

## Structure du projet

```
.
├── main.py         # Point d'entrée du jeu
├── game.py         # Logique principale du jeu
├── board.py        # Gestion du plateau
└── README.md       # Ce fichier
```

## Améliorations futures

- Mode IA (vs ordinateur)
- Interface graphique (Tkinter/PyQt)
- Sauvegarde des scores
- Mode en ligne avec sockets

## Licence

MIT
