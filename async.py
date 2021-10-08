import asyncio

async def main():
    print('hello')
    # it will make it wait 10 sec
    # await text('omah lay')

    # await keyword makes it to wait for the exact 10 sec that was been set

    await asyncio.sleep(4) #it will await 4 sec before display both text func and 'money heist' at once

    # it doesn't have to wait 10 sec to display 'money heist'
    # like 'money heist' will come b4 task


    task = asyncio.create_task(text('omah lay'))

    print('money heist')

async def text(damm):
    print(damm)
    # sleeps the fucntion
    await asyncio.sleep(10)

asyncio.run(main())