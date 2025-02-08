from pong import PongGame
import pygame
import numpy as np


class PongRL(PongGame):
    def __init__(self, SCREEN_WIDTH=1280, SCREEN_HEIGHT=800):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.reward = 0
        self.done = False

    def reset(self):
        self.ball.center = self.screen.get_rect().center
        self.ball_speed_x = 6 * np.random.choice([-1, 1])
        self.ball_speed_y = 6 * np.random.choice([-1, 1])

        self.player_left.centery = self.screen.get_rect().centery
        self.player_right.centery = self.screen.get_rect().centery

        self.reward = 0
        self.done = False

    def handle_keydown(self, event):
        # if event.key == pygame.K_UP:
        #     self.player_right.speed = -self.player_speed_increment
        # if event.key == pygame.K_DOWN:
        #     self.player_right.speed = self.player_speed_increment
        if event.key == pygame.K_w:
            self.player_left.speed = -self.player_speed_increment
        if event.key == pygame.K_s:
            self.player_left.speed = self.player_speed_increment

    def handle_keyup(self, event):
        # if event.key == pygame.K_UP:
        #     self.player_right.speed = 0
        # if event.key == pygame.K_DOWN:
        #     self.player_right.speed = 0
        if event.key == pygame.K_w:
            self.player_left.speed = 0
        if event.key == pygame.K_s:
            self.player_left.speed = 0


    def step(self, action):
        if action == 1:
            self.player_right.speed = -self.player_speed_increment
        elif action == -1:
            self.player_right.speed = self.player_speed_increment
        else:
            self.player_right.speed = 0
        
        self.animate_ball()
        self.animate_players()

        state = self.get_state()
        return state, self.reward, self.done
    
    def state(self):
        return np.array([
            self.ball.x, self.ball.y,
            self.ball_speed_x, self.ball_speed_y,
            self.player_left.y, self.player_right.y
            ], dtype=np.float32)

    def animate_ball(self):
        self.ball.x += self.ball_speed_x
        self.ball.y += self.ball_speed_y

        if self.ball.bottom >= self.screen.get_height() or self.ball.top <= 0:
            self.ball_speed_y *= -1
        
        if self.ball.colliderect(self.player_left):
            self.ball_speed_x *= -1
            self.reward = -1
        elif self.ball.colliderect(self.player_right):
            self.ball_speed_x *= -1
            self.reward = 1
        



if __name__ == "__main__":
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 800
    game = PongRL(SCREEN_WIDTH, SCREEN_HEIGHT)
    initial_state = game.reset()
    game.run()




