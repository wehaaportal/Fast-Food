#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fast_food.core.palettes import DarkFusionPalette, LightFusionPalette

class Design:
    def __init__(self, app):
        self.app = app

    def set_font_size(self, fontname=None,  fontsize=None):
        '''
            fontsize (int): Tamaño de la fuente.
            fontname (str): Nombre de la fuente.
        '''
        font = self.app.font()
        if fontname:
            font.setFamily(fontname)
        if fontsize:
            font.setPointSize(int(fontsize))

    def set_theme(self, theme='light'):
        '''theme (str): El tema deseado ('dark' o 'light'). ''' 
        palette = DarkFusionPalette() if theme == 'dark' else LightFusionPalette()
        self.app.setPalette(palette)

    def set_style(self, style='Fusion'):
        ''' style (str): El estilo de diseño a aplicar ('Windows', 'Fusion', 'WindowsVista'). '''
        self.app.setStyle(style)