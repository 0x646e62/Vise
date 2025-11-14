# send_events.py
from axiom_py import Client

# Si AXIOM_TOKEN está en env, Client() lo usa automáticamente.
client = Client()  

# Ingesta eventos (lista de dicts). Ajusta "mi_dataset".
client.ingest_events(
    dataset="devops",
    events=[
        {"level": "info", "msg": "Hola desde mi app", "user": "edison"},
        {"level": "error", "msg": "Algo falló", "code": 500},
    ],
)

# (Opcional) consultar datos
res = client.query(r"['devops'] | where level == 'info' | limit 20")
print(res)
