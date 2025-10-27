from azure.monitor.opentelemetry import configure_azure_monitor
import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import clientes

# --- Configurar Azure Monitor ---
# Usa tu cadena de conexión desde Application Insights
configure_azure_monitor(connection_string=os.getenv("APPLICATIONINSIGHTS_CONNECTION_STRING"))

# --- Crear la app FastAPI ---
app = FastAPI(
    title="API Clientes",
    description="API para manejo de clientes",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

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
