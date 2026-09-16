import asyncio
import random

left = True # clean
right = False # dirty


class Agent():
    position = "left"
    async def run(self):
        global left
        global right

        while True:
            self.position = "left" if self.position == "right" else "left"

            if self.position == "left" and left is False:
                print("Hoover is hoovering left side")
                left = True
            elif self.position == "right" and right is False:
                print("Hoover is hoovering right side")
                right = True
            await asyncio.sleep(3)

async def environment():
    while True:
        global left
        global right
        if left is True:
            left = random.choice([True, False])
            print("Left location became dirty") if left is False else None

        if right is True:
            right = random.choice([True, False])
            print("Right location became dirty") if right is False else None

        await asyncio.sleep(3)

async def main():
    agent = Agent()
    await asyncio.gather(
        environment(),
        agent.run(),
    )

if __name__ == "__main__":
    asyncio.run(main())