import asyncio
import netdev

async def task(param):
    async with netdev.create(**param) as ios:
        # Testing sending simple command
        out = await ios.send_command("show ip int br")
        print(out)


async def run():
    dev1 = { 'username' : 'admin',
             'password' : 'admin',
             'device_type': 'cisco_ios',
             'host': '192.168.100.201',
             'secret':'123',
    }
    dev2 = { 'username' : 'admin',
             'password' : 'admin',
             'device_type': 'cisco_ios',
             'host': '192.168.100.202',
             'secret':'123',
    }
    devices = [dev1, dev2]
    tasks = [task(dev) for dev in devices]
    await asyncio.wait(tasks)


loop = asyncio.get_event_loop()
loop.run_until_complete(run())