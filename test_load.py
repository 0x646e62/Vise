import asyncio
import httpx
import random

URL = "http://localhost:8000/client"  # Cambia si tu API corre en otro puerto o host

# Generar datos aleatorios de clientes
def random_client():
    return {
        "name": f"Cliente-{random.randint(1, 9999)}",
        "cardType": random.choice(["Classic", "Gold", "Platinum", "Black", "White"]),
        "monthlyIncome": random.randint(100, 5000),
        "viseClub": random.choice([True, False]),
        "country": random.choice(["USA", "Colombia", "Ecuador", "Peru", "Chile"])
    }

async def send_request(client: httpx.AsyncClient, data):
    try:
        response = await client.post(URL, json=data)
        return response.status_code
    except Exception as e:
        print("❌ Error:", e)
        return None

async def main():
    async with httpx.AsyncClient(timeout=10) as client:
        tasks = []
        for _ in range(500):  # 🔥 número de peticiones
            tasks.append(send_request(client, random_client()))
        results = await asyncio.gather(*tasks)

    # Estadísticas
    total = len(results)
    success = sum(1 for r in results if r == 200)
    failed = sum(1 for r in results if r != 200)

    print(f"\n✅ Total: {total}")
    print(f"🟢 Éxitos: {success}")
    print(f"🔴 Fallos: {failed}")

if __name__ == "__main__":
    asyncio.run(main())
