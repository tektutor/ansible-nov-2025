import asyncio

async def doTask1():
    await asyncio.sleep(1)
    for i in range(100):
        print("Inside Task 1 ...")
        await asyncio.sleep(1)
    print("Task 1 completed")

async def doTask2():
    await asyncio.sleep(2)
    for i in range(100):
        print("Inside Task 2 ...")
        await asyncio.sleep(1)
    print("Task 2 completed")

async def main():
    await asyncio.gather( doTask1(), doTask2() )

asyncio.run(main())
