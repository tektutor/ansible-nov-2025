import asyncio

async def sayHello():
    print("Hello")
    await asyncio.sleep(1)
    print("World!")

asyncio.run(sayHello())
