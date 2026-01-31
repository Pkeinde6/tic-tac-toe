class Board:
    """Gère le plateau de jeu Tic Tac Toe"""
    
    def __init__(self):
        self.grid = [' ' for _ in range(9)]  # Cases 1-9
    
    def print_board(self):
        """Affiche le plateau de jeu"""
        print("\n")
        print(f" {self.grid[0]} | {self.grid[1]} | {self.grid[2]}")
        print("---+---+---")
        print(f" {self.grid[3]} | {self.grid[4]} | {self.grid[5]}")
        print("---+---+---")
        print(f" {self.grid[6]} | {self.grid[7]} | {self.grid[8]}")
        print("\n")
    
    def print_positions(self):
        """Affiche les numéros des positions disponibles"""
        print("\nNuméros des positions:")
        print(" 1 | 2 | 3")
        print("---+---+---")
        print(" 4 | 5 | 6")
        print("---+---+---")
        print(" 7 | 8 | 9\n")
    
    def make_move(self, position, player_symbol):
        """
        Place le symbole du joueur à la position spécifiée
        Position: 1-9 (1-indexé pour l'utilisateur, 0-indexé en interne)
        Retourne: True si le coup est valide, False sinon
        """
        if position < 1 or position > 9:
            return False
        
        index = position - 1
        if self.grid[index] != ' ':
            return False
        
        self.grid[index] = player_symbol
        return True
    
    def is_empty(self, position):
        """Vérifie si une position est vide"""
        return self.grid[position - 1] == ' '
    
    def is_full(self):
        """Vérifie si le plateau est plein"""
        return ' ' not in self.grid
    
    def check_winner(self, player_symbol):
        """
        Vérifie si le joueur a gagné
        Retourne: True si gagnant, False sinon
        """
        # Combinaisons gagnantes (indices 0-8)
        winning_combos = [
            [0, 1, 2],  # Ligne du haut
            [3, 4, 5],  # Ligne du milieu
            [6, 7, 8],  # Ligne du bas
            [0, 3, 6],  # Colonne gauche
            [1, 4, 7],  # Colonne milieu
            [2, 5, 8],  # Colonne droite
            [0, 4, 8],  # Diagonale \
            [2, 4, 6],  # Diagonale /
        ]
        
        for combo in winning_combos:
            if all(self.grid[i] == player_symbol for i in combo):
                return True
        return False
    
    def reset(self):
        """Réinitialise le plateau"""
        self.grid = [' ' for _ in range(9)]
