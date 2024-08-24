from sys import exit
from pygame import init, quit, display
from state import Game, Menu, CharacterSelect, Story


class Main:
    def __init__(self) -> None:
        init()
        self.menu = Menu()
        self.game = Game()
        self.selector = CharacterSelect()
        self.story = Story()

    def run(self):
        current_state = "menu"
        while True:
            if current_state == "menu":
                self.game.background_music.stop()
                self.menu.update()
                display.update()
                result = self.menu.handle_events()
                if result == "start":
                    current_state = "char_select"
                elif result == "exit":
                    quit()
                    exit()

            elif current_state == "game":
                self.game.background_music.play()
                self.game.run()

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
