# ¡Juega a CONECTA 4!

CONECTA 4 es un juego de mesa de estrategia para dos jugadores. El objetivo es ser el primero en alinear tres fichas del mismo color (en nuestro caso el mismo símbolo "o" u "x") en forma horizontal, vertical o diagonal. 

## Características y reglas del juego 
- La versión original de CONECTA 4 tiene un tablero de 7 columnas y 6 filas. 

- Esta versión del juego tiene un tablero de 4x4 por lo que al conseguir tres fichas iguales y seguidas (es decir una racha o strike) ¡Ganas! 

- Si se llenan todos los espacios sin hacer una racha la partida termina en empate. 

- Ten en cuenta que el propio juego aprende de las jugadas fallidas, 
así que cada partida será más compleja que la anterior, en el caso que juegues contra la máquina. 

¿Te animas? 

## Requisitos - Detalles

**Ver / instalar requirements.txt** 

No olvides comprobar que tienes instalado pytest y marcar la carpeta "test" para hacer las comprobaciones con assert 

Pasos para activar la carpeta "test" (para macOS):  


* Abre la Paleta de Comandos: Presiona Ctrl + Shift + P (o Cmd + Shift + P en Mac).
* Configura los tests: Escribe y selecciona el comando Python: Configure Tests.
* Selecciona el framework: Elige pytest de la lista desplegable.
* Selecciona el directorio raíz: Indica la carpeta donde se encuentran tus archivos de código o de prueba (por lo general, la carpeta principal del proyecto o tests).
* Una vez finalizado, verás un icono con forma de matraz de laboratorio en la barra lateral izquierda de VS Code (el Explorador de pruebas o Test Explorer). Desde ahí podrás ver, ejecutar y depurar todas tus pruebas automáticamente.  

## Ejecutar el programa 
- Para ejecutar el programa: `python3 main.py`

## Requisitos Previos

* **Python:** Versión 3.14.7
* **Visual Studio Code** con la extensión de Python instalada.


## Instalación y Ejecución

1. Clona o descarga el repositorio en tu equipo.
2. Abre la carpeta del proyecto en Visual Studio Code.
3. Crea y activa un entorno virtual:
   ```bash
    # Para crear el entorno: 
    # En Windows: 
    python -m venv entorno

    # En MacOS: 
    python3 -m venv entorno

    # Para activar el entorno: 
    # En Windows:
    entorno\Scripts\activate

    # En macOS/Linux:
    source entorno/bin/activate
   ```
4. Instala las librerías necesarias ejecutando:
   ```bash
   # En Windows:
   pip install -r requirements.txt

   # En macOS/Linux:
   pip3 install -r requirements.txt
   ```

## Licencia

Autor = Keepcoding España S.L.U.