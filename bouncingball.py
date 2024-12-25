import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Ball properties
BALL_RADIUS = 20

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bouncing Ball")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Function to generate a random color
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Ball class
class Ball:
    def __init__(self, x, y, dx, dy, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def check_collision(self):
        if self.x - BALL_RADIUS <= 0 or self.x + BALL_RADIUS >= SCREEN_WIDTH:
            self.dx = -self.dx
            return True

        if self.y - BALL_RADIUS <= 0 or self.y + BALL_RADIUS >= SCREEN_HEIGHT:
            self.dy = -self.dy
            return True

        return False

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), BALL_RADIUS)

# Initialize the first ball
balls = [Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 5, 5, WHITE)]

# Score
score = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Update and draw each ball
    for ball in balls:
        ball.move()
        if ball.check_collision():
            score += 1  # Increment score on collision
            ball.color = random_color()  # Change the color of the ball
        ball.draw(screen)

    # Display the score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
