#!/usr/bin/env python

# WS server that sends messages at random intervals
import asyncio
import datetime
import random
import websockets
import pyfirmata

PORT = '/dev/cu.usbmodem141101'

PIN = 0  # Pin 2 is used
DEL = 2  # A 3 seconds delay

# Creates a new board
board = pyfirmata.Arduino(PORT)
it = pyfirmata.util.Iterator(board)
it.start()


async def time(websocket, path):
    while True:
        board.analog[PIN].enable_reporting()
        light = board.analog[PIN].read()
        await websocket.send(str(light))
        await asyncio.sleep(random.random() * 3)

start_server = websockets.serve(time, '127.0.0.1', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
