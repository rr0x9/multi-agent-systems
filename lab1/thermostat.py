import asyncio
import random

temp = 20

class Agent():
    async def run(self):
        while True:
            if temp == 20:
                print("Temp is good")
            else:
                print("Temp is bad")
            await asyncio.sleep(1)

async def environment():
    while True:
        global temp
        temp = random.randrange(12, 28)
        print(temp)
        await asyncio.sleep(1)

async def main():
    agent = Agent()
    await asyncio.gather(
        environment(),
        agent.run(),
    )

if __name__ == "__main__":
    asyncio.run(main())