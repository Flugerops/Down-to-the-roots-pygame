from pygame import display, draw, event, MOUSEBUTTONDOWN, QUIT, time, font, Rect, image, transform, quit, mixer
from settings import WIDTH, HEIGHT


class Menu:
    def __init__(self):
        self.screen = display.set_mode((WIDTH, HEIGHT))
        display.set_caption("Down to the roots")
        self.clock = time.Clock()
        self.font = font.Font("assets/fonts/NewAmsterdam-Regular.ttf", 36)
        self.title_font = font.Font("assets/fonts/NewAmsterdam-Regular.ttf", 64)
        self.start_button = Rect(WIDTH / 2 - 100, HEIGHT / 2 - 50, 200, 50)
        self.exit_button = Rect(WIDTH / 2 - 100, HEIGHT / 2 + 50, 200, 50)
        self.background = image.load("assets/level/large_bg.png").convert()
        self.background = transform.scale(self.background, (WIDTH, HEIGHT))

    def update(self):
        self.screen.blit(self.background, (0, 0))
        title_text = self.title_font.render("Down To The Roots", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(WIDTH / 2, 100))
        self.screen.blit(title_text, title_rect)
        
        start_text = self.font.render("Start", True, (255, 255, 255))
        start_rect = start_text.get_rect(center=self.start_button.center)
        self.screen.blit(start_text, start_rect)
        
        exit_text = self.font.render("Exit", True, (255, 255, 255))
        exit_rect = exit_text.get_rect(center=self.exit_button.center)
        self.screen.blit(exit_text, exit_rect)

        draw.rect(self.screen, (255, 255, 255), self.start_button, 2)
        draw.rect(self.screen, (255, 255, 255), self.exit_button, 2)


    def handle_events(self):
        for ev in event.get():
            if ev.type == QUIT:
                quit()
                exit()
            if ev.type == MOUSEBUTTONDOWN:
                if self.start_button.collidepoint(ev.pos):
                    return "start"
                if self.exit_button.collidepoint(ev.pos):
                    return "exit"
        return "menu"

class CharacterSelect:
    def __init__(self):
        self.screen = display.set_mode((WIDTH, HEIGHT))
        self.clock = time.Clock()
        self.font = font.Font("assets/fonts/NewAmsterdam-Regular.ttf", 36)
        self.title_font = font.Font("assets/fonts/NewAmsterdam-Regular.ttf", 64)
        self.background = image.load("assets/level/large_bg.png").convert()
        self.background = transform.scale(self.background, (WIDTH, HEIGHT))
        self.characters = [
            {"name": "Stickman", "description": "Weak and sick :)", "image": image.load("assets/chars_menu/stickman.png")},
            {"name": "Leaf Ranger", "description": "Wise and nimble", "image": image.load("assets/chars_menu/leaf_ranger.png"), "broken_image": image.load("assets/chars_menu/broken_leaf.png")},
            {"name": "Warrior", "description": "Strong and brave", "image": image.load("assets/chars_menu/fire_knight.png"), "broken_image": image.load("assets/chars_menu/fire_broken.png")},
        ]
        self.character_buttons = [
            Rect(WIDTH / 2 - 250, HEIGHT / 2 - 300, 200, 200),
            Rect(WIDTH / 2 - 25, HEIGHT / 2 - 50, 200, 200),
            Rect(WIDTH / 2 + 200, HEIGHT / 2 + 200, 200, 200),
        ]
        self.broken_characters = [False, False, False]
        self.broken_sound = mixer.Sound("assets/sounds/glass_hit.mp3")
        self.troll_text = ["You can't handle this power!", "Not for you mortal!"]

    def update(self):
        self.screen.blit(self.background, (0, 0))
        title_text = self.title_font.render("Select character that most similar to you", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(WIDTH / 2, 50))
        self.screen.blit(title_text, title_rect)
        for i, character in enumerate(self.characters):
            draw.rect(self.screen, (128, 128, 128), self.character_buttons[i], 0)
            draw.rect(self.screen, (255, 255, 255), self.character_buttons[i], 2)
            if self.broken_characters[i]:
                broken_image = transform.scale(character.get("broken_image"), (200, 200))
                self.screen.blit(broken_image, self.character_buttons[i])
                text = self.font.render(self.troll_text[i-1], True, (255, 255, 255))
                text_rect = text.get_rect(center=(self.character_buttons[i].centerx, self.character_buttons[i].top - 20))
                self.screen.blit(text, text_rect)
            else:
                char_image = transform.scale(character.get("image"), (200, 200))
                self.screen.blit(char_image, self.character_buttons[i])
            name_text = self.font.render(character.get("name"), True, (255, 255, 255))
            name_rect = name_text.get_rect(center=(self.character_buttons[i].centerx, self.character_buttons[i].bottom + 40))
            self.screen.blit(name_text, name_rect)
            description_text = self.font.render(character.get("description"), True, (255, 255, 255))
            description_rect = description_text.get_rect(center=(self.character_buttons[i].centerx, self.character_buttons[i].bottom + 70))
            self.screen.blit(description_text, description_rect)
        
    def handle_events(self):
        for ev in event.get():
            if ev.type == QUIT:
                quit()
                exit()
            if ev.type == MOUSEBUTTONDOWN:
                for i, button in enumerate(self.character_buttons):
                    if button.collidepoint(ev.pos):
                        if i > 0:
                            self.broken_characters[i] = True
                            self.broken_sound.play()
                        elif i == 0:
                            return "story"

        return "character_select"
    
