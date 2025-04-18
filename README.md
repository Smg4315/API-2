# API de Generación y Evaluación de Cadenas

Este proyecto es una API web desarrollada con **Python y Flask**, que permite generar cadenas, evaluarlas con un autómata de pila y generar sus árboles de configuración. Está pensada para propósitos educativos o experimentales en el procesamiento de lenguajes formales.

---

## Contenido

- [Características](#caracteristicas)
- [Requisitos](#requisitos)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Instalación](#instalacion)
- [Uso](#uso)
- [Explicación del funcionamiento](#explicacion-del-funcionamiento)
- [Ejemplo de flujo](#ejemplo-de-flujo)

---

## Características

- Interfaz gráfica web sencilla para ingresar el número de cadenas.
- Ejecuta 3 algoritmos secuenciales:
  1. **Generador de cadenas**
  2. **Evaluador de cadenas con autómata**
  3. **Generador de árboles de configuración**
- Muestra resultados directamente en la web:
  - Cadenas generadas
  - Cadenas aceptadas
  - Árboles de configuración

---

## Requisitos

- Python 3.7 o superior
- Flask

Instalar Flask:
```bash
pip install flask
```

---

## Estructura del proyecto

```
API-2/
├── App.py                        # Archivo principal de la API (Flask)
├── templates/
│   └── index.html               # Interfaz web HTML
├── Algorithms/                 
│   ├── Algoritmo_1.py          # Generador de cadenas
│   ├── Algoritmo_2.py          # Evaluador con autómata
│   └── Algoritmo_3.py          # Generador de árboles de configuración
├── String.txt                  # Archivo generado con cadenas
├── AcceptedStrings.txt        # Archivo con cadenas aceptadas
├── config_trees.txt           # Archivo con árboles de configuración
```

---

## Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/Smg4315/API-2.git
```

---

## Uso

### `Primer Forma Para Usarlo`

1. Cuando hayas clonado el repositorio, entra en la carpeta del proyecto.

2. Una vez dentro de la carpeta API-2, abre la terminal de Git Bash:
```bash
Click Derecho -> Mostrar Mas Opciones -> Open Git Bash Here
```

3. Ejecuta el servidor:
```bash
python App.py
```

4. Cuando hayas ejecutado el servidor, abre tu navegador y visita:
```
http://localhost:5000
```

5. Ingresa un número (ej: 5) y haz clic en "Ejecutar".

6. El sistema ejecutará los 3 algoritmos y te mostrará:
   - Las cadenas generadas (válidas e inválidas)
   - Las cadenas aceptadas por el autómata
   - Los árboles de configuración


### `Segunda Forma de Usarlo`

1. Abre la carpeta en un editor de código o en un IDE de programación (especial para python).

2. Entra en el archivo App.py y ejecutalo.

3. Cuando hayas ejecutado el archivo, abre tu navegador y visita:
```
http://localhost:5000
```

4. Ingresa un número (ej: 5) y haz clic en "Ejecutar".

5. El sistema ejecutará los 3 algoritmos y te mostrará:
   - Las cadenas generadas (válidas e inválidas)
   - Las cadenas aceptadas por el autómata
   - Los árboles de configuración

---

## Explicación del funcionamiento

La API tiene dos rutas principales:

### `/`
- Muestra la interfaz HTML (`index.html`) que contiene el formulario para ingresar el número de cadenas.

### `/procesar` (método POST)
- Recibe un JSON con la cantidad de cadenas.
- Ejecuta en orden:
  1. `Algoritmo_1.py` para generar cadenas.
  2. `Algoritmo_2.py` para evaluarlas con el autómata.
  3. `Algoritmo_3.py` para generar los árboles de configuración.
- Lee los archivos de salida de cada uno:
  - `String.txt`
  - `AcceptedStrings.txt`
  - `config_trees.txt`
- Devuelve todo en formato JSON para que el frontend lo muestre.

---

## Ejemplo de flujo

1. Usuario ingresa: `4`
2. El sistema genera 4 cadenas válidas y 4 inválidas.
3. Evalúa cuáles acepta el autómata.
4. Muestra los resultados estructurados en la interfaz:

```
Cadenas generadas correctamente.
Cadenas generadas:
'aaaabbbb'
'abab'
...

Cadenas evaluadas correctamente.
Cadenas aceptadas:
'aaaabbbb'

Árboles de configuración generados correctamente.
...
```

---

## Licencia

Este proyecto es libre para uso educativo y demostrativo. Puedes adaptarlo a tus necesidades.

