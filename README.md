# Analisis y Procesamiento de Señales
Este es un repositorio que tiene las características para generar una librería en tu computadora, esta librería va a estar destinada a generacion de señales (cajon, triángulo, etc) y graficación de las mismas.

## Objetivo
El objetivo es que estudiantes puedan utilizar con más facilidad las funciones para generar señales y con una explicación detallada de las acciones realizadas en cada función de la librería. 
La librería es modificable, lo que quiere decir que va a ir creciendo con nuevas funciones si es que estas se encuentran útiles para facilitar la programación de análisis de señales.

## Estructura del proyecto
El directorio contiene un proyecto de desarrollo de software en Python destinado al **análisis y procesamiento de señales**. El objetivo principal es:

> **Crear una biblioteca modular y escalable para generar señales estándar (rectangular, triangular, etc.) y realizar operaciones matemáticas como correlación, convolución y análisis en dominio temporal.**

### Componentes clave:
1. **`seniales/`** (carpeta principal):
   - **`signals.py`**: Funciones para generar señales (rectangular, triangular).
   - **`operaciones.py`**: Implementación de operaciones como correlación, convolución y generación de tiempos discretos/continuos.
   - **`funciones.py`**: Herramientas para graficar señales con personalización de colores y ventanas.
   - **`__init__.py`**: Inicialización del paquete para su uso como librería.

2. **`setup.py`**: Configuración para empaquetar y distribuir la librería como un paquete Python.

3. **`build/` y `dist/`**: Artefactos de construcción (wheel y tar.gz) para la distribución del proyecto.

## Tests implementados
- **`test_signals.py`**: Verifica que las funciones de generación de señales (cajon, triangulo) funcionen correctamente.
- **`test_operations.py`**: Verifica que las operaciones matemáticas (correlación, convolución) funcionen correctamente.
- **`test_plotting.py`**: Verifica que la función de graficación no lance errores.
- **`RunTests.py`**: Script para ejecutar todos los tests de forma centralizada.

## Mejoras sugeridas
- Añadir documentación detallada para cada función.
- Expandir el soporte para más tipos de señales (seno, exponenciales, etc.).
- Mejorar la interactividad de las gráficas (animaciones, exportación a archivos).

¿Desea modificar el README.md para actualizar la descripción del proyecto o mejorar la documentación?
