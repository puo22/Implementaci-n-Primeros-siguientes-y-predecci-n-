
# Implementación de FIRST, FOLLOW, PRED

Herramienta modular en Python para analizar gramáticas libres de contexto y calcular los conjuntos **FIRST**, **FOLLOW** y **PRED**.

---

## Características

- Carga de gramáticas** desde archivos `.txt`
- Cálculo de conjuntos FIRST** para todos los no terminales
- Cálculo de conjuntos FOLLOW** para todos los no terminales
- Cálculo de conjuntos PRED** para cada producción
---

## Requisitos

- Python **3.6** o superior
- No requiere librerías externas (solo la librería estándar)

---

## 📁 Estructura del proyecto

```

gramaticas-ll1/
│
├── main.py           # Punto de entrada del programa
├── utils.py          # Funciones para cargar gramáticas
├── primeros.py       # Cálculo de conjuntos FIRST
├── siguientes.py     # Cálculo de conjuntos FOLLOW
├── prediccion.py     # Cálculo de conjuntos PRED
└── README.md         # Este archivo

```

---

## Formato de gramáticas

Crea archivos `.txt` con tus gramáticas usando el siguiente formato:

```

S -> A B
A -> a | ε
B -> b | c

````

### Reglas
- Usa `->` para separar el no terminal de sus producciones  
- Usa `|` para separar alternativas de producción  
- Usa `ε` para representar la cadena vacía  
- Las líneas vacías y las que empiezan con `#` son ignoradas  
- Los espacios separan símbolos en una producción  

---

### Ejemplo: `ejercicio1.txt`

```txt
# Gramática de ejemplo
S -> A B | C
A -> a A | ε
B -> b | c
C -> c C | d
````

---

## Uso

### Modo interactivo

Ejecuta el programa:

```bash
python3 main.py
```

Ingresa el nombre de tu archivo:

```
Archivo: ejercicio1.txt
```

* Analiza más archivos escribiendo sus nombres
* Presiona **Ctrl+D** (Linux/Mac) o **Ctrl+Z + Enter** (Windows) para salir

---

### Ejemplo de salida

```
=== Analizando: ejercicio1.txt ===

GRAMÁTICA:
  S -> A uno B C
  S -> S dos
  A -> B C D
  A -> A tres
  A -> ε
  B -> D cuatro C tres
  B -> ε
  C -> cinco D B
  C -> ε
  D -> seis
  D -> ε

FIRST:
FIRST(A) = ['cinco', 'cuatro', 'seis', 'tres', 'ε']
FIRST(B) = ['cuatro', 'seis', 'ε']
FIRST(C) = ['cinco', 'ε']
FIRST(D) = ['seis', 'ε']
FIRST(S) = ['cinco', 'cuatro', 'seis', 'tres', 'uno']

FOLLOW:
FOLLOW(A) = ['tres', 'uno']
FOLLOW(B) = ['$', 'cinco', 'dos', 'seis', 'tres', 'uno']
FOLLOW(C) = ['$', 'dos', 'seis', 'tres', 'uno']
FOLLOW(D) = ['$', 'cuatro', 'dos', 'seis', 'tres', 'uno']
FOLLOW(S) = ['$', 'dos']

PRED:
PRED(A -> B C D) = ['cinco', 'cuatro', 'seis', 'tres', 'uno']
PRED(A -> A tres) = ['cinco', 'cuatro', 'seis', 'tres']
PRED(A -> ε) = ['tres', 'uno']
PRED(B -> D cuatro C tres) = ['cuatro', 'seis']
PRED(B -> ε) = ['$', 'cinco', 'dos', 'seis', 'tres', 'uno']
PRED(C -> cinco D B) = ['cinco']
PRED(C -> ε) = ['$', 'dos', 'seis', 'tres', 'uno']
PRED(D -> seis) = ['seis']
PRED(D -> ε) = ['$', 'cuatro', 'dos', 'seis', 'tres', 'uno']
PRED(S -> A uno B C) = ['cinco', 'cuatro', 'seis', 'tres', 'uno']
PRED(S -> S dos) = ['cinco', 'cuatro', 'seis', 'tres', 'uno']

==================================================
```

---

## Módulos

* **utils.py** → contiene `load_grammar_from_txt()` para cargar gramáticas desde archivos de texto.
* **primeros.py** → implementa `compute_first()` que calcula los conjuntos FIRST usando un algoritmo de punto fijo.
* **siguientes.py** → implementa `compute_follow()` que calcula los conjuntos FOLLOW basándose en los FIRST.
* **prediccion.py** → implementa `compute_pred()` que calcula los conjuntos de predicción para cada producción.
* **main.py** → orquesta el análisis y proporciona la interfaz de usuario.

---

## Algoritmos

* **FIRST** → calcula el conjunto de terminales que pueden aparecer al inicio de las cadenas derivadas desde un no terminal.
* **FOLLOW** → calcula el conjunto de terminales que pueden aparecer inmediatamente después de un no terminal en alguna forma sentencial.
* **PRED** → calcula el conjunto de símbolos de predicción para cada producción, usado en el análisis LL(1).

---

## 👤 Autor
- Paula Alejandra Ortiz Salon 

```
