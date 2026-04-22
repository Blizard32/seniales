# Test para funciones de graficación
import numpy as np
from seniales.funciones import graficar_seniales

def test_graficar_seniales():
    """Verificar que la función graficar_sen nadie lance errores"""
    t = np.linspace(-1, 1, 100)
    signal1 = np.sin(2*np.pi*t)
    signal2 = np.cos(2*np.pi*t)
    
    # Verificar que no se lanzen errores al graficar
    try:
        graficar_seniales([signal1, signal2], t, ["Senal seno", "Senal coseno"])
    except Exception as e:
        print(f"Error inesperado: {e}")
        assert False, "Se lanzó un error inesperado al graficar señales"

if __name__ == "__main__":
    test_graficar_seniales()
    print("Tests de graficación completados correctamente")
