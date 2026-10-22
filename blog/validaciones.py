# VALIDACIONES DEL SISTEMA DE BLOG

# Se importa la tupla de estados válidos desde el módulo de datos
from blog.datos import estados_post

# Claves que todo post debe tener obligatoriamente
CLAVES_OBLIGATORIAS = ("id", "titulo", "contenido", "autor", "tags", "estado")


# --- Revisa que un post cumpla las reglas. Retorna una tupla (True/False, mensaje) ---
def validar_post(post):
    # El post debe ser un diccionario
    if not isinstance(post, dict):
        return False, "el post no es un diccionario"

    # Deben existir todas las claves obligatorias
    for clave in CLAVES_OBLIGATORIAS:
        if clave not in post:
            return False, f'falta la clave "{clave}"'

    # El título no puede estar vacío (ni ser solo espacios)
    if not isinstance(post["titulo"], str) or post["titulo"].strip() == "":
        return False, 'el "titulo" está vacío o no es texto'

    # El contenido no puede estar vacío (ni ser solo espacios)
    if not isinstance(post["contenido"], str) or post["contenido"].strip() == "":
        return False, 'el "contenido" está vacío o no es texto'

    # El autor debe ser un diccionario con la clave "nombre"
    if not isinstance(post["autor"], dict):
        return False, 'el "autor" no es un diccionario'
    if "nombre" not in post["autor"]:
        return False, 'el autor no tiene la clave "nombre"'

    # Los tags deben ser una lista
    if not isinstance(post["tags"], list):
        return False, 'los "tags" no son una lista'

    # El estado debe ser uno de los definidos en estados_post
    if post["estado"] not in estados_post:
        return False, f'el "estado" no es válido (debe ser uno de {estados_post})'

    return True, "válido"


# --- Opción 4: recorre todos los posts y muestra cuáles son válidos y cuáles no ---
def validar_todos(lista):
    print("\nResultado de la validación:")
    # enumerate numera los posts empezando en 1
    for numero, post in enumerate(lista, start=1):
        es_valido, mensaje = validar_post(post)
        if es_valido:
            print(f"Post {numero}: válido")
        else:
            print(f"Post {numero}: error - {mensaje}")