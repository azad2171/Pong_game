import pygame
import sys

class Player(pygame.Rect):
    def __init__(self, left, top, width, height):
        super().__init__(left, top, width, height)
        # self.paddle = pygame.Rect(0, 0, 30, 30)
        # self.left, self.top, self.width, self.height = 0, 0, 30, 30
        self.score = 0
        self.speed = 0

class PongGame:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.ball = pygame.Rect(0, 0, 30, 30)
        self.ball.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.ball_speed_x = 6
        self.ball_speed_y = 6

        self.player_left = Player(0, 0, 20, 100)
        self.player_right = Player(0, 0, 20, 100)

        self.player_left.midleft = (5, SCREEN_HEIGHT / 2)
        self.player_right.midright = (SCREEN_WIDTH - 5, SCREEN_HEIGHT / 2)

        self.player_speed_increment = 6

        

    def run(self):
        while True:
            self.handle_events()
            self.animate_ball()
            self.animate_players()
            self.draw_objects()
            pygame.display.update()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.handle_keydown(event)
            if event.type == pygame.KEYUP:
                self.handle_keyup(event)

    def handle_keydown(self, event):
        if event.key == pygame.K_UP:
            self.player_right.speed = -self.player_speed_increment
        if event.key == pygame.K_DOWN:
            self.player_right.speed = self.player_speed_increment
        if event.key == pygame.K_w:
            self.player_left.speed = -self.player_speed_increment
        if event.key == pygame.K_s:
            self.player_left.speed = self.player_speed_increment

    def handle_keyup(self, event):
        if event.key == pygame.K_UP:
            self.player_right.speed = 0
        if event.key == pygame.K_DOWN:
            self.player_right.speed = 0
        if event.key == pygame.K_w:
            self.player_left.speed = 0
        if event.key == pygame.K_s:
            self.player_left.speed = 0

    def animate_ball(self):
        self.ball.x += self.ball_speed_x
        self.ball.y += self.ball_speed_y

        if self.ball.bottom >= self.screen.get_width() or self.ball.top <= 0:
            self.ball_speed_y *= -1

        if self.ball.colliderect(self.player_left) or self.ball.colliderect(self.player_right):
            self.ball_speed_x *= -1

    def animate_players(self):
        self.player_left.y += self.player_left.speed
        self.player_right.y += self.player_right.speed

        if self.player_left.top <= 0:
            self.player_left.top = 0

        if self.player_left.bottom >= self.screen.get_height():
            self.player_left.bottom = self.screen.get_height()

        if self.player_right.top <= 0:
            self.player_right.top = 0

        if self.player_right.bottom >= self.screen.get_height():
            self.player_right.bottom = self.screen.get_height()

    def draw_objects(self):
        self.screen.fill('black')
        pygame.draw.aaline(self.screen, 'white', (self.screen.get_width() / 2, 0), (self.screen.get_width() / 2, self.screen.get_height()))
        pygame.draw.ellipse(self.screen, 'white', self.ball)
        pygame.draw.rect(self.screen, 'red', self.player_left)
        pygame.draw.rect(self.screen, 'red', self.player_right)

if __name__ == "__main__":
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 800
    game = PongGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.run()
