import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Ikea Labyrinth")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/FatSansRound.ttf", size)


def levels():
    while True:
        LEVELS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill((251,218,12))

        LEVELS_TEXT = get_font(55).render("This is the LEVELS screen.", True, "#0057ad")
        LEVELS_RECT = LEVELS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(LEVELS_TEXT, LEVELS_RECT)

        LEVELS_BACK = Button(image=None, pos=(640, 460), text_input="BACK", font=get_font(90), base_color="#0057ad", hover_color="white")

        LEVELS_BACK.ChangeColor(LEVELS_MOUSE_POS)
        LEVELS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVELS_BACK.CheckForInput(LEVELS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill((251,218,12))

        OPTIONS_TEXT = get_font(55).render("This is the OPTIONS screen.", True, "#0057ad")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(90), base_color="#0057ad", hover_color="white")

        OPTIONS_BACK.ChangeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.CheckForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.fill((0,87,173))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("IKEA LABYRINTH", True, "#fbda0c")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        LEVELS_BUTTON = Button(image=pygame.image.load("assets/levels_button.png"), pos=(640, 250),
                             text_input="LEVELS", font=get_font(90), base_color="#0057ad", hover_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/options_button.png"), pos=(640, 400),
                                text_input="OPTIONS", font=get_font(90), base_color="#0057ad", hover_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/quit_button.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(80), base_color="#0057ad", hover_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [LEVELS_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.ChangeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVELS_BUTTON.CheckForInput(MENU_MOUSE_POS):
                    levels()
                if OPTIONS_BUTTON.CheckForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.CheckForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()