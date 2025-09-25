# API de Usuarios FastAPI

API REST para manejo de usuarios construida con FastAPI.

## 🏗️ Estructura del Proyecto

```
Vise/
├── app/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py          # Configuración de la aplicación
│   │   └── database.py        # Simulador de base de datos en memoria
│   ├── models/
│   │   ├── __init__.py
│   │   ├── common.py          # Modelos de respuesta comunes
│   │   └── usuario.py         # Modelos para usuarios
│   └── routers/
│       ├── __init__.py
│       └── usuarios.py        # CRUD de usuarios
├── main.py                    # Punto de entrada de la aplicación
├── requirements.txt           # Dependencias del proyecto
└── README.md                  # Este archivo
```

## 🚀 Instalación y Ejecución

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2. Ejecutar la aplicación

```bash
fastapi dev main.py
```

O usando uvicorn directamente:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 3. Acceder a la documentación

Una vez ejecutándose, puedes acceder a:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 📡 Endpoints Disponibles

### Endpoints de Usuarios (CRUD)

- `POST /usuarios` - Crear un nuevo usuario
- `GET /usuarios` - Listar todos los usuarios
- `GET /usuarios/{usuario_id}` - Obtener un usuario específico
- `PUT /usuarios/{usuario_id}` - Actualizar un usuario
- `DELETE /usuarios/{usuario_id}` - Eliminar un usuario

## 🧪 Ejemplos de Uso

### Crear un usuario

```bash
curl -X POST "http://localhost:8000/usuarios" \
     -H "Content-Type: application/json" \
     -d '{
       "nombre": "Juan Pérez",
       "edad": 30,
       "activo": true
     }'
```

### Obtener todos los usuarios

```bash
curl -X GET "http://localhost:8000/usuarios"
```

## 🏛️ Arquitectura

### Separación de Responsabilidades

- **`main.py`**: Configuración principal y enrutamiento
- **`app/core/`**: Configuración y lógica central
- **`app/models/`**: Modelos de datos con Pydantic
- **`app/routers/`**: Endpoints organizados por funcionalidad

### Características Implementadas

- ✅ Estructura modular y escalable
- ✅ Validación automática con Pydantic
- ✅ Documentación automática (Swagger/ReDoc)
- ✅ Manejo de errores HTTP
- ✅ CORS configurado
- ✅ Base de datos simulada en memoria
- ✅ CRUD completo para usuarios
- ✅ Código limpio sin comentarios

## 🛠️ Tecnologías Utilizadas

- **FastAPI**: Framework web moderno y rápido
- **FastAPI CLI**: Herramientas de desarrollo
- **Pydantic**: Validación de datos
- **Uvicorn**: Servidor ASGI
- **Python 3.12+**: Lenguaje de programación

## 📝 Próximas Mejoras

- [ ] Conexión a base de datos real (SQLite/PostgreSQL)
- [ ] Autenticación y autorización
- [ ] Logging estructurado
- [ ] Variables de entorno
- [ ] Dockerización

---

💡 **Tip**: Usa la documentación automática en `/docs` para probar los endpoints interactivamente.