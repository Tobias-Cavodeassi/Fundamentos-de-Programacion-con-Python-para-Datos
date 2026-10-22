# DATOS BASE DEL SISTEMA DE BLOG

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

# --- Lista de posts (cada post es un diccionario) ---
posts = [
    {
        "id": 1,
        "titulo": "Primer post del blog",
        "contenido": "Este es el contenido del primer post del blog.",
        "autor": perfil_autor,
        "tags": ["Python", "Desarrollo Web"],
        "estado": "publicado",
    },
    {
        "id": 2,
        "titulo": "Segundo post del blog",
        "contenido": "Este es el contenido del segundo post del blog.",
        "autor": perfil_autor,
        "tags": ["Data Science", "Noticias"],
        "estado": "borrador",
    },
    {
        "id": 3,
        "titulo": "Tercer post del blog",
        "contenido": "",
        "autor": perfil_autor,
        "tags": ["Django", "Opinión"],
        "estado": "archivado",
    }
]