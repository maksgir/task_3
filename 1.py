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


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Task')
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    running = True
    screen.fill((0, 0, 0))

    while running:
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                screen.fill((0, 0, 0))
                image = load_image('arrow.png')
                screen.blit(image, event.pos)
                if not pygame.mouse.get_focused():
                    screen.fill((0, 0, 0))

        pygame.display.flip()
    pygame.quit()
