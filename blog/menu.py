# MENÚ Y MANEJO DE INPUT

from blog.datos import estados_post


# --- Muestra las opciones y retorna la opción elegida (int) o None si fue inválida ---
def mostrar_menu():
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Crear nuevo post")
    print("5. Validar posts")
    print("6. Guardar posts en JSON")
    print("7. Salir")

    # try-except: evita que el programa se cierre si el usuario escribe texto
    try:
        opcion = int(input("Elegí una opción: "))
        return opcion
    except ValueError:
        print("Opción inválida, ingresá un número.")
        return None


# --- Pide un texto al usuario y lo retorna sin espacios al inicio ni al final ---
def pedir_texto(mensaje):
    return input(mensaje).strip()


# --- Pide los datos de un post nuevo. Retorna un diccionario o None si hay campos vacíos/inválidos ---
def pedir_datos_post():
    print("\n--- CREAR NUEVO POST ---")
    titulo = pedir_texto("Título: ")
    contenido = pedir_texto("Contenido: ")
    tags_texto = pedir_texto("Tags (separados por coma): ")
    estado = pedir_texto(f"Estado ({', '.join(estados_post)}): ").lower()

    # Los campos no pueden quedar vacíos
    if titulo == "" or contenido == "":
        print("Error: el título y el contenido no pueden estar vacíos. No se creó el post.")
        return None

    # Se convierte el texto de tags en una lista, descartando elementos vacíos
    tags = [t.strip() for t in tags_texto.split(",") if t.strip() != ""]
    if not tags:
        print("Error: tenés que ingresar al menos un tag. No se creó el post.")
        return None

    # El estado debe ser uno de los permitidos
    if estado not in estados_post:
        print(f"Error: el estado debe ser uno de {estados_post}. No se creó el post.")
        return None

    return {"titulo": titulo, "contenido": contenido, "tags": tags, "estado": estado}