
import asyncio
from datetime import datetime
from store_api.database.mongo import product_collection

products = [
    {"name": "Notebook Gamer", "description": "RTX 4060, i7", "price": 7500, "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()},
    {"name": "Smartphone", "description": "Android 13, 256GB", "price": 3200, "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()},
    {"name": "Cadeira Gamer", "description": "Ergonômica", "price": 890, "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()},
    {"name": "Monitor 4K", "description": "32 polegadas", "price": 2100, "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()},
    {"name": "PC Desktop", "description": "Ryzen 9, 32GB RAM", "price": 9600, "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()},
]

async def seed():
    await product_collection.delete_many({})
    await product_collection.insert_many(products)
    print("✅ Banco populado com dados fictícios.")

if __name__ == "__main__":
    asyncio.run(seed())
