from board import Board


class Game:
    """Gère la logique principale du jeu Tic Tac Toe"""
    
    def __init__(self):
        self.board = Board()
        self.current_player = 1
        self.player_symbols = {1: 'X', 2: 'O'}
    
    def switch_player(self):
        """Passe au joueur suivant"""
        self.current_player = 2 if self.current_player == 1 else 1
    
    def get_current_symbol(self):
        """Retourne le symbole du joueur actuel"""
        return self.player_symbols[self.current_player]
    
    def play_move(self, position):
        """
        Effectue un coup
        Retourne: (succès: bool, message: str)
        """
        if not isinstance(position, int) or position < 1 or position > 9:
            return False, "Position invalide. Entrez un nombre entre 1 et 9."
        
        if not self.board.is_empty(position):
            return False, f"La case {position} est déjà occupée!"
        
        symbol = self.get_current_symbol()
        self.board.make_move(position, symbol)
        return True, "Coup joué avec succès"
    
    def check_game_over(self):
        """
        Vérifie l'état du jeu
        Retourne: (game_over: bool, winner: int ou None, reason: str)
        """
        # Vérifier les victoires
        for player in [1, 2]:
            if self.board.check_winner(self.player_symbols[player]):
                return True, player, f"Joueur {player} ({self.player_symbols[player]}) a gagné!"
        
        # Vérifier le match nul
        if self.board.is_full():
            return True, None, "Match nul!"
        
        return False, None, ""
    
    def reset(self):
        """Réinitialise le jeu"""
        self.board.reset()
        self.current_player = 1
    
    def display_status(self):
        """Affiche l'état actuel du jeu"""
        self.board.print_board()
        print(f"Tour du Joueur {self.current_player} ({self.get_current_symbol()})")
