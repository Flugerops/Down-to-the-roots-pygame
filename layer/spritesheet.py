from pygame import Surface, transform


class Spritesheet:
    def __init__(self, sheet) -> None:
        self.sheet = sheet
        
    def get_image(self, frame, width, height, scale, colour):
        image = Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image = transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(colour)
        return image