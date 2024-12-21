

import pygame



class NPC:

    def __init__(self, npc_image, pos_x, pos_y):
        self.npc_image = npc_image
        self.npc_rect = npc_image.get_rect()
        self.ubicacion = self.npc_rect.topleft = (pos_x, pos_y)


