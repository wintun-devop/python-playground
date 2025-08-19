import asyncio
import sys

from async_db import AsyncDatabase

# ✅ Only applies on Windows
if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

db = AsyncDatabase()

async def create():
    async with await db.connect() as conn:
        print("conn",conn)
        async with conn.cursor() as cur:
            print("cur",cur)
            query = """INSERT INTO "Product" (name, model_no, description, arrival)
                       VALUES (%s, %s, %s, %s)
                       RETURNING id, name, model_no, description, arrival"""
            record = (
                'Mikrotik L009UiGS-2HaxD-IN',
                'CRS310-8G+2S+IN',
                'amazing Marvell 98DX226S switch-chip...',
                '2012-01-05'
            )
            await cur.execute(query, record)
            result = await cur.fetchone()
            print(result)
            return result
        
async def read_one(id: str):
    async with await db.connect() as conn:
        async with conn.cursor() as cur:
            query = 'SELECT id, name, model_no, description, arrival FROM "Product" WHERE id = %s'
            await cur.execute(query, (id,))
            result = await cur.fetchone()
            print(result)
            return result
        
async def read_all():
    async with await db.connect() as conn:
        async with conn.cursor() as cur:
            query = 'SELECT id, name, model_no, description, arrival FROM "Product"'
            await cur.execute(query)
            results = await cur.fetchall()
            for row in results:
                print(row)
            return results
        
async def update(id: str, field: str, value: str):
    async with await db.connect() as conn:
        try:
            async with conn.transaction():
                async with conn.cursor() as cur:
                    query = f'UPDATE "Product" SET {field} = %s WHERE id = %s RETURNING id, name, model_no, description, arrival'
                    await cur.execute(query, (value, id))
                    result = await cur.fetchone()
                    print(result)
                    return result
        except Exception as e:
            print("❌ Update failed:", e)
            await conn.rollback()
            raise

async def delete(id: str):
    async with await db.connect() as conn:
        try:
            async with conn.transaction():
                async with conn.cursor() as cur:
                    query = 'DELETE FROM "Product" WHERE id = %s'
                    await cur.execute(query, (id,))
                    print(f"✅ Deleted product with id: {id}")
        except Exception as e:
            print("❌ Delete failed:", e)
            await conn.rollback()
            raise

        
async def create_transaction():
    async with await db.connect() as conn:
        print("conn", conn)
        try:
            async with conn.transaction():  # 🔒 Begin transaction
                async with conn.cursor() as cur:
                    print("cur", cur)
                    query = """INSERT INTO "Product" (name, model_no, description, arrival)
                               VALUES (%s, %s, %s, %s)
                               RETURNING id, name, model_no, description, arrival"""
                    record = (
                        'Mikrotik L009UiES-2HaxD-ES',
                        'CRS310-8G+ES+ES',
                        'amazing Marvell 98ES226S switch-chip...',
                        '2012-01-06'
                    )
                    await cur.execute(query, record)
                    result = await cur.fetchone()
                    print(result)
                    return result
        except Exception as e:
            print("❌ Transaction failed:", e)
            await conn.rollback()  # 🔁 Explicit rollback (optional here)
            raise


async def main():
    await delete("74733c88-3664-447b-8191-5b8699dc0817")


asyncio.run(main())