"""
Configuración de OpenTelemetry para Axiom
Exporta trazas, métricas y logs a Axiom usando OTLP
"""

import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()
from opentelemetry import trace, metrics
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor

# ========== VARIABLES DE CONFIGURACIÓN ==========
SERVICE_NAME = os.getenv("OTEL_SERVICE_NAME", "viseapi")
SERVICE_NAMESPACE = os.getenv("OTEL_SERVICE_NAMESPACE", "production")
DEPLOY_ENV = os.getenv("OTEL_DEPLOYMENT_ENVIRONMENT", "production")

# Axiom OTLP endpoint y token
AXIOM_DATASET = os.getenv("AXIOM_DATASET", "devops")
API_TOKEN = os.getenv("API_TOKEN", "")

# Endpoint OTLP de Axiom (formato correcto)
OTLP_ENDPOINT = "https://api.axiom.co/v1/traces"
OTLP_METRICS_ENDPOINT = "https://api.axiom.co/v1/metrics"

# Headers para Axiom (Authorization Bearer Token + Dataset)
OTLP_HEADERS = {}
if API_TOKEN:
    OTLP_HEADERS["Authorization"] = f"Bearer {API_TOKEN}"
    OTLP_HEADERS["X-Axiom-Dataset"] = AXIOM_DATASET

print(f"🔧 Configurando OpenTelemetry para Axiom...")
print(f"   Servicio: {SERVICE_NAME}")
print(f"   Endpoint: {OTLP_ENDPOINT}")
print(f"   Headers: {list(OTLP_HEADERS.keys())}")

# ========== RECURSO COMÚN ==========
resource = Resource.create({
    "service.name": SERVICE_NAME,
    "service.namespace": SERVICE_NAMESPACE,
    "deployment.environment": DEPLOY_ENV,
    "service.version": "1.0.0",
})

# ========== CONFIGURACIÓN DE TRAZAS ==========
trace_exporter = OTLPSpanExporter(
    endpoint=OTLP_ENDPOINT,
    headers=OTLP_HEADERS,
    timeout=10,
)

tracer_provider = TracerProvider(resource=resource)
tracer_provider.add_span_processor(BatchSpanProcessor(trace_exporter))
trace.set_tracer_provider(tracer_provider)

# ========== CONFIGURACIÓN DE MÉTRICAS ==========
metric_exporter = OTLPMetricExporter(
    endpoint=OTLP_METRICS_ENDPOINT,
    headers=OTLP_HEADERS,
    timeout=10,
)

metric_reader = PeriodicExportingMetricReader(metric_exporter)
meter_provider = MeterProvider(resource=resource, metric_readers=[metric_reader])
metrics.set_meter_provider(meter_provider)

# ========== INSTRUMENTACIÓN AUTOMÁTICA ==========
def instrument_app(app):
    """Instrumenta la app FastAPI y librerías HTTP"""
    print("📊 Instrumentando FastAPI...")
    FastAPIInstrumentor.instrument_app(app)
    
    # Instrumentar librerías HTTP para capturar requests salientes
    print("📊 Instrumentando HTTP clients...")
    RequestsInstrumentor().instrument()
    
    print("✅ OpenTelemetry configurado y listo para Axiom")

# ========== TRACER HELPER ==========
def get_tracer(name):
    """Obtener tracer para logs manuales"""
    return trace.get_tracer(name)
