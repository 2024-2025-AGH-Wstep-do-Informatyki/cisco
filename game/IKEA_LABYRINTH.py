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

        LEVELS_TEXT = get_font(55).render("", True, "#0057ad")
        LEVELS_RECT = LEVELS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(LEVELS_TEXT, LEVELS_RECT)

        LEVELS_BACK = Button(image=None, pos=(640, 600), text_input="BACK", font=get_font(90), base_color="#0057ad", hover_color="white")
        LEVELS_LEVELONE = Button(image=pygame.image.load("assets/levels_button.png"), pos=(640, 100), text_input="LEVEL ONE", font=get_font(90), base_color="#0057ad", hover_color="white")
        LEVELS_LEVELTWO = Button(image=pygame.image.load("assets/levels_button.png"), pos=(640, 240), text_input="LEVEL TWO", font=get_font(90), base_color="#0057ad", hover_color="white")
        LEVELS_LEVELTHREE = Button(image=pygame.image.load("assets/levels_button.png"), pos=(640, 380), text_input="LEVEL THREE", font=get_font(90), base_color="#0057ad", hover_color="white")

        for button in [LEVELS_BACK, LEVELS_LEVELONE, LEVELS_LEVELTWO, LEVELS_LEVELTHREE]:
            button.ChangeColor(LEVELS_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVELS_BACK.CheckForInput(LEVELS_MOUSE_POS):
                    main_menu()
                if LEVELS_LEVELONE.CheckForInput(LEVELS_MOUSE_POS):
                    level_one()
                if LEVELS_LEVELTWO.CheckForInput(LEVELS_MOUSE_POS):
                    level_two()
                if LEVELS_LEVELTHREE.CheckForInput(LEVELS_MOUSE_POS):
                    level_three()

        pygame.display.update()

def level_one():
    while True:
        LEVELONE_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill((251,218,12))
        LEVELONE_TEXT = get_font(55).render("This is level ONE", True, "#0057ad")
        LEVELONE_RECT = LEVELONE_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(LEVELONE_TEXT, LEVELONE_RECT)

        LEVELONE_BACK = Button(image=None, pos=(640,400), text_input="BACK", font=get_font(90),base_color="#0057ad", hover_color="white")

        LEVELONE_BACK.ChangeColor(LEVELONE_MOUSE_POS)
        LEVELONE_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVELONE_BACK.CheckForInput(LEVELONE_MOUSE_POS):
                    levels()

        pygame.display.update()

def level_two():
    while True:
        LEVELTWO_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill((251,218,12))
        LEVELTWO_TEXT = get_font(55).render("This is level TWO", True, "#0057ad")
        LEVELTWO_RECT = LEVELTWO_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(LEVELTWO_TEXT, LEVELTWO_RECT)

        LEVELTWO_BACK = Button(image=None, pos=(640,400), text_input="BACK", font=get_font(90),base_color="#0057ad", hover_color="white")

        LEVELTWO_BACK.ChangeColor(LEVELTWO_MOUSE_POS)
        LEVELTWO_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVELTWO_BACK.CheckForInput(LEVELTWO_MOUSE_POS):
                    levels()

        pygame.display.update()

def level_three():
    while True:
        LEVELTHREE_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill((251,218,12))
        LEVELTHREE_TEXT = get_font(55).render("This is level THREE", True, "#0057ad")
        LEVELTHREE_RECT = LEVELTHREE_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(LEVELTHREE_TEXT, LEVELTHREE_RECT)

        LEVELTHREE_BACK = Button(image=None, pos=(640,400), text_input="BACK", font=get_font(90),base_color="#0057ad", hover_color="white")

        LEVELTHREE_BACK.ChangeColor(LEVELTHREE_MOUSE_POS)
        LEVELTHREE_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVELTHREE_BACK.CheckForInput(LEVELTHREE_MOUSE_POS):
                    levels()

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