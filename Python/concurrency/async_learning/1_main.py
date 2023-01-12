import asyncio


async def sleep():
    print("Before sleep")
    await asyncio.sleep(5)
    print("After sleep")
    

async def print():
    print("Hello")
    

# This is the event loop
async def main():
    await sleep()
    await print()
    

if __name__ == "__main__":
    # invoke event loop
    asyncio.run(main())