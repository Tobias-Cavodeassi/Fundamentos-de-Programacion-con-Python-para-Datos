# OPERACIONES DE PRESENTACIÓN: mostrar resultados en consola

# --- Muestra una lista de objetos Post (usa el método __str__ de Post) ---
def mostrar_posts(lista, mensaje_vacio="No hay posts para mostrar."):
    if not lista:
        print(mensaje_vacio)
        return
    print("\nPosts:")
    for post in lista:
        print(f"- {post}")


# --- Muestra el resultado de la validación: lista de tuplas (numero, es_valido, mensaje) ---
def mostrar_validacion(resultados):
    print("\nResultado de la validación:")
    if not resultados:
        print("No hay posts para validar.")
        return
    for numero, es_valido, mensaje in resultados:
        if es_valido:
            print(f"Post {numero}: válido")
        else:
            print(f"Post {numero}: error - {mensaje}")