# from pygame import sprite, math, display, image, Vector2
# from settings import WIDTH, HEIGHT
# from layer import all_sprites_group


# class Camera(sprite.Sprite):
#     def __init__(self, player, screen) -> None:
#         super().__init__()
#         self.offset = math.Vector2()
#         self.screen = screen
#         self.player = player
#         self.background = image.load("assets/level/ground.png").convert_alpha()
#         self.floor_rect = self.background.get_rect(topleft=(0,0))

        
#     def custom_draw(self):
#         self.offset.x = self.player.rect.centerx - self.screen.get_width() // 2
#         self.offset.y = self.player.rect.centery - self.screen.get_height() // 2 
        
#         floor_offset_pos = self.floor_rect.topleft - self.offset
#         self.screen.blit(self.background, floor_offset_pos)
        
#         for sprite in all_sprites_group:
#             offset_pos = sprite.rect.topleft - self.offset
#             self.screen.blit(sprite.image, offset_pos)

            
# # class Camera(sprite.Sprite):
# #     def __init__(self) -> None:
# #         super().__init__()
# #         self.display_surface = display.get_surface()
# #         self.offset = Vector2()
# #         self.ground_surface = image.load("assets/level/ground.png").convert_alpha()
# #         self.ground_rect = self.ground_surface.get_rect(topleft = (0, 0))
        
# #     def custom_draw(self):
# #         ground_offset = self.ground_rect.topleft + self.offset
# #         self.display_surface.blit(self.ground_rect, ground_offset)
        
# #         for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
# #             offset_pos = sprite.rect.topleft + self.offset
# #             self.display_surface.blit(sprite.image, offset_pos)