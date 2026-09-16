import asyncio
import random

temp = 20
heater = False

class Agent():
    async def run(self):
        while True:
            global heater
            if temp < 20:
                heater = True
                print(f"temp({temp}) heater is ON")
            elif temp > 20:
                heater = False
                print(f"temp({temp}) heater is OFF")
            else:
                print("Temp is perfect")
            await asyncio.sleep(1)

async def environment():
    while True:
        global temp
        if heater:
            temp += random.randint(1, 2)
            print(f"temp({temp}) has increased")
        else:
            temp -= random.randint(1, 2)
            print(f"temp({temp}) has decreased")
        await asyncio.sleep(1)

async def main():
    agent = Agent()
    await asyncio.gather(
        environment(),
        agent.run(),
    )

if __name__ == "__main__":
    asyncio.run(main())