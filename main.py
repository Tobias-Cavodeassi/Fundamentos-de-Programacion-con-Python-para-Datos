# SISTEMA DE BLOG - Archivo principal

# --- Imports desde el paquete blog ---
from blog.datos import cargar_posts_json, guardar_posts_json, perfil_autor
from blog.menu import mostrar_menu, pedir_texto, pedir_datos_post
from blog.modelos import Autor, Blog
from blog.operaciones import mostrar_posts, mostrar_validacion


# --- Coordina el flujo del programa: carga -> menú -> opción -> método de Blog ---
def main():
    # Se cargan los datos desde posts.json y se crea la instancia de Blog
    datos_cargados = cargar_posts_json()
    blog = Blog.desde_diccionarios(datos_cargados)

    # Indica si hay cambios que todavía no se guardaron en posts.json
    cambios_sin_guardar = False

    # El while True mantiene el programa activo hasta que se elija salir
    while True:
        # Se muestra el menú y se captura la opción del usuario
        opcion = mostrar_menu()

        # Opción 1: mostrar todos los posts
        if opcion == 1:
            blog.listar_posts()

        # Opción 2: buscar por título
        elif opcion == 2:
            termino = pedir_texto("Ingresá el título (o parte del título) a buscar: ")
            if termino == "":
                print("La búsqueda no puede estar vacía.")
            else:
                mostrar_posts(blog.buscar_por_titulo(termino), "No se encontraron posts con ese título.")

        # Opción 3: filtrar por tag
        elif opcion == 3:
            tag = pedir_texto("Ingresá el tag por el que querés filtrar: ")
            if tag == "":
                print("El tag no puede estar vacío.")
            else:
                mostrar_posts(blog.filtrar_por_tag(tag), "No hay posts con ese tag.")

        # Opción 4: crear un nuevo post
        elif opcion == 4:
            datos_post = pedir_datos_post()
            if datos_post is not None:
                try:
                    autor = Autor.from_dict(perfil_autor)
                    nuevo = blog.crear_post(autor=autor, **datos_post)
                    print(f"Post creado con id {nuevo.id}. Recordá guardarlo con la opción 6.")
                    cambios_sin_guardar = True
                except ValueError as error:
                    print(f"Error: no se pudo crear el post ({error}).")

        # Opción 5: validar todos los posts
        elif opcion == 5:
            mostrar_validacion(blog.validar_posts())

        # Opción 6: guardar los posts en posts.json (primero se convierten a diccionarios)
        elif opcion == 6:
            if guardar_posts_json(blog.a_diccionarios()):
                print("Posts guardados correctamente en posts.json.")
                cambios_sin_guardar = False

        # Opción 7: despedida y cierre del programa
        elif opcion == 7:
            # Si hay cambios sin guardar, se ofrece guardarlos antes de salir
            if cambios_sin_guardar:
                respuesta = pedir_texto("Hay cambios sin guardar. ¿Querés guardarlos? (s/n): ").lower()
                if respuesta == "s":
                    if guardar_posts_json(blog.a_diccionarios()):
                        print("Posts guardados correctamente en posts.json.")
            print("Saliendo del programa. ¡Hasta pronto!")
            break

        # opcion es None cuando se ingresó texto: el error ya se mostró en mostrar_menu()
        elif opcion is None:
            continue

        # Cualquier número que no sea una opción existente
        else:
            print("Opción inválida, intenta de nuevo")


# --- Protege la ejecución: main() solo corre si se ejecuta este archivo directamente ---
if __name__ == "__main__":
    main()