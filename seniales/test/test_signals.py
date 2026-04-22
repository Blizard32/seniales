# Test para funciones de generación de señales
import numpy as np
from seniales.signals import cajon, triangulo

def test_cajon():
    """Verificar que la función cajon genere una señal rectangular"""
    t = np.linspace(-1, 1, 100)
    signal = cajon(t, t0=0, ancho=1, amplitud=1)
    assert np.allclose(signal, np.zeros_like(t)), "La señal cajón no se comporta como esperado"

def test_triangulo():
    """Verificar que la función triangulo genere una señal triangular"""
    t = np.linspace(-2, 2, 100)
    signal = triangulo(t, t0=0, ancho=2, amplitud=1)
    expected = np.clip(1 - np.abs(t), 0, 1)
    assert np.allclose(signal, expected), "La señal triangular no se comporta como esperado"

if __name__ == "__main__":
    test_cajon()
    test_triangulo()
    print("Todos los tests pasaron correctamente")
