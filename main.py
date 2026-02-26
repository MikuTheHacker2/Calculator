import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 300, 465
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Calculator")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLUE = (0, 122, 255)
RED = (255, 59, 48)

SCREEN_FONT = pygame.font.SysFont("Arial", 40)
BUTTON_FONT = pygame.font.SysFont("Arial", 25)

current_value = ""
result = ""
operation = None

class Button:
    def __init__(self, x, y, width, height, text, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.text_surf = BUTTON_FONT.render(text, True, WHITE)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def draw(self):
        pygame.draw.rect(SCREEN, self.color, self.rect, border_radius=5)
        SCREEN.blit(self.text_surf, self.text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

buttons = [
    Button(10, 100, 65, 65, "C", RED),
    Button(85, 100, 65, 65, "<-", GRAY),
    Button(160, 100, 65, 65, "%", GRAY),
    Button(235, 100, 65, 65, "/", BLUE),
    
    Button(10, 175, 65, 65, "7", BLACK),
    Button(85, 175, 65, 65, "8", BLACK),
    Button(160, 175, 65, 65, "9", BLACK),
    Button(235, 175, 65, 65, "*", BLUE),
    
    Button(10, 250, 65, 65, "4", BLACK),
    Button(85, 250, 65, 65, "5", BLACK),
    Button(160, 250, 65, 65, "6", BLACK),
    Button(235, 250, 65, 65, "-", BLUE),
    
    Button(10, 325, 65, 65, "1", BLACK),
    Button(85, 325, 65, 65, "2", BLACK),
    Button(160, 325, 65, 65, "3", BLACK),
    Button(235, 325, 65, 65, "+", BLUE),
    
    Button(10, 400, 140, 65, "0", BLACK),
    Button(160, 400, 65, 65, ".", BLACK),
    Button(235, 400, 65, 65, "=", BLUE)
]

clock = pygame.time.Clock()
while True:
    SCREEN.fill((20, 20, 20))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for button in buttons:
                if button.is_clicked(pos):
                    button_text = button.text
                    
                    if button_text == "C":
                        current_value = ""
                        result = ""
                        operation = None
                    elif button_text == "<-":
                        current_value = current_value[:-1]
                    elif button_text in "+-*/":
                        if current_value:
                            if result and operation:
                                try:
                                    result = str(eval(f"{result} {operation} {current_value}"))
                                except:
                                    result = "Error"
                            else:
                                result = current_value
                            operation = button_text
                            current_value = ""
                    elif button_text == "=":
                        if result and operation and current_value:
                            try:
                                result = str(eval(f"{result} {operation} {current_value}"))
                                current_value = ""
                                operation = None
                            except ZeroDivisionError:
                                result = "Div by 0"
                            except:
                                result = "Error"
                    elif button_text == "%":
                        if current_value:
                            try:
                                current_value = str(float(current_value) / 100)
                            except:
                                current_value = "Error"
                    else:
                        if current_value == "Error":
                            current_value = button_text
                        else:
                            current_value += button_text

    display_text = current_value if current_value else result
    if len(display_text) > 10:
        display_text = display_text[:10]
    text_surf = SCREEN_FONT.render(display_text, True, WHITE)
    text_rect = text_surf.get_rect(right=WIDTH-20, top=40)
    SCREEN.blit(text_surf, text_rect)

    for button in buttons:
        button.draw()

    pygame.display.flip()
    clock.tick(30)
