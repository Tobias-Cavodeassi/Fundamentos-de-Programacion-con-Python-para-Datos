# SISTEMA DE BLOG - Archivo principal

# --- Imports desde el paquete blog ---
from blog.datos import posts
from blog.menu import mostrar_menu, pedir_texto
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_todos


# --- Coordina el flujo del programa: menú -> opción -> función correspondiente ---
def main():
    # El while True mantiene el programa activo hasta que se elija salir
    while True:
        # Se muestra el menú y se captura la opción del usuario
        opcion = mostrar_menu()

        # Opción 1: mostrar título, autor y estado de cada post
        if opcion == 1:
            listar_posts(posts)

        # Opción 2: buscar por título
        elif opcion == 2:
            termino = pedir_texto("Ingresá el título (o parte del título) a buscar: ")
            if termino == "":
                print("La búsqueda no puede estar vacía.")
            else:
                buscar_por_titulo(posts, termino)

        # Opción 3: filtrar por tag
        elif opcion == 3:
            tag = pedir_texto("Ingresá el tag por el que querés filtrar: ")
            if tag == "":
                print("El tag no puede estar vacío.")
            else:
                filtrar_por_tag(posts, tag)

        # Opción 4: validar todos los posts
        elif opcion == 4:
            validar_todos(posts)

        # Opción 5: despedida y cierre del programa
        elif opcion == 5:
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