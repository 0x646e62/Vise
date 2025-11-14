import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import clientes

# --- Cargar variables de entorno desde .env ---
from dotenv import load_dotenv
load_dotenv()

# --- Configurar OpenTelemetry para Axiom ---
# Cargar variables de entorno y configurar OTLP
from axiom_setup import instrument_app
os.environ.setdefault("OTEL_SDK_DISABLED", "false")

# --- Crear la app FastAPI ---
app = FastAPI(
    title="API Clientes",
    description="API para manejo de clientes",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# --- Instrumentar con OpenTelemetry para Axiom ---
instrument_app(app)

# --- Middleware CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Routers ---
app.include_router(clientes.router)


# --- Punto de entrada ---
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
