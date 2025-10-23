import otel_setup  # activa OpenTelemetry
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import clientes
from otel_setup import instrument_app


app = FastAPI(
    title="API Clientes",
    description="API para manejo de clientes",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(clientes.router)

# Instrumenta del FastAPI
instrument_app(app)

if __name__ == "__main__":
 uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)