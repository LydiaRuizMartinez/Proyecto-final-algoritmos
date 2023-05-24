import pygame
from quicksort import quickSort
from ListaDoble import ListaDoble

class SearchButton:
    def __init__(self, x, y, width, height, font = None):
        self.rect = pygame.Rect(x ,y, width, height)

        self.font = font if font else pygame.font.Font(None, 28)
        self.colors = {
        'BLACK' : (0, 0, 0),
        'WHITE' : (255, 255, 255),
        'GRAY' : (200, 200, 200),
        'LIGHT_GRAY' : (220, 220, 220)
        }
        self.color_to_draw = "GRAY"

    def draw(self, screen):
        # Draw the main dropdown button
        pygame.draw.rect(screen, self.colors[self.color_to_draw], self.rect)
        pygame.draw.rect(screen, self.colors["BLACK"], self.rect, 2)

        
        text = self.font.render("Buscar", True, self.colors["BLACK"])
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def _check_filtros(self, filtros_array):
        N = len(filtros_array)
        i = 0
        while i < N - 1: # El último elemento es optativo
            if filtros_array[i] == None:
                return False
            i += 1
        return True


    def handle_event(self, event, arbol, filtros_array, mensaje_error) -> ListaDoble:
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.color_to_draw = "LIGHT_GRAY"
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self._check_filtros(filtros_array):
                    vuelos, msg_error = arbol.buscar(filtros_array)
                    quickSort(vuelos)
                    mensaje_error.set_msg(msg_error)
                    if not vuelos:
                        return None
                    lista = ListaDoble()
                    for vuelo in vuelos:
                        lista.insertar_vuelo(vuelo)
                    return lista
                else:
                    mensaje_error.set_msg("Debe rellenar todos los campos obligatorios")
                    return None
        else:
            self.color_to_draw = "GRAY"

        return None
        