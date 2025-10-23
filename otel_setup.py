# otel_setup.py
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

import os

# Cargar variables de entorno si es necesario
OTLP_ENDPOINT = os.getenv(
    "OTEL_EXPORTER_OTLP_TRACES_ENDPOINT",
    "https://otlp-gateway-prod-us-east-2.grafana.net/otlp/v1/traces"
)
OTLP_HEADERS = {
    "Authorization": os.getenv(
        "OTEL_EXPORTER_OTLP_HEADERS",
        "Basic MTQxMTE5NDpnbGNfZXlKdklqb2lNVFUyTlRZeU1TSXNJbTRpT2lKMmFYTmxMWFJ2YTJWdUlpd2lheUk2SWpZeE9FcFJNRmREV1ZNNVEyeHNOVUUwUVRjMWVUZHhVaUlzSW0waU9uc2ljaUk2SW5CeWIyUXRkWE10WldGemRDMHdJbjE5"
    )
}
SERVICE_NAME = os.getenv("OTEL_SERVICE_NAME", "viseapi")
SERVICE_NAMESPACE = os.getenv("OTEL_SERVICE_NAMESPACE", "devops")
DEPLOY_ENV = os.getenv("OTEL_DEPLOYMENT_ENVIRONMENT", "production")

# Crear recurso
resource = Resource.create(attributes={
    "service.name": SERVICE_NAME,
    "service.namespace": SERVICE_NAMESPACE,
    "deployment.environment": DEPLOY_ENV
})

# Configurar TracerProvider
trace.set_tracer_provider(TracerProvider(resource=resource))

# Configurar exporter OTLP
otlp_exporter = OTLPSpanExporter(
    endpoint=OTLP_ENDPOINT,
    headers=OTLP_HEADERS
)

# Procesador de spans
span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

# Función helper para instrumentar FastAPI
def instrument_app(app):
    FastAPIInstrumentor.instrument_app(app)
