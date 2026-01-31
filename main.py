#!/usr/bin/env python3
"""
Jeu de Tic Tac Toe (Morpion)
Joueur 1 (X) vs Joueur 2 (O)
"""

from game import Game


def main():
    """Boucle principale du jeu"""
    print("=" * 40)
    print("  BIENVENUE AU TIC TAC TOE!")
    print("=" * 40)
    
    game = Game()
    game.board.print_positions()
    
    while True:
        game.display_status()
        
        # Récupérer l'entrée du joueur
        while True:
            try:
                move = int(input(f"Joueur {game.current_player}, entrez la position (1-9): "))
                success, message = game.play_move(move)
                if success:
                    break
                else:
                    print(f"❌ {message}")
            except ValueError:
                print("❌ Entrée invalide. Veuillez entrer un nombre entre 1 et 9.")
        
        # Vérifier si le jeu est terminé
        game_over, winner, reason = game.check_game_over()
        if game_over:
            game.board.print_board()
            print("=" * 40)
            print(reason)
            print("=" * 40)
            break
        
        # Passer au joueur suivant
        game.switch_player()
    
    # Demander s'il faut rejouer
    while True:
        replay = input("\nVoulez-vous rejouer? (o/n): ").lower()
        if replay in ['o', 'oui', 'yes', 'y']:
            game.reset()
            main()
            return
        elif replay in ['n', 'non', 'no']:
            print("Merci d'avoir joué! Au revoir!")
            return
        else:
            print("Veuillez répondre par 'o' ou 'n'")


if __name__ == "__main__":
    main()
