import asyncio
import datetime
import websockets


async def hello_time(websocket, path):

    while True:
        
        now = datetime.datetime.utcnow().isoformat() + "Z"
        await websocket.send(str(now))
        await asyncio.sleep(1)


def main():

    start_server = websockets.serve(hello_time, 'localhost', 8765)

    websocket_loop = asyncio.get_event_loop()
    websocket_loop.run_until_complete(start_server)

    try:

        websocket_loop.run_forever()

    except KeyboardInterrupt:

        websocket_loop.close()


if __name__ == '__main__':
    
    main()

"""asyncio.get_event_loop().run_until_complete(start_server)
try:
    asyncio.get_event_loop().run_forever()

except KeyboardInterrupt:

    asyncio.get_event_loop().close()
"""