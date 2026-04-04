import numpy as np

#-------------------------------------------------------------------------------------------
#                                       OPERACIONES
#-------------------------------------------------------------------------------------------


def correlacion(x, y, dt):
    """ Realiza la correlacion entre x e y.<p>
        Se utiliza la propiedad hayada en el punto 9.4.<p>
        Correlación usando definición: x * y(-t) """
    y_inv = y[::-1]  # invertir señal
    return np.convolve(x, y_inv, mode='full') * dt


def convolucion(x, y, dt):
    """ Realiza la convolución entre x e y.<p>
        Se utiliza la propiedad hayada en el punto 9.4.<p>
        Convolución usando definición: x * y(t) """
    return np.convolve(x, y, mode='full') * dt


def tiempo(inicio, fin, particiones = 1000):
    """ Genera un vector de tiempo con el intervalo y cantidad de particiones dadas.

    Args:
        inicio (float): Es el tiempo inicial del vector
        fin (float): Es el tiempo final del vector
        particiones (int, optional): Es la cantidad de puntos que se quieren generar. Defaults to 1000.

    Returns:
        vector: Vector de tiempo generado.
        float: El diferencial de tiempo entre cada punto del vector.
    """
    t_vector = np.linspace(inicio, fin, particiones)
    dt = t_vector[1] - t_vector[0]
    return t_vector, dt


# --------------- Calcular la nueva dimensión temporal -------------------
def dominio_temporal(t, signal, escala = 1):
    """Genera una nueva dimensión temporal en base al cambio generado en una señal.

    Args:
        t (vector): Es la dimensión temporal base
        signal (vector): Es la señal modificada a la cual se le quiere generar una nueva dimensión temporal 
        escala (int, optional): Es la escala que se le modifica a la dimensión (define el porsentaje de los limites). Si es <1 se comprime, si es >1 se estira. Defaults to 1.

    Returns:
        vector: Nueva dimensión generada. 
    """
    # Si len(señal) = len(tiempo) * N - (N-1)    -->    N = (len(señal)-1) / (len(tiempo)-1)
    N = ((len(signal)-1)/(len(t)-1)) * escala
    t_conv = tiempo(t[0] * N, t[-1] * N, int(len(signal))*N)
    return t_conv
# ----------------------------------------------------------------------