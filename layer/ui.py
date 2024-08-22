from pygame import font


class UI:
    def __init__(self, screen) -> None:
        self.font = font.Font(None, 36)
        self.screen = screen
    
    def display_player_stats(self, player):
        player_stats_surface = self.font.render(f"Level: {player.level}", False, (255, 255, 255))
        player_stats_rect = player_stats_surface.get_rect(topleft=(10, 10))
        self.screen.blit(player_stats_surface, player_stats_rect)
        
        player_stats_surface = self.font.render(f"Health: {player.health}/{player.max_health}", False, (255, 0, 0))
        player_stats_rect = player_stats_surface.get_rect(topleft=(10, 40))
        self.screen.blit(player_stats_surface, player_stats_rect)

        player_stats_surface = self.font.render(f"Skill Points: {player.skill_points}", False, (255, 255, 255))
        player_stats_rect = player_stats_surface.get_rect(topleft=(10, 70))
        self.screen.blit(player_stats_surface, player_stats_rect)
        
        player_stats_surface = self.font.render(f"Strength: {player.strength}", False, (255, 255, 255))
        player_stats_rect = player_stats_surface.get_rect(topleft=(10, 100))
        self.screen.blit(player_stats_surface, player_stats_rect)

        player_stats_surface = self.font.render(f"Agility: {player.agility}", False, (255, 255, 255))
        player_stats_rect = player_stats_surface.get_rect(topleft=(10, 130))
        self.screen.blit(player_stats_surface, player_stats_rect)
        
        player_stats_surface = self.font.render(f"Intelligence: {player.intelligence}", False, (255, 255, 255))
        player_stats_rect = player_stats_surface.get_rect(topleft=(10, 160))
        self.screen.blit(player_stats_surface, player_stats_rect)
    
    def update(self, player):
        self.display_player_stats(player)