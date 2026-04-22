# Test para operaciones matemáticas de señales
import numpy as np
from seniales.operaciones import correlacion, convolucion, tiempo_continuo

def test_correlacion():
    """Verificar que la correlación funcione correctamente"""
    t = tiempo_continuo(-1, 1, 100)
    x = np.sin(2*np.pi*t)
    y = np.cos(2*np.pi*t)
    result = correlacion(x, y, t[1]-t[0])
    assert np.isclose(result, 0.5), "La correlación no se comporta como esperado"

def test_convolucion():
    """Verificar que la convolución funcione correctamente"""
    t = tiempo_continuo(-1, 1, 100)
    x = np.heaviside(t, 0)
    y = np.heaviside(t, 0)
    result = convolucion(x, y, t[1]-t[0])
    assert np.allclose(result, np.zeros_like(t)), "La convolución no se comporta como esperado"

if __name__ == "__main__":
    test_correlacion()
    test_convolucion()
    print("Todos los tests pasaron correctamente")
