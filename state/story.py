from pygame import display, draw, event, MOUSEBUTTONDOWN, QUIT, time, font, Rect, image, transform, quit, mixer
from settings import WIDTH, HEIGHT


class Story:
    def __init__(self):
        self.screen = display.set_mode((WIDTH, HEIGHT))
        display.set_caption("Down to the roots")
        self.clock = time.Clock()
        self.font = font.Font("assets/fonts/NewAmsterdam-Regular.ttf", 36)
        self.text_lines = [
            "In the depths of the roots, the fallen ones can regain their lives.",
            "Will you be able to withstand the trials and emerge victorious?"
        ]
        self.text_surfaces = [self.font.render(text, True, (255, 255, 255)) for text in self.text_lines]
        self.rects = [text_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 50)) for text_surface in self.text_surfaces]
        self.rects[1].centery = HEIGHT / 2 + 20
        self.background = image.load("assets/level/large_bg.png").convert()
        self.background = transform.scale(self.background, (WIDTH, HEIGHT))
        self.continue_button = Rect(WIDTH / 2 - 100, HEIGHT / 2 + 100, 200, 50)
        self.alpha = 0
        self.timer = 0

    def update(self):
        self.screen.blit(self.background, (0, 0))
        if self.timer < 5 * 60:
            self.timer += 1
            self.alpha = int(255 * (self.timer / (5 * 60)))
            for i, text_surface in enumerate(self.text_surfaces):
                text_surface.set_alpha(self.alpha)
                self.screen.blit(text_surface, self.rects[i])
        else:
            for i, text_surface in enumerate(self.text_surfaces):
                self.screen.blit(text_surface, self.rects[i])
        draw.rect(self.screen, (255, 255, 255), self.continue_button, 2)
        continue_text = self.font.render("Continue", True, (255, 255, 255))
        continue_rect = continue_text.get_rect(center=self.continue_button.center)
        self.screen.blit(continue_text, continue_rect)

    def handle_events(self):
        for ev in event.get():
            if ev.type == QUIT:
                quit()
                exit()
            if ev.type == MOUSEBUTTONDOWN:
                if self.continue_button.collidepoint(ev.pos):
                    return "game"
        return "story"