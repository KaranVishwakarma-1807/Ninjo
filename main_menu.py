import pygame
import sys

class MainMenu:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Main Menu")

        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 48)
        self.small_font = pygame.font.Font(None, 32)

        self.options = ["Start", "Quit"]
        self.selected = 0

    def run(self):
        while True:
            self.screen.fill((20, 20, 30))

            title = self.font.render("My Game", True, (255, 255, 255))
            self.screen.blit(title, (320 - title.get_width() // 2, 120))

            for i, option in enumerate(self.options):
                color = (255, 220, 100) if i == self.selected else (200, 200, 200)

                text = self.small_font.render(option, True, color)
                x = 320 - text.get_width() // 2
                y = 220 + i * 50
                self.screen.blit(text, (x, y))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected = (self.selected - 1) % len(self.options)

                    if event.key == pygame.K_DOWN:
                        self.selected = (self.selected + 1) % len(self.options)

                    if event.key == pygame.K_RETURN:
                        if self.options[self.selected] == "Start":
                            return "start"

                        if self.options[self.selected] == "Quit":
                            pygame.quit()
                            sys.exit()

            pygame.display.update()
            self.clock.tick(60)