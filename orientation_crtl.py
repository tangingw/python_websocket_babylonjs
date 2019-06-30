import asyncio
import json
import websockets
from androidhelper import Android

droid = Android()
droid.startSensingTimed(1, 150)

async def get_oriention(websocket, path):

    while True:

        #orientation_result = droid.sensorsReadOrientation().orientation_result
        orientation_result = droid.sensorsReadOrientation().result
        orientation_json = json.dumps(
            {
                "azimuth": '%.4f' % orientation_result[0],
                "pitch": "%.4f" % orientation_result[1],
                "roll": orientation_result[2]

            }
        )

        await websocket.send(orientation_json)
        await asyncio.sleep(0.01)


def main():

    start_server = websockets.serve(get_oriention, '0.0.0.0', 8765)

    websocket_loop = asyncio.get_event_loop()
    websocket_loop.run_until_complete(start_server)

    try:

        websocket_loop.run_forever()

    except KeyboardInterrupt:

        websocket_loop.close()


if __name__ == '__main__':

    main()