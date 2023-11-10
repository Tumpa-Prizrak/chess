import pygame


def draw_text(
    screen: pygame.Surface,
    font: pygame.font.Font,
    coords: tuple[int, int],
    text: str,
    color: tuple[int, int, int],
    bgcolor: tuple[int, int, int] | None = None,
):
    txt = font.render(text, True, color, bgcolor)
    textRect = txt.get_rect()
    textRect.center = coords
    screen.blit(txt, textRect)
