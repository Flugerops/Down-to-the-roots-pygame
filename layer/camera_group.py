from pygame import sprite, image, Vector2, transform
from settings import WIDTH, HEIGHT
from layer import all_sprites_group


class Camera(sprite.Group):
    """Camera group that implements camera
    to the game
    """

    def __init__(self, background):
        super().__init__()
        self.offset = Vector2()
        self.background = background
        self.floor_rect = background.get_rect(topleft=(0, 0))
        self.large_bg = transform.scale(image.load(
            "assets/level/hell_bg.png").convert(), (2500, 1500))

    def custom_draw(self, player, screen):
        """Custom screen draw
        """
        screen.blit(self.large_bg, (0, 0))
        self.offset.x = player.rect.centerx - WIDTH // 2
        self.offset.y = player.rect.centery - HEIGHT // 2
        floor_offset_pos = self.floor_rect.topleft - self.offset
        screen.blit(self.background, floor_offset_pos)
        for sprite in all_sprites_group:
            offset_pos = sprite.rect.topleft - self.offset
            screen.blit(sprite.image, offset_pos)
