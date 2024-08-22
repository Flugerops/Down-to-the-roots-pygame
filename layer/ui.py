from pygame import font


class UI:
    def __init__(self, screen) -> None:
        self.font = font.Font(None, 36)
        self.screen = screen
    
    def display_player_stats(self, player):
        player_stats_surface = self.font.render(f"Health: {player.health}/{player.max_health}", False, (255, 0, 0))
        player_stats_rect = player_stats_surface.get_rect(topleft=(10, 40))
        self.screen.blit(player_stats_surface, player_stats_rect)
        
        player_stats_surface = self.font.render(f"Experience: {player.experience}/{player.exp_to_next_level}", False, (255, 255, 255))
        player_stats_rect = player_stats_surface.get_rect(topleft=(10, 190))
        self.screen.blit(player_stats_surface, player_stats_rect)
        
        player_stats_surface = self.font.render(f"Level: {player.level}", False, (255, 255, 255))
        player_stats_rect = player_stats_surface.get_rect(topleft=(10, 10))
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
    
    def display_wave_info(self, game):
        wave_surface = self.font.render(f"Wave: {game.enemy_wave}", False, (255,255,255))
        enemies_surface = self.font.render(f"Enemies: {game.living_enemies}", False, (255, 255, 255))
        
        wave_rect = wave_surface.get_rect(center=(self.screen.get_width() // 2, 10))
        enemies_rect = enemies_surface.get_rect(center=(self.screen.get_width() // 2, 40))
        
        self.screen.blit(wave_surface, wave_rect)
        self.screen.blit(enemies_surface, enemies_rect)
    
    def update(self, player, game):
        self.display_player_stats(player)
        self.display_wave_info(game)