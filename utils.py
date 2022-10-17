#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 13:03:35 2022

@author: jjimenez
"""

import io
import base64
from turtle import color

import matplotlib
matplotlib.use('Agg')   # Para multi-thread, non-interactive backend (avoid run in main loop)
import matplotlib.pyplot as plt
# Para convertir matplotlib a imagen y luego a datos binarios
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.image as mpimg


def graficar(x, y,title,labelx):
    ''' 
        Crear el grafico que se desea mostrar en HTML
    '''
    
    fig, ax = plt.subplots(figsize=(15, 6))

    ax.barh(x, y, color="tab:blue")
    ax.set_title('Top {goal}'.format(goal=title))
    ax.set_xlabel('Number of {goals}'.format(goals=labelx))


    # Convertir ese grafico en una imagen para enviar por HTTP
    # y mostrar en el HTML
    image_html = io.BytesIO()
    FigureCanvas(fig).print_png(image_html)
    plt.close(fig)  # Cerramos la imagen para que no consuma memoria del sistema
    return image_html