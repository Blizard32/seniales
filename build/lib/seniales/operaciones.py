import numpy as np


def correlacion(x_vals, y_vals, dt):
    """ Realiza la correlacion entre x e y.<p>
        Se utiliza la propiedad hayada en el punto 9.4.<p>
        Correlación usando definición: x * y(-t) """
    y_inv = y_vals[::-1]  # invertir señal
    return np.convolve(x_vals, y_inv, mode='full') * dt

