from sys import exit
from pygame import display, quit, init
from state import Game, Menu, CharacterSelect, Story


class Main:
    """
    Main class that manage all game windows
    """

    def __init__(self) -> None:
        init()
        self.menu = Menu()
        self.selector = CharacterSelect()
        self.story = Story()

    def run(self):
        """
        Method that loops the game
        """
        current_state = "menu"
        while True:
            if current_state == "menu":
                self.menu.update()
                display.update()
                result = self.menu.handle_events()
                if result == "start":
                    current_state = "char_select"
                elif result == "exit":
                    quit()
                    exit()

            elif current_state == "game":
                self.game = Game()
                self.game.run()
                if self.game.show_menu:
                    current_state = "menu"
                

            elif current_state == "char_select":
                self.selector.update()
                display.update()
                result = self.selector.handle_events()

                if result == "story":
                    current_state = "story"

            elif current_state == "story":
                self.story.update()
                display.update()
                result = self.story.handle_events()
                if result == "game":
                    current_state = "game"


if __name__ == "__main__":
    main = Main()
    main.run()
