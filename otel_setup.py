from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter

# Define atributos del servicio
resource = Resource(attributes={
    "service.name": "api-clientes",
    "service.namespace": "my-application-group",
    "deployment.environment": "production"
})

# Configura el proveedor de trazas
trace.set_tracer_provider(TracerProvider(resource=resource))
tracer_provider = trace.get_tracer_provider()

# Exportador a consola
console_exporter = ConsoleSpanExporter()
tracer_provider.add_span_processor(SimpleSpanProcessor(console_exporter))
