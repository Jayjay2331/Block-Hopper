import pygame
from admin import game_settings  # Import live settings from admin panel

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2-Player Platformer")

clock = pygame.time.Clock()
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)

PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50

class Player:
    def __init__(self, x, y, color, keys):
        self.rect = pygame.Rect(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.color = color
        self.vel_y = 0
        self.on_ground = False
        self.keys = keys

    def handle_input(self):
        keys = pygame.key.get_pressed()
        speed = game_settings["player_speed"]  # Read live speed
        if keys[self.keys['left']]:
            self.rect.x -= speed
        if keys[self.keys['right']]:
            self.rect.x += speed
        if keys[self.keys['jump']] and self.on_ground:
            self.vel_y = -game_settings["jump_strength"]
            self.on_ground = False

    def apply_gravity(self):
        self.vel_y += game_settings["gravity"]
        self.rect.y += self.vel_y

    def check_platform_collision(self, platforms):
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform) and self.vel_y >= 0:
                self.rect.bottom = platform.top
                self.vel_y = 0
                self.on_ground = True

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

# Platforms
platforms = [
    pygame.Rect(0, HEIGHT - 50, WIDTH, 50),
    pygame.Rect(200, 450, 150, 20),
    pygame.Rect(400, 350, 150, 20),
    pygame.Rect(600, 250, 150, 20),
]

# Players
player1 = Player(100, HEIGHT - 100, BLUE, {'left': pygame.K_a, 'right': pygame.K_d, 'jump': pygame.K_w})
player2 = Player(200, HEIGHT - 100, RED, {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT, 'jump': pygame.K_UP})

# Game loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for player in [player1, player2]:
        player.handle_input()
        player.apply_gravity()
        player.check_platform_collision(platforms)
        player.draw(screen)

    for platform in platforms:
        pygame.draw.rect(screen, GREEN, platform)

    pygame.display.flip()

pygame.quit()
