# 📁 Organizador Automático de Archivos

## 🧠 Descripción del Proyecto

Este proyecto consiste en un **script de automatización** desarrollado en Python que organiza archivos dentro de una carpeta específica. El sistema clasifica automáticamente los archivos según su **extensión** y los distribuye en carpetas correspondientes. La ejecución se realiza en un **horario determinado**, simulando un comportamiento tipo cronjob o tarea programada.

Este trabajo fue desarrollado en el marco de un **Trabajo Práctico Colaborativo**, con fines educativos y de aplicación práctica de las librerías estándar de Python.

---

## ⚙️ Tecnologías y Librerías Utilizadas

- Python 3.x
- `os`: Para manipulación de archivos, rutas y directorios.
- `shutil`: Para mover archivos entre carpetas.
- `datetime`: Para obtener la hora actual.
- `time`: Para temporizar la ejecución periódica.

---

## 📂 Estructura de Archivos

- `main.py`: Script principal que monitorea la hora y ejecuta el organizador de archivos cuando corresponde.
- `organizador.py`: Módulo que contiene la lógica para clasificar y mover archivos según sus extensiones.

---

## 🧩 Funcionamiento

### 1. Clasificación Automática
El script reconoce y organiza los archivos en las siguientes categorías:

| Categoría   | Extensiones                                                   |
|-------------|---------------------------------------------------------------|
| Excel       | `.xls`, `.xlsx`                                               |
| Word        | `.doc`, `.docx`                                               |
| PDF         | `.pdf`                                                        |
| Imágenes    | `.jpg`, `.jpeg`, `.png`, `.gif`                               |
| Videos      | `.mov`, `.avi`, `.mp4`, `.mkv`                                |
| iReport     | `.jrxml`                                                      |
| SQL         | `.sql`                                                        |
| Python      | `.py`                                                         |
| Notas       | `.txt`                                                        |
| Otros       | Archivos no contemplados en las categorías anteriores         |

### 2. Ejecución por Horario
En `main.py` se define un diccionario de horarios. Cuando el sistema detecta que la hora coincide con alguna clave, ejecuta la función `organizar_archivos()` y clasifica los archivos.

```python
acciones = {
    "19:46": lambda: organizar_archivos("D:/Descargas [D]/TP_Python/ejemplos")
}
```


# Ejecución del Proyecto

## Requisitos previos
- Tener Python instalado en el sistema
- Configurar el horario y la ruta deseada en mail.py
- Crear entorno virtual


### Entorno virtual
Ejecutar en la terminal para crear el entorno virtual:
```bash
python -m venv venv
```

Activar el entorno virtual:
- En Windows:
```bash
venv\Scripts\activate
```

- En Linux:
```bash
source venv/bin/activate
```


### Ejecución 
```bash
python main.py
```

El sistema mostrará un mensaje que el programa se encuentra en espera a la hora programada, una vez llegado a su horario limpiará la carpeta de la ruta indicada y lo distribuirá en su carpeta por extension.


# Programadores
- Aragusuku Pablo Ariel
- Justiniano Debora
- Muscio Julian
- Pastor Micaela
- Piedrabuena Giuliana
- Rizzardi Daiana