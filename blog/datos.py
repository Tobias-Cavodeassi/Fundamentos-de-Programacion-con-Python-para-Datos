# DATOS BASE Y PERSISTENCIA CON JSON

import json
import os

# --- Perfil del autor (diccionario) ---
perfil_autor = {
    "nombre": "Tobías Cavodeassi",
    "bio": "Desarrollador de software con experiencia en Python y Django.",
    "especialidad": "Desarrollo Web",
    "redes_sociales": ["https://twitter.com/tobiascavodeassi", "https://www.linkedin.com/in/tobiascavodeassi/"]
}

# --- Estados posibles de un post (tupla: no se puede modificar) ---
estados_post = ("borrador", "publicado", "archivado")

# --- Etiquetas del blog (set: no admite elementos repetidos) ---
etiquetas_blog = {"Python", "Desarrollo Web", "Data Science", "Django", "Noticias", "Opinión"}

# --- Ruta de posts.json: siempre en la carpeta raíz del proyecto, sin importar desde dónde se ejecute ---
RUTA_POSTS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "posts.json")


# --- Carga la lista de diccionarios desde posts.json (nunca cierra el programa) ---
def cargar_posts_json(ruta=RUTA_POSTS):
    # Caso 1: el archivo no existe
    if not os.path.exists(ruta):
        print("Aviso: no se encontró posts.json. Se inicia con un blog vacío.")
        return []

    # Se lee el contenido del archivo
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
    except OSError as error:
        print(f"Error: no se pudo leer posts.json ({error}). Se inicia con un blog vacío.")
        return []

    # Caso 2: el archivo está vacío
    if contenido.strip() == "":
        print("Aviso: posts.json está vacío. Se inicia con un blog vacío.")
        return []

    # Caso 3: el contenido no es un JSON válido
    try:
        datos = json.loads(contenido)
    except json.JSONDecodeError as error:
        print(f"Error: posts.json tiene contenido inválido ({error}). Se inicia con un blog vacío.")
        return []

    # Caso 4: es un JSON válido pero no es una lista de posts
    if not isinstance(datos, list):
        print("Error: posts.json debe contener una lista de posts. Se inicia con un blog vacío.")
        return []

    return datos


# --- Guarda una lista de diccionarios en posts.json. Retorna True si se guardó, False si falló ---
def guardar_posts_json(lista_posts, ruta=RUTA_POSTS):
    # Los objetos deben convertirse a diccionarios ANTES de guardarse
    if not isinstance(lista_posts, list) or not all(isinstance(p, dict) for p in lista_posts):
        print("Error: los posts deben convertirse a diccionarios antes de guardarse en JSON.")
        return False

    try:
        # Se convierte a texto primero: si algo falla, el archivo original no se toca
        texto = json.dumps(lista_posts, ensure_ascii=False, indent=4)
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(texto)
        return True
    except (OSError, TypeError) as error:
        print(f"Error: no se pudo guardar posts.json ({error}).")
        return False