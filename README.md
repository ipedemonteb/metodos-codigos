<a id="metodos-numericos---codigos"></a>
# Métodos Numéricos - Códigos

Este repositorio recopila las implementaciones en Python que utilicé durante la cursada de Métodos Numéricos. Cada carpeta agrupa algoritmos vistos en clase con ejemplos simples listos para ejecutar y adaptar a nuevos ejercicios.

Las funcionalidades incluidas son las siguientes:

- <b>Raíces de ecuaciones</b>: Implementaciones de bisección, punto fijo y Newton-Raphson con registro de iteraciones y chequeos de convergencia.
- <b>Interpolación y curvas</b>: Polinomios de Lagrange y Newton junto con curvas de Bézier para aproximar datos o trayectorias.
- <b>Integración numérica</b>: Reglas de Newton-Cotes, rectángulos y Gauss-Legendre, además de cálculo de errores teóricos.
- <b>Sistemas lineales</b>: Eliminación gaussiana y descomposición LU para resolver matrices cuadradas y analizar condicionamiento.
- <b>Problemas de valor inicial</b>: Esquemas de Euler, Heun, Taylor y Runge-Kutta para integrar ecuaciones diferenciales ordinarias.
- <b>Utilidades comunes</b>: Helpers de validación para manejar intervalos, dominios y entradas inválidas de manera consistente.

<details>
  <summary>Contenidos</summary>
  <ol>
    <li><a href="#instalacion">Instalación</a></li>
    <li><a href="#organizacion-del-repositorio">Organización del Repositorio</a></li>
    <li><a href="#instrucciones">Instrucciones</a></li>
    <li><a href="#manual-de-usuario">Manual de Usuario</a></li>
    <li><a href="#autor">Autor</a></li>
  </ol>
</details>

<a id="instalacion"></a>
## Instalación

Clonar el repositorio y, de manera opcional, crear un entorno virtual para aislar dependencias (los scripts usan solo librerías de la biblioteca estándar).

- HTTPS:
  ```sh
  git clone https://github.com/ipedemonteb/metodos-codigos.git
  ```
- SSH:
  ```sh
  git clone git@github.com:ipedemonteb/metodos-codigos.git
  ```

Configurar entorno (opcional):

```sh
python3 -m venv .venv
source .venv/bin/activate        # Linux / macOS
# .venv\\Scripts\\activate     # Windows PowerShell
pip install --upgrade pip
```

> **Requisitos**: Python 3.10+ o compatible con f-strings y type hints básicos.

<p align="right">(<a href="#metodos-numericos---codigos-de-cursada">Volver</a>)</p>

<a id="organizacion-del-repositorio"></a>
## Organización del Repositorio

- `roots/`: Métodos para encontrar raíces de funciones escalares.
- `interpolation/`: Rutinas de interpolación polinomial y curvas paramétricas.
- `integration/`: Reglas de cuadratura y aproximaciones de integrales definidas.
- `linear_algebra/`: Resolución de sistemas lineales y factorizaciones.
- `ivp/`: Solvers de ecuaciones diferenciales ordinarias de primer orden.
- `utils/`: Validaciones compartidas y utilidades de soporte.
- `README.md`: Este documento.

<p align="right">(<a href="#metodos-numericos---codigos-de-cursada">Volver</a>)</p>

<a id="instrucciones"></a>
## Instrucciones

Todos los ejemplos se ejecutan desde la raíz del repositorio. Cada script define una función principal con parámetros de ejemplo que se pueden editar para adaptarse a un problema particular.

- Ejecutar un método de raíces:
  ```sh
  python roots/newton_raphson.py
  ```
- Probar un polinomio interpolante:
  ```sh
  python interpolation/lagrange.py
  ```
- Aproximar una integral definida:
  ```sh
  python integration/newton_cotes.py
  ```
- Resolver un sistema lineal vía LU:
  ```sh
  python linear_algebra/lu_decomposition.py
  ```
- Integrar una EDO de primer orden:
  ```sh
  python ivp/runge_kutta.py
  ```

<p align="right">(<a href="#metodos-numericos---codigos-de-cursada">Volver</a>)</p>

<a id="manual-de-usuario"></a>
## Manual de Usuario

### Roots (Python)

Cada archivo define una función que implementa el algoritmo numérico y un bloque `if __name__ == "__main__"` con las funciones test. Ajustar la función objetivo, su derivada (cuando aplique) y los criterios de parada para reutilizar el código en nuevos ejercicios.

### Interpolation (Python)

Los scripts generan polinomios a partir de listas de puntos. Se pueden modificar las listas `X` y `Y` o parametrizaciones para evaluar nuevas muestras; los resultados impresos muestran los coeficientes y evaluaciones relevantes.

### Integration (Python)

Incluye variantes de Newton-Cotes y Gauss-Legendre. Ajustar el intervalo `I`, la cantidad de subintervalos y la función a integrar. Existen funciones auxiliares para estimar el error teórico.

### Linear Algebra (Python)

Implementaciones de eliminación gaussiana y descomposición LU. Editar las matrices de ejemplo para resolver nuevos sistemas o inspeccionar condicionamiento.

### IVP (Python)

Contiene integradores de paso fijo para problemas de valor inicial. Modificar la derivada `f`, las condiciones iniciales y el paso `h` para replicar ejercicios de la cursada.

<p align="right">(<a href="#metodos-numericos---codigos-de-cursada">Volver</a>)</p>

<a id="autor"></a>
## Autor

Ignacio Pedemonte Berthoud (64908) - ipedemonteberthoud@itba.edu.ar

<p align="right">(<a href="#metodos-numericos---codigos-de-cursada">Volver</a>)</p>

