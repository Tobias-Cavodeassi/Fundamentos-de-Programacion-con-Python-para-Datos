# MENÚ Y MANEJO DE INPUT

# --- Muestra las opciones y retorna la opción elegida (int) o None si fue inválida ---
def mostrar_menu():
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")

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