from main_menu import MainMenu
from game import Game

menu = MainMenu()
choice = menu.run()

if choice == "start":
    Game().run()