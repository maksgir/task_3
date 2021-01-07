import pygame
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)

    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Hero:
    def __init__(self):
        self.x = 0
        self.y = 0

    def render(self, screen):
        image = load_image('creature.png')
        screen.blit(image, (self.x, self.y))


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Task')
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    running = True
    screen.fill((255, 255, 255))
    hero = Hero()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if hero.y - 10 >= 0:
                        hero.y -= 10
                if event.key == pygame.K_DOWN:
                    if hero.y + 10 <= 300:
                        hero.y += 10
                if event.key == pygame.K_RIGHT:
                    if hero.x + 10 <= 300:
                        hero.x += 10
                if event.key == pygame.K_LEFT:
                    if hero.x - 10 >= 0:
                        hero.x -= 10
        screen.fill((255, 255, 255))
        hero.render(screen)
        pygame.display.flip()
    pygame.quit()
