from pygame import sprite, display, image, math, Vector2
from settings import WIDTH, HEIGHT
from layer import all_sprites_group


class Camera(sprite.Group):
    def __init__(self, background):
        super().__init__()
        self.offset = Vector2()
        self.background = background
        self.floor_rect = background.get_rect(topleft = (0, 0))

    def custom_draw(self, player, screen):
        self.offset.x = player.rect.centerx - WIDTH // 2
        self.offset.y = player.rect.centery - HEIGHT // 2
        floor_offset_pos = self.floor_rect.topleft - self.offset
        screen.blit(self.background, floor_offset_pos)

        for sprite in all_sprites_group:
            offset_pos = sprite.rect.topleft - self.offset
            screen.blit(sprite.image, offset_pos)