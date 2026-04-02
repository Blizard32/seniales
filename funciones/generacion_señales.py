import numpy as np

# --------------- Generar una libreria con esta funcion ------------------
def crear_cajon(t, t0, ancho, amplitud=1.0):
    """Crea una señal rectangular (cajón) continua discretizada."""
    return np.where((t >= t0) & (t <= t0 + ancho), amplitud, 0.0)
# ------------------------------------------------------------------------


# ------------------------------------------------------------------------
# ----------------- Cambiar dominio temporal de una señial ---------------
# ------------------------------------------------------------------------

# --------------- Calcular la nueva dimensión temporal -------------------
def new_time_dim(t, signal, escala = 1):
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
    t_conv = np.linspace(t[0]*(N), t[-1]*(N), len(signal))
    return t_conv
# ----------------------------------------------------------------------
