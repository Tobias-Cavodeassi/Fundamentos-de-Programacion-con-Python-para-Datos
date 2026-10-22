# OPERACIONES DEL BLOG: listar, buscar y filtrar

# --- Opción 1: listar título, autor y estado de cada post ---
def listar_posts(lista):
    print("\nListado de posts:")
    if not lista:
        print("No hay posts para mostrar.")
        return
    for post in lista:
        # Se usa .get() para no fallar si falta alguna clave o el dato es incorrecto
        if not isinstance(post, dict):
            print("- (post con formato incorrecto)")
            continue
        titulo = post.get("titulo", "(sin título)")
        estado = post.get("estado", "(sin estado)")
        autor = post.get("autor")
        # Si el autor es un diccionario se lee su nombre; si no, se avisa
        if isinstance(autor, dict):
            nombre = autor.get("nombre", "(autor sin nombre)")
        else:
            nombre = "(autor desconocido)"
        print(f"- {titulo} | Autor: {nombre} | Estado: {estado}")


# --- Opción 2: buscar por título (sin distinguir mayúsculas) ---
def buscar_por_titulo(lista, termino):
    termino = termino.lower()
    encontrados = False
    for post in lista:
        if not isinstance(post, dict):
            continue  # se ignora cualquier elemento que no sea un diccionario
        titulo = str(post.get("titulo", ""))
        if termino in titulo.lower():
            print(f"- {titulo} | Estado: {post.get('estado', 'sin estado')}")
            print(f"  {post.get('contenido', '(sin contenido)')}")
            encontrados = True
    if not encontrados:
        print("No se encontraron posts con ese título.")


# --- Opción 3: filtrar por tag (sin distinguir mayúsculas) ---
def filtrar_por_tag(lista, tag):
    tag = tag.lower()
    encontrados = False
    for post in lista:
        if not isinstance(post, dict):
            continue
        tags_post = post.get("tags", [])
        if not isinstance(tags_post, list):
            continue  # si "tags" no es una lista, se ignora ese post
        for t in tags_post:
            if str(t).lower() == tag:
                print(f"- {post.get('titulo', '(sin título)')} | Tags: {', '.join(str(x) for x in tags_post)}")
                encontrados = True
                break  # evita repetir el post si el tag coincide más de una vez
    if not encontrados:
        print("No hay posts con ese tag.")