#       Librería para el manejo de señales en Python
#       Autor: Felipe Outeiral
#       Esta librería tiene como objetivo proporcionar herramientas para la generación, manipulación y visualización de señales en Python. Incluye funciones para crear señales básicas como el cajón y el triángulo, así como operaciones fundamentales como la correlación y la convolución. Además, ofrece una función para graficar múltiples señales de manera clara y personalizada.
#       Por otro lado, se generó una función para generar una nueva dimensión temporal en base al cambio generado en una señal, lo cual es útil para graficar señales discretas con una dimensión temporal adecuada.

from .signals import cajon
from .signals import triangulo

from .operaciones import correlacion
from .operaciones import convolucion
from .operaciones import tiempo_continuo
from .operaciones import tiempo_discreto
from .operaciones import dominio_temporal

# Al graficar señales, la funcion identifica si la señal es continua o discreta y opera de manera diferente en cada caso. 
# En un futuro se planea automatizar la identificacion de cada una de las señales dentro de la tupla pasada por parametro para poder graficar cada senial en su respectiva dimensión temporal, sin necesidad de pasar una dimensión temporal base por parametro.
from .funciones import graficar_seniales