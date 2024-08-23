from pygame import Surface, transform, time


class Spritesheet:
    def __init__(self, sheet, animation_speed, delay) -> None:
        self.sheet = sheet
        self.frame = 0
        self.animation_speed = animation_speed
        self.delay = delay
        self.last_frame_time = time.get_ticks()
        
    def get_image(self, frame, width, height, scale, colour):
        image = Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image = transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(colour)
        return image
    
    def play_animation(self, width, height, scale, colour):
        current_time = time.get_ticks()
        if current_time - self.last_frame_time >= self.delay:
            self.frame += self.animation_speed
            if self.frame >= self.sheet.get_width() // width:
                self.frame = 0
            self.last_frame_time = current_time
        return self.get_image(self.frame, width, height, scale, colour)