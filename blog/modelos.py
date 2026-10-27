# MODELOS: clases Autor, Post y Blog

from blog.operaciones import mostrar_posts
from blog.validaciones import validar_post, CLAVES_OBLIGATORIAS


# --- Clase Autor: representa a la persona que escribe los posts ---
class Autor:
    def __init__(self, nombre, bio="", especialidad="", redes_sociales=None):
        self.nombre = nombre
        self.bio = bio
        self.especialidad = especialidad
        self.redes_sociales = redes_sociales if redes_sociales is not None else []

    # Convierte el objeto Autor a diccionario (compatible con JSON)
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "bio": self.bio,
            "especialidad": self.especialidad,
            "redes_sociales": self.redes_sociales,
        }

    # Crea un Autor a partir de un diccionario; si está incompleto lanza ValueError
    @classmethod
    def from_dict(cls, datos):
        if not isinstance(datos, dict):
            raise ValueError('el "autor" no es un diccionario')
        if "nombre" not in datos or str(datos["nombre"]).strip() == "":
            raise ValueError('el autor no tiene la clave "nombre"')
        return cls(
            nombre=datos["nombre"],
            bio=datos.get("bio", ""),
            especialidad=datos.get("especialidad", ""),
            redes_sociales=datos.get("redes_sociales", []),
        )


# --- Clase Post: representa una publicación del blog ---
class Post:
    def __init__(self, id, titulo, contenido, autor, tags, estado):
        self.id = id
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor      # objeto Autor
        self.tags = tags        # lista de strings
        self.estado = estado

    # Convierte el Post a diccionario; el autor también se convierte a diccionario anidado
    def to_dict(self):
        autor = self.autor.to_dict() if isinstance(self.autor, Autor) else self.autor
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": autor,
            "tags": self.tags,
            "estado": self.estado,
        }

    # Crea un Post a partir de un diccionario; si está incompleto lanza ValueError
    @classmethod
    def from_dict(cls, datos):
        if not isinstance(datos, dict):
            raise ValueError("el post no es un diccionario")
        for clave in CLAVES_OBLIGATORIAS:
            if clave not in datos:
                raise ValueError(f'falta la clave "{clave}"')
        if not isinstance(datos["tags"], list):
            raise ValueError('los "tags" no son una lista')
        autor = Autor.from_dict(datos["autor"])
        return cls(datos["id"], datos["titulo"], datos["contenido"], autor, datos["tags"], datos["estado"])

    # Texto con el que se muestra el post en consola
    def __str__(self):
        nombre = getattr(self.autor, "nombre", "(autor desconocido)")
        return f"{self.titulo} | Autor: {nombre} | Estado: {self.estado} | Tags: {', '.join(str(t) for t in self.tags)}"


# --- Clase Blog: centraliza la colección de posts y la lógica principal ---
class Blog:
    def __init__(self, posts=None):
        # Atributo principal: lista de objetos Post
        self.posts = posts if posts is not None else []

    # Reconstruye un Blog a partir de una lista de diccionarios (cargados desde JSON)
    @classmethod
    def desde_diccionarios(cls, lista):
        blog = cls()
        for numero, datos in enumerate(lista, start=1):
            try:
                blog.posts.append(Post.from_dict(datos))
            except ValueError as error:
                # Un post incompleto se omite, pero el programa sigue funcionando
                print(f"Aviso: se omitió el post #{numero} del archivo ({error}).")
        return blog

    # Convierte todos los posts a una lista de diccionarios (lista para guardar en JSON)
    def a_diccionarios(self):
        return [post.to_dict() for post in self.posts]

    # Retorna todos los posts cargados
    def obtener_posts(self):
        return list(self.posts)

    # Muestra todos los posts en consola
    def listar_posts(self):
        mostrar_posts(self.posts, "No hay posts para mostrar.")

    # Retorna los posts cuyo título contiene el término (sin distinguir mayúsculas)
    def buscar_por_titulo(self, termino):
        termino = termino.lower()
        encontrados = []
        for post in self.posts:
            if termino in str(post.titulo).lower():
                encontrados.append(post)
        return encontrados

    # Retorna los posts que tienen el tag indicado (sin distinguir mayúsculas)
    def filtrar_por_tag(self, tag):
        tag = tag.lower()
        encontrados = []
        for post in self.posts:
            for t in post.tags:
                if str(t).lower() == tag:
                    encontrados.append(post)
                    break  # evita repetir el post si el tag coincide más de una vez
        return encontrados

    # Calcula el próximo id disponible
    def _siguiente_id(self):
        ids = [post.id for post in self.posts if isinstance(post.id, int)]
        return max(ids, default=0) + 1

    # Crea un Post nuevo, lo valida y lo agrega al blog; si no es válido lanza ValueError
    def crear_post(self, titulo, contenido, tags, estado, autor):
        nuevo = Post(self._siguiente_id(), titulo, contenido, autor, tags, estado)
        es_valido, mensaje = validar_post(nuevo.to_dict())
        if not es_valido:
            raise ValueError(mensaje)
        self.posts.append(nuevo)
        return nuevo

    # Valida todos los posts. Retorna una lista de tuplas (numero, es_valido, mensaje)
    def validar_posts(self):
        resultados = []
        for numero, post in enumerate(self.posts, start=1):
            es_valido, mensaje = validar_post(post.to_dict())
            resultados.append((numero, es_valido, mensaje))
        return resultados