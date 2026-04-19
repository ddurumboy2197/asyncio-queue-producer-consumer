import asyncio

async def producer(queue):
    for i in range(10):
        await queue.put(i)
    print("Producer: 10 ta son qo'yildi")

async def consumer(queue):
    while True:
        try:
            son = await queue.get()
            print(f"Consumer: {son} son olindi")
            queue.task_done()
        except asyncio.CancelledError:
            break

async def main():
    queue = asyncio.Queue()

    producer_task = asyncio.create_task(producer(queue))
    consumer_task = asyncio.create_task(consumer(queue))

    await producer_task
    await consumer_task

    await queue.join()
    print("Barcha sonlar yig'ilgan")

asyncio.run(main())
```

Kodni ishga tushirganda, producer 10 ta sonni qo'yadi va keyin consumerlar ularni yig'adi. `queue.task_done()` funksiyasi bilan har bir son yig'ilganidan keyin task_done() metodi chaqiriladi, bu esa `queue.join()` funksiyasini chaqirganda, yig'ilgan sonlar soni bilan teng bo'lishiga yordam beradi.
