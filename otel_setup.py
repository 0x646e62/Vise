# otel_setup.py
import os
from opentelemetry import trace, metrics
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

# Opcional para logs
from opentelemetry.sdk._logs import LoggerProvider, BatchLogProcessor
from opentelemetry.exporter.otlp.proto.http.log_exporter import OTLPLogExporter

# Cargar variables
SERVICE_NAME = os.getenv("OTEL_SERVICE_NAME", "viseapi")
SERVICE_NAMESPACE = os.getenv("OTEL_SERVICE_NAMESPACE", "devops")
DEPLOY_ENV = os.getenv("OTEL_DEPLOYMENT_ENVIRONMENT", "production")

TRACES_ENDPOINT = os.getenv("OTEL_EXPORTER_OTLP_TRACES_ENDPOINT")
LOGS_ENDPOINT = os.getenv("OTEL_EXPORTER_OTLP_LOGS_ENDPOINT")
OTLP_HEADERS = {"Authorization": os.getenv("OTEL_EXPORTER_OTLP_HEADERS")}

# Recurso común
resource = Resource.create({
    "service.name": SERVICE_NAME,
    "service.namespace": SERVICE_NAMESPACE,
    "deployment.environment": DEPLOY_ENV
})

# Tracing
trace.set_tracer_provider(TracerProvider(resource=resource))
trace_exporter = OTLPSpanExporter(endpoint=TRACES_ENDPOINT, headers=OTLP_HEADERS)
trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(trace_exporter))

# Logging (opcional)
logger_provider = LoggerProvider(resource=resource)
log_exporter = OTLPLogExporter(endpoint=LOGS_ENDPOINT, headers=OTLP_HEADERS)
logger_provider.add_log_processor(BatchLogProcessor(log_exporter))

# Helper FastAPI
def instrument_app(app):
    FastAPIInstrumentor.instrument_app(app)
