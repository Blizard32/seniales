import numpy as np


def cajon(t, t0=0.0, ancho=1.0, amplitud=1.0):
    """ Crea una señal rectangular (cajón) continua discretizada.

    Args:
        t (array): Es la dimensión temporal que se le asigna al cajon
        t0 (float, optional): Es donde está centrado (default 0)
        ancho (float, optional): Es el soporte que se le asigna al cajón (default 1)
        amplitud (float, optional): Es la altura que se le asigna al triangulo (default 1)

    Returns:
        array: Valores del cajón en base al tiempo
    """
    return np.where((t >= t0 - ancho/2) & (t <= t0 + ancho/2), amplitud, 0.0)


def triangulo(t, t0=0.0, ancho=2.0, amplitud=1.0):
    """ Crea una señal triangular continua discretizada.

    Args:
        t (array): Es la dimensión temporal que se le asigna al cajon
        t0 (float, optional): Es donde está centrado (default 0)
        ancho (float, optional): Es el soporte que se le asigna al cajón (default 2)
        amplitud (float, optional): Es la altura que se le asigna al triangulo (default 1)

    Returns:
        array: Valores del triangulo en base al tiempo
    """
    x = cajon(t, t0, ancho/2, amplitud)
    return np.convolve(x, x, 'full') * (t[1] - t[0])

