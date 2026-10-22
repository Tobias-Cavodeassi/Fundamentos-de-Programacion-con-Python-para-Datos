# Blog en consola

Sistema de blog que se usa desde la consola. Permite ver los posts, buscarlos por título, filtrarlos por tag y validar que su estructura sea correcta.

## Cómo ejecutar

Desde la carpeta `blog_consola/`, ejecutar:

```
python main.py
```

(En Windows también se puede usar `py main.py`.)

El archivo que se debe ejecutar es **`main.py`**.

## Estructura de carpetas

```
blog_consola/
│
├── main.py
├── README.md
│
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── operaciones.py
    └── validaciones.py
```

## Responsabilidad de cada módulo

- **main.py**: archivo principal. Importa las piezas del paquete `blog`, muestra el menú en bucle y llama a la función correspondiente según la opción elegida.
- **blog/__init__.py**: archivo vacío que convierte la carpeta `blog` en un paquete de Python.
- **blog/datos.py**: datos base del sistema: `perfil_autor` (diccionario), `estados_post` (tupla), `etiquetas_blog` (set) y `posts` (lista de diccionarios).
- **blog/menu.py**: muestra el menú, captura la opción del usuario (con `try-except` para evitar errores si escribe texto) y pide textos por consola.
- **blog/operaciones.py**: funciones del blog: `listar_posts`, `buscar_por_titulo` y `filtrar_por_tag`. Reciben la lista de posts por parámetro.
- **blog/validaciones.py**: reglas del sistema: `validar_post` revisa la estructura de un post y `validar_todos` informa qué posts son válidos y cuáles tienen errores.

## Opciones del menú

1. Ver todos los posts (título, autor y estado).
2. Buscar por título (total o parcial, sin distinguir mayúsculas).
3. Filtrar por tag (sin distinguir mayúsculas).
4. Validar posts.
5. Salir.