import asyncio
import time
import websockets

async def receive_time():

    async with websockets.connect("ws://192.168.0.143:8765") as websocket:
            
            while True:
                current_time = await websocket.recv()
                print(current_time)

asyncio.get_event_loop().run_until_complete(receive_time())
