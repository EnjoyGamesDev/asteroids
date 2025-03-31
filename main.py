import pygame
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_caption("Asteroids")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock =  pygame.time.Clock()
    dt = 0
    points = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    # Function to draw the points
    text_font = pygame.font.SysFont(None, 30)
    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))  

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        
        # Loop through all asteroids and check if the player collides with  any of them.
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                exit()
        
        # Check if a shot (bullet) has collision with an asteroid,
        # then delete that asteroid and the bullet        
            for shot in shots:
                if shot.collision(asteroid):
                    points += 1
                    shot.kill()
                    asteroid.split()
                        
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
        
        draw_text(f"Points: {points}", text_font, "white", 15, 15)
        fps = clock.get_fps()
        draw_text(f"FPS: {fps:.2f}", text_font, "white", 15, 50)
        pygame.display.flip()
        
        # Limit the framerate to 60
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()