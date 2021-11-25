import pygame
import sys
from game.game import Game
from records.records import Records

pygame.display.set_caption("Pacman")
fps = 60


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    width, height = screen.get_size()
    font = pygame.font.SysFont('Arial', 25)

    pygame.mixer.music.load('assets/menu_sound.ogg')
    pygame.mixer.music.play(loops=True)

    start_button = pygame.Rect(600, 250, 200, 50)
    record_button = pygame.Rect(600, 325, 200, 50)
    end_button = pygame.Rect(600, 400, 200, 50)
    bg = pygame.image.load("assets/Packman_main_menu.png")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if end_button.collidepoint(mouse_pos):
                    pygame.mixer.music.stop()
                    pygame.quit()
                    sys.exit
                if start_button.collidepoint(mouse_pos):
                    pygame.mixer.music.stop()
                    GAME = Game(screen, clock)
                    GAME.run()

                if record_button.collidepoint(mouse_pos):
                    pygame.mixer.music.stop()
                    Record = Records(screen, clock)
                    Record.run()



        screen.fill((0, 0, 0))

        screen.blit(bg, (0, 0))

        pygame.draw.rect(screen, (255, 255, 255), end_button)
        pygame.draw.rect(screen, (255, 255, 255), start_button)
        pygame.draw.rect(screen, (255, 255, 255), record_button)

        screen.blit(font.render("Выйти из игры", True, (255, 0, 0)), (end_button.x, end_button.y))
        screen.blit(font.render("Начать игру", True, (255, 0, 0)), (start_button.x, start_button.y))
        screen.blit(font.render("Таблица рекордов", True, (255, 0, 0)), (record_button.x, record_button.y))

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    sys.exit


if __name__ == '__main__':
    main()
