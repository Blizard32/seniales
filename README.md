# Analisis y Procesamiento de Señales
Este es un repositorio que tiene las características para generar una librería  en tu computadora, esta librería  va a estar destinada a generacion de señales (cajon, triángulo, etc) y graficación de las mísmas.

## Objetivo
El objetivo es que estudiantes puedan utilizar con más facilidad las funciones para generar señales y con una explicación detallada de las acciones realizadas en cada funcion de la librería. 
La librería es modificable, lo que quiere decir que va a ir creciendo con nuevas funciones si es que estas se encuentran útilies para facilitar la programación de analisis de señales.



---
## Cómo instalar la librería
Se utilizq el siguente comando en la terimal para instalar por primera vez la librería que encuentra en github:
```cmd
pip install git+https://github.com/Blizard32/seniales.git
```

Se instalará las dependencias **build**, luego se obtendrán los requerimientos para el **build wheel** que necesita la librería y posteriormente se instalará la metadata de la librería. Luego de eso se pueden usar, explorar y modificar las funciones dentro de la librería.
<p>

Si se modificaron las funciones (en la librería local o global), se puede reinstalar la librería con el siguiente comando:

```c
pip install --upgrade --force-reinstall git+https://github.com/Blizard32/seniales.git
```