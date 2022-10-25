DALGO TAREA 5
Integrantes del grupo:
- Luis Alejandro Rubiano Guerrero
- Sebastian Gaona Castellanos
- Isaac David Bermúdez Lara


Pre-requisitos:

- Tener instalado Python 3.10.8, se puede instalar en https://www.python.org/downloads/ 
para cualquier sistema operativo. (Puede que sirva para otras versiones de Python pero fue probado con esta)
- Verificar dependencias ejecutando los siguientes comandos en la terminal: 
    - pip3 install sys
    - pip3 install timeit
    - pip3 install math


Instrucciones de uso:

Parte 1:    
    - Tener un archivo txt con el grafo dirigido a analizar representado como una matriz de adyacencia
      en donde la entrada ij-ésima representa el costo asociado al eje (i,j).
      Este txt debe ser un archivo de texto separado por tabuladores, o en su defecto espacios.
      Un ejemplo de este archivo es el siguiente:

      0	   90	80	-1	-1
      15	0	69	48	-1
      91	-1	0	12	39
      78	-1	-1	0	36
      26	12	39	33	0

    - Mediante el uso de la terminal de comandos, dirigirse a la carpeta donde se encuentre el archivo
      parte_1.py y ejecutar el comando: python3 parte_1.py < PATH
      Donde PATH es la ruta relativa o absoluta al archivo txt con el grafo dirigido a analizar.
    - El programa mostrará en terminal el tiempo de ejecución de Dijkstra para cada vertice,
      de Bellman-Ford para cada vertice y de Floyd-Warshall para el grafo completo.
    - Adicionalmente se creará un archivo llamado "results_1.txt" en la misma carpeta donde se encuentre
      el archivo parte_1.py, en donde se mostrarán las matrices de costos mínimos para cada algoritmo.
      (Son las mismas pero se guardan una por una para mostrar que se obtienen correctamente)

Parte 2:
    - Tener un archivo txt con el grafo no-dirigido a analizar representado como una matriz de adyacencia
      simétrica en donde la entrada ij-ésima es 1 si existe un eje de i a j, y -1 si no.
      Este txt debe ser un archivo de texto separado por tabuladores, o en su defecto espacios.
      Un ejemplo de este archivo es el siguiente:

      -1	-1	-1	1	-1	-1	-1
      -1	-1	-1	-1	-1	1	-1
      -1	-1	-1	1	-1	-1	-1
       1	-1	1	-1	-1	-1	-1
      -1	-1	-1	-1	-1	-1	1
      -1	1	-1	-1	-1	-1	-1
      -1	-1	-1	-1	1	-1	-1

    - Mediante el uso de la terminal de comandos, dirigirse a la carpeta donde se encuentre el archivo
      parte_2.py y ejecutar el comando: python3 parte_2.py < PATH
      Donde PATH es la ruta relativa o absoluta al archivo txt con el grafo no-dirigido a analizar.
    - El programa mostrará en terminal el tiempo de ejecución de BFS para encontrar componentes
      conectadas. 
    - Adicionalmente se creará un archivo llamado "results_2.txt" en la misma carpeta donde se encuentre
      el archivo parte_2.py, en donde se mostrarán todas las componentes conectadas del grafo a modo de 
      conjunto de conjuntos. Para el ejemplo anterior results_2.txt sería:
      {{0, 2, 3}, {1, 5}, {4, 6}}

Parte 3:
    - Tener un archivo txt con el grafo dirigido a analizar representado como una matriz de adyacencia
      de igual forma que en la parte 1.
    - Mediante el uso de la terminal de comandos, dirigirse a la carpeta donde se encuentre el archivo
      parte_3.py y ejecutar el comando: python3 parte_3.py < PATH
      Donde PATH es la ruta relativa o absoluta al archivo txt con el grafo dirigido a analizar.
    - El programa mostrará en terminal si el grafo contiene o no ciclos.
    - Adicionalmente se mostrará en terminal el tiempo de ejecución de DFS para encontrar ciclos.
