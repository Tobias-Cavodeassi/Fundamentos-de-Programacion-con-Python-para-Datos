# Blog en consola

Sistema de blog que se usa desde la consola. Permite ver, buscar, filtrar, crear y validar posts, y guarda la información en un archivo `posts.json` para que no se pierda al cerrar el programa.

## Cómo ejecutar

Desde la carpeta `blog_consola/` (con el entorno virtual activado):

```
python main.py
```

El archivo que se debe ejecutar es **`main.py`**.

## Estructura de carpetas

```
blog_consola/
│
├── main.py
├── README.md
├── posts.json
│
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── modelos.py
    ├── operaciones.py
    └── validaciones.py
```

## Clases principales (`blog/modelos.py`)

- **Autor**: representa a quien escribe los posts (nombre, bio, especialidad y redes sociales). Puede convertirse a diccionario (`to_dict`) y crearse desde uno (`from_dict`).
- **Post**: representa una publicación (id, título, contenido, autor, tags y estado). El autor es un objeto `Autor`. También tiene `to_dict` y `from_dict`.
- **Blog**: centraliza la colección de posts, que se guarda como una lista de objetos `Post`. Sus métodos permiten listar, buscar por título, filtrar por tag, crear y validar posts, y convertir todos los posts a diccionarios para guardarlos.

## Módulos

- **main.py**: punto de entrada. Carga los datos, crea la instancia de `Blog`, muestra el menú y llama a los métodos según la opción elegida.
- **blog/datos.py**: datos base (`perfil_autor`, `estados_post`, `etiquetas_blog`) y funciones para cargar y guardar `posts.json`.
- **blog/menu.py**: muestra el menú y maneja todos los `input()`.
- **blog/operaciones.py**: funciones que muestran resultados en consola.
- **blog/validaciones.py**: reglas para validar la estructura de un post.

## Cómo se guarda y carga la información

- **Carga**: al iniciar, `cargar_posts_json()` lee `posts.json` y devuelve una lista de diccionarios. `Blog.desde_diccionarios()` los convierte en objetos `Post` (y `Autor`).
- **Guardado**: con la opción 6, `Blog.a_diccionarios()` convierte los objetos en diccionarios y `guardar_posts_json()` los escribe en `posts.json`. Al salir, si hay cambios sin guardar, el programa ofrece guardarlos.
- **Errores controlados**: si `posts.json` no existe, está vacío o tiene contenido inválido, el programa muestra un aviso y arranca con un blog vacío. Si un post del archivo está incompleto, se omite con un aviso.

## Menú

1. Ver todos los posts
2. Buscar por titulo
3. Filtrar por tag
4. Crear nuevo post
5. Validar posts
6. Guardar posts en JSON
7. Salir

## Qué cambió respecto al checkpoint anterior

- Los posts y el autor ahora son **objetos** (clases `Post` y `Autor`) y la colección se maneja desde la clase **`Blog`**.
- Se agregó `blog/modelos.py` con las clases.
- Los datos se **guardan y cargan desde `posts.json`** en lugar de estar escritos en el código.
- Las funciones de búsqueda y filtrado pasaron a ser métodos de `Blog`; `operaciones.py` quedó solo para mostrar resultados.
- Se agregaron las opciones **Crear nuevo post** y **Guardar posts en JSON**.
- Se agregó el manejo de errores de archivo y de datos incompletos.