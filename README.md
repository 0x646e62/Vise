# API de Clientes FastAPI

**Autores:**
- Edgard Leonardo Patiño Largo
- Edison Santiago Hurtado Campos
- Daniel Felipe Arenas Quiroga

#### Tecnologías UtilizadasDocker

### Ejecutar con Docker

API REST para manejo de clientes construida con FastAPI.

## Estructura del Proyecto

```
Vise/
├── app/
│   ├── __init__.py## Tecnologías Utilizadas│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── database.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── common.py
│   │   └── cliente.py
│   └── routers/
│       ├── __init__.py
│       └── clientes.py
├── main.py
├── requirements.txt
└── README.md
```

## Instalación y Ejecución

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

## Endpoints Disponibles

### Endpoints de Clientes (CRUD)

- `POST /clientes` - Crear un nuevo cliente
- `GET /clientes` - Listar todos los clientes
- `GET /clientes/{cliente_id}` - Obtener un cliente específico
- `PUT /clientes/{cliente_id}` - Actualizar un cliente
- `DELETE /clientes/{cliente_id}` - Eliminar un cliente

## Ejemplos de Uso

### Crear un cliente

```bash
curl -X POST "http://localhost:8000/clientes" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "Juan Perez",
       "country": "Mexico",
       "monthlyIncome": 1200,
       "viseClub": true,
       "cardType": "Platinum"
     }'
```

### Obtener todos los clientes

```bash
curl -X GET "http://localhost:8000/clientes"
```

### Obtener un cliente específico

```bash
curl -X GET "http://localhost:8000/clientes/1"
```

### Actualizar un cliente

```bash
curl -X PUT "http://localhost:8000/clientes/1" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "Juan Perez",
       "country": "Mexico",
       "monthlyIncome": 1500,
       "viseClub": true,
       "cardType": "Platinum"
     }'
```

### Eliminar un cliente

```bash
curl -X DELETE "http://localhost:8000/clientes/1"
```

## Arquitectura

### Separación de Responsabilidades

- **`main.py`**: Configuración principal y enrutamiento
- **`app/core/`**: Configuración y lógica central
- **`app/models/`**: Modelos de datos con Pydantic
- **`app/routers/`**: Endpoints organizados por funcionalidad

### Características Implementadas

- Estructura modular y escalable
- Validación automática con Pydantic
- Documentación automática (Swagger/ReDoc)
- Manejo de errores HTTP
- CORS configurado
- Base de datos simulada en memoria
- CRUD completo para clientes
- Código limpio sin comentarios

## � Docker

### Ejecutar con Docker

#### Opción 1: Docker Compose (Recomendado)

```bash
# Desde la carpeta Vise
docker-compose up -d

# Ver logs
docker-compose logs -f

# Detener la aplicación
docker-compose down
```

#### Opción 2: Docker manual

```bash
# Desde la carpeta Vise
docker build -t clientes-api .
docker run -d -p 8000:8000 --name clientes-api-container clientes-api
```



## �🛠️ Tecnologías Utilizadas

- **FastAPI**: Framework web moderno y rápido
- **FastAPI CLI**: Herramientas de desarrollo
- **Pydantic**: Validación de datos
- **Uvicorn**: Servidor ASGI
- **Python 3.12+**: Lenguaje de programación
- **Docker**: Containerización
- **Docker Compose**: Orquestación de servicios

## Próximas Mejoras

- [x] Dockerización
- [ ] Conexión a base de datos real (SQLite/PostgreSQL)
- [ ] Autenticación y autorización
- [ ] Logging estructurado
- [ ] Variables de entorno
- [ ] Tests automatizados
- [ ] CI/CD Pipeline

---

💡 **Tip**: Usa la documentación automática en `/docs` para probar los endpoints interactivamente.