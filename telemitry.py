# telemetry.py
import os
from azure.monitor.opentelemetry import configure_azure_monitor
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor

# Configura Azure Monitor con tu connection string
configure_azure_monitor(connection_string=os.getenv("APPLICATIONINSIGHTS_CONNECTION_STRING"))

def instrument_app(app):
    """Instrumenta la app FastAPI para enviar trazas y métricas."""
    FastAPIInstrumentor.instrument_app(app)
    RequestsInstrumentor().instrument()
