from pygame import font, image, transform


class UI:
    """UI class
    """
    def __init__(self, screen) -> None:
        self.font = font.Font(None, 36)
        self.screen = screen
        self.ability_icons = [
            image.load("assets/abil_icons/bullet_strike.png").convert_alpha(),
            image.load("assets/abil_icons/heal.png").convert_alpha(),
            image.load("assets/abil_icons/lightning_strike.png").convert_alpha()
        ]
        self.stats_icons = [
            image.load("assets/stats/strength.png").convert_alpha(),
            image.load("assets/stats/dexterity.png").convert_alpha(),
            image.load("assets/stats/intelligent.png").convert_alpha()
        ]
        self.ability_icons = [transform.scale(icon, (50, 50)) for icon in self.ability_icons]
    
    def display_player_stats(self, player):
        player_stats_surface = self.font.render(f"Health: {player.health}/{player.max_health}", False, (255, 0, 0))
        player_stats_rect = player_stats_surface.get_rect(topleft=(10, 10))
        self.screen.blit(player_stats_surface, player_stats_rect)
        
        player_stats_surface = self.font.render(f"Experience: {player.experience}/{player.exp_to_next_level}", False, (255, 255, 255))
        player_stats_rect = player_stats_surface.get_rect(topleft=(10, 215))
        self.screen.blit(player_stats_surface, player_stats_rect)
        
        player_stats_surface = self.font.render(f"Level: {player.level}", False, (255, 255, 255))
        player_stats_rect = player_stats_surface.get_rect(topleft=(10, 40))
        self.screen.blit(player_stats_surface, player_stats_rect)
        
        player_stats_surface = self.font.render(f"Skill Points: {player.skill_points}", False, (255, 255, 255))
        player_stats_rect = player_stats_surface.get_rect(topleft=(10, 70))
        self.screen.blit(player_stats_surface, player_stats_rect)
        
        icon_size = 30
        icon_x = 50
        icon_y = 100
        stats_x = icon_x + icon_size + 10
        stats_y = 100
        for i, (icon, stat) in enumerate(zip(self.stats_icons, [player.strength, player.agility, player.intelligence])):
            icon_rect = icon.get_rect(topleft=(icon_x, icon_y + i * (icon_size + 10)))
            self.screen.blit(icon, icon_rect)
            stat_num_surface = self.font.render(f"{i+1}", False, (255, 255, 255))
            stat_num_rect = stat_num_surface.get_rect(topleft=(icon_x - 20, icon_y + i * (icon_size + 10)))
            self.screen.blit(stat_num_surface, stat_num_rect)
            stat_surface = self.font.render(f"{stat}", False, (255, 255, 255))
            stat_rect = stat_surface.get_rect(topleft=(stats_x, stats_y + i * (icon_size + 10)))
            self.screen.blit(stat_surface, stat_rect)

    def display_wave_info(self, game):
        """Draw info about game waves

        Args:
            game (Game): game instance
        """
        wave_surface = self.font.render(f"Wave: {game.enemy_wave}", False, (255,255,255))
        enemies_surface = self.font.render(f"Enemies: {game.living_enemies}", False, (255, 255, 255))
        wave_rect = wave_surface.get_rect(center=(self.screen.get_width() // 2, 10))
        enemies_rect = enemies_surface.get_rect(center=(self.screen.get_width() // 2, 40))
        self.screen.blit(wave_surface, wave_rect)
        self.screen.blit(enemies_surface, enemies_rect)
    def display_ability_icons(self, player):
        ability_icons = self.ability_icons
        ability_keys = ["Q", "E", "R"]
        ability_сooldowns = player.ability_cooldowns

        icon_size = 50
        icon_spacing = 20
        icon_x = self.screen.get_width() // 2 - (icon_size + icon_spacing) * len(ability_icons) // 2
        icon_y = self.screen.get_height() - icon_size - 50

        for i, icon in enumerate(ability_icons):
            icon_rect = icon.get_rect(center=(icon_x + i * (icon_size + icon_spacing), icon_y))
            self.screen.blit(icon, icon_rect)
            cooldown = ability_сooldowns.get(ability_keys[i].lower())
            if cooldown > 0:
                cooldown_seconds = int(cooldown / 60)
                cooldown_surface = self.font.render(str(cooldown_seconds), False, (255, 0, 0))
                cooldown_rect = cooldown_surface.get_rect(center=icon_rect.center)
                self.screen.blit(cooldown_surface, cooldown_rect)

            key_surface = self.font.render(ability_keys[i], False, (255, 255, 255))
            key_rect = key_surface.get_rect(midbottom=icon_rect.midtop)
            self.screen.blit(key_surface, key_rect)
    
    def update(self, player, game):
        """Screen and events update
        Args:
            player (Player): player instance
            game (Game): game instance
        """
        self.display_player_stats(player)
        self.display_wave_info(game)
        self.display_ability_icons(player)