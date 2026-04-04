import random
import matplotlib.pyplot as plt
import numpy as np
from .operaciones import dominio_temporal


def graficar_seniales(seniales, t, nombres, random_colors = True, window_lenght = 10, window_height = 2):
    """ Genera una ventana plot con las señales pasadas por parametro

    Args:
        seniales (array): Son las señales a graficar, se debe pasar una lista [s1, s2, ...] con cada señal a graficar.
        t (array): Es la dimensión temporal base, se le asigna a cada señal una nueva dimensión temporal en base a su cambio.
        nombres (array): Son los nombres de las señales a graficar, se debe pasar una lista ["n1", "n2", ...] con cada nombre.
        random_colors (bool, optional): Si es True, se asignan colores aleatorios a las señales. Defaults to True.
        window_lenght (int, optional): Es la longitud de la ventana del gráfico. Defaults to 10.
        window_height (int, optional): Es la altura de cada subplot del gráfico. Defaults to 2.
    """
    N = len(seniales)
    fig, axs = plt.subplots(N, 1, figsize=(window_lenght, window_height * N))
    colors = ["blue", "red", "green", "orange", "purple", "brown", "gray", "olive", "cyan"]

    # En un futuro hacer que si N es muy grande, se generen varias ventanas con 3 subplots cada una, para evitar que se amontonen las señales en una sola ventana.
    
    for i in range(N):
        if (t[1] - t[0] == 1):
            # Si la dimensión temporal es igual a 1, se asume que es una señal continua y se grafica con líneas.
            dim_t = np.arange(t[0], t[0] + len(seniales[i]), 1)  # Se genera una dimensión temporal en base al tamaño de la señal
            if random_colors:
                axs[i].stem(dim_t, seniales[i])
            else:
                axs[i].stem(dim_t, seniales[i])
            axs[i].set_title(nombres[i])
            axs[i].grid()
        else:
            # Si la dimensión temporal es menor a 1, se asume que es una señal discreta y se grafica con marcadores.
            dim_t = dominio_temporal(t, seniales[i])
            if random_colors:
                axs[i].plot(dim_t, seniales[i], color=colors[random.randint(0, len(colors)-1)])
            else:
                axs[i].plot(dim_t, seniales[i], color=colors[i % len(colors)])
            axs[i].set_title(nombres[i])
            axs[i].grid()

    plt.tight_layout()
    plt.show()
