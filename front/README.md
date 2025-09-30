# Frontend de Vise - Gestión de Clientes

Este es el frontend para la API de Clientes Vise, construido con **React + Vite**.

## 🚀 Características

- **React 18** con hooks modernos
- **Vite** para desarrollo rápido
- **React Hook Form** + **Zod** para validación de formularios
- **Axios** para comunicación con la API
- **React Hot Toast** para notificaciones
- **Lucide React** para iconos
- **Responsive Design** con CSS Grid y Flexbox
- **Docker** listo para producción

## 🛠️ Instalación y Desarrollo

### Prerequisitos

- Node.js 18+
- npm o yarn

### Instalación

```bash
cd front
npm install
```

### Desarrollo

```bash
npm run dev
```

El frontend estará disponible en: http://localhost:3000

### Build para producción

```bash
npm run build
```

## 🐳 Docker

### Construcción de la imagen

```bash
docker build -t vise-frontend .
```

### Ejecutar con Docker

```bash
docker run -p 3000:80 vise-frontend
```

### Docker Compose (desde la raíz del proyecto)

```bash
docker-compose up -d
```

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000

## 🎨 Funcionalidades

### Gestión de Clientes

- ✅ **Ver todos los clientes** en tarjetas responsivas
- ✅ **Crear nuevos clientes** con formulario validado
- ✅ **Editar clientes existentes**
- ✅ **Eliminar clientes** con confirmación
- ✅ **Validación en tiempo real** con mensajes de error
- ✅ **Notificaciones toast** para feedback del usuario

### Campos del Cliente

- **Nombre**: Texto requerido (2-50 caracteres)
- **País**: Texto requerido (2-50 caracteres)
- **Ingresos Mensuales**: Número positivo
- **Tipo de Tarjeta**: Select (Standard, Gold, Platinum, Black)
- **Club Vise**: Checkbox para membresía

### UI/UX

- **Diseño moderno** con gradientes y sombras
- **Responsive** para móviles y desktop
- **Iconos intuitivos** para acciones
- **Estados de carga** y manejo de errores
- **Confirmaciones** para acciones destructivas

## 🔧 Configuración

### Variables de entorno

Crea un archivo `.env` en la carpeta `front/`:

```bash
VITE_API_URL=http://localhost:8000
```

### Configuración de proxy (desarrollo)

El archivo `vite.config.js` incluye proxy para `/api` que redirige a `http://localhost:8000`

### Configuración de Nginx (producción)

El archivo `nginx.conf` incluye:

- Servir archivos estáticos
- SPA routing con fallback a index.html
- Proxy opcional para `/api`
- Headers de seguridad básicos

## 📁 Estructura del proyecto

```
front/
├── src/
│   ├── components/
│   │   ├── ClientForm.jsx     # Formulario crear/editar
│   │   └── ClientCard.jsx     # Tarjeta de cliente
│   ├── services/
│   │   └── api.js            # Cliente HTTP con axios
│   ├── App.jsx               # Componente principal
│   ├── main.jsx              # Punto de entrada
│   └── index.css             # Estilos globales
├── Dockerfile                # Imagen Docker multi-stage
├── nginx.conf               # Configuración Nginx
├── vite.config.js           # Configuración Vite
└── package.json             # Dependencias
```

## 🚀 Despliegue

### Con Docker (Recomendado)

```bash
# Desde la raíz del proyecto
docker-compose up -d

# Solo frontend
cd front
docker build -t vise-frontend .
docker run -p 3000:80 vise-frontend
```

### Build estático

```bash
npm run build
# Los archivos se generan en dist/
```

## 🔗 Integración con la API

El frontend se conecta automáticamente con la API de Vise:

- **Base URL**: Configurable via `VITE_API_URL`
- **Endpoints utilizados**:
  - `GET /clientes` - Listar clientes
  - `POST /clientes` - Crear cliente
  - `PUT /clientes/{id}` - Actualizar cliente
  - `DELETE /clientes/{id}` - Eliminar cliente

## 🎯 Próximas mejoras

- [ ] Paginación para muchos clientes
- [ ] Filtros y búsqueda
- [ ] Exportar datos (CSV, PDF)
- [ ] Dashboard con estadísticas
- [ ] Autenticación de usuarios
- [ ] Tests automatizados
- [ ] PWA (Progressive Web App)

---

**Desarrollado por:**

- Edgard Leonardo Patiño Largo
- Edison Santiago Hurtado Campos
- Daniel Felipe Arenas Quiroga
