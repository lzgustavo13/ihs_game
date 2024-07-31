import pygame, sys

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.jpeg")

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def draw_text(surface, text, pos, font_size, color):
    font = get_font(font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=pos)
    surface.blit(text_surface, text_rect)
    return text_rect

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "White")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        # Draw rectangles
        P1_RECT = pygame.Rect(90, 215, 1090, 80)
        P2_RECT = pygame.Rect(335, 365, 600, 80)
        QT_RECT = pygame.Rect(485, 515, 300, 80)
        
        pygame.draw.rect(SCREEN, (0, 0, 0), P1_RECT)
        pygame.draw.rect(SCREEN, (0, 0, 0), P2_RECT)
        pygame.draw.rect(SCREEN, (0, 0, 0), QT_RECT)

        # Draw texts
        draw_text(SCREEN, "PLAY SPACE INVADERS", (640, 250), 55, "White")
        draw_text(SCREEN, "PLAY SNAKE", (640, 400), 55, "White")
        draw_text(SCREEN, "QUIT", (640, 550), 55, "White")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    print("play")
                if event.key == pygame.K_o:
                    print("options")
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
