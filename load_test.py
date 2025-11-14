import asyncio
import httpx
import random
import time

API_URL = "http://127.0.0.1:8002"  # cambia si tu servidor está en otro host o puerto

# Datos base para clientes
CARD_TYPES = ["classic", "gold", "platinum", "black", "white"]
COUNTRIES = ["usa", "colombia", "mexico", "chile"]

async def create_client(client_id: int):
    data = {
        "name": f"Cliente {client_id}",
        "cardType": random.choice(CARD_TYPES),
        "monthlyIncome": random.randint(100, 3000),
        "viseClub": random.choice([True, False]),
        "country": random.choice(COUNTRIES)
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{API_URL}/client", json=data)
        return response.status_code

async def make_purchase(client_id: int):
    data = {
        "clientId": client_id,
        "amount": random.randint(50, 500),
        "currency": "USD",
        "purchaseDate": "2025-10-23",
        "purchaseCountry": random.choice(COUNTRIES)
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{API_URL}/purchase", json=data)
        return response.status_code

async def run_load_test(num_clients: int = 50, num_purchases: int = 100):
    start = time.time()

    print(f"\n🚀 Creando {num_clients} clientes...")
    tasks = [create_client(i) for i in range(1, num_clients + 1)]
    client_results = await asyncio.gather(*tasks)

    print(f"✅ Clientes creados: {client_results.count(200)}/{len(client_results)}")

    print(f"\n🛒 Ejecutando {num_purchases} compras...")
    purchase_tasks = [make_purchase(random.randint(1, num_clients)) for _ in range(num_purchases)]
    purchase_results = await asyncio.gather(*purchase_tasks)

    print(f"✅ Compras exitosas: {purchase_results.count(200)}/{len(purchase_results)}")

    end = time.time()
    print(f"\n⏱️ Tiempo total: {end - start:.2f} segundos")
    print("🏁 Prueba de carga finalizada.\n")

if __name__ == "__main__":
    asyncio.run(run_load_test(num_clients=50, num_purchases=200))
