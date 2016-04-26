import pygame

class Game(object):
    def main(self, screen):
        bg = pygame.image.load('data/bg.png')
        select = pygame.image.load('data/select.png')
        wood = pygame.image.load('data/wood.png')
        select_x = 320
        select_y = 240
        clock = pygame.time.Clock()
        change=select


        while 1:
            clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return

                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    select_x = select_x + 5
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    select_x = select_x - 5
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    select_y = select_y - 5
                if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    select_y = select_y + 5
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    change=wood

            screen.fill((200, 200, 200))
            screen.blit(bg, (0, 0))
            screen.blit(change, (select_x, select_y))
            pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1366, 768))
    Game().main(screen)
