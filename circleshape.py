import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    # Check if two shapes are colliding
    def collision(self, otherShape):
        # Calculate the distance between the centers of the two shapes.
        # If the distance is less than or equal to the sum of their radii, a collision has occurred.
        # Otherwise, return False (no collision).
        return pygame.Vector2.distance_to(self.position, otherShape.position) <= (self.radius + otherShape.radius)
