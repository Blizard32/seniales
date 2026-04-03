import random
import matplotlib.pyplot as plt
from signals import new_time_dim


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

    for i in range(N):
        dim_t = new_time_dim(t, seniales[i])
        if random_colors:
            axs[i].plot(dim_t, seniales[i], color=colors[random.randint(0, len(colors)-1)])
        else:
            axs[i].plot(dim_t, seniales[i], color=colors[i % len(colors)])
        axs[i].set_title(nombres[i])
        axs[i].grid()


    plt.tight_layout()
    plt.show()
