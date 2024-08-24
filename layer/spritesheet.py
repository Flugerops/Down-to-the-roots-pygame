from pygame import Surface, transform, time


class Spritesheet:
    """Class that handles spritesheet
    """

    def __init__(self, sheet, animation_speed: int, delay: int) -> None:
        self.sheet = sheet
        self.frame = 0
        self.animation_speed = animation_speed
        self.delay = delay
        self.last_frame_time = time.get_ticks()

    def get_image(self, frame: int, width: int, height: int, scale: float, colour: tuple):
        """Get image from spritesheet

        Args:
            frame (int): your frame step
            width (int): your sprite width
            height (int): your sprite height
            scale (float): how much scale your sprite
            colour (tuple): tuple of colour info

        Returns:
            image
        """
        image = Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image = transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(colour)
        return image

    def play_animation(self, width: int, height: int, scale: float, colour: tuple):
        """Play whole animation from spritesheet

        Args:
            width (int): width of single sprite
            height (int): height of single sprite
            scale (float): how much scale sprites
            colour (tuple): tuple of colout information
        """
        current_time = time.get_ticks()
        if current_time - self.last_frame_time >= self.delay:
            self.frame += self.animation_speed
            if self.frame >= self.sheet.get_width() // width:
                self.frame = 0
            self.last_frame_time = current_time
        return self.get_image(self.frame, width, height, scale, colour)
