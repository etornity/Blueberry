from game.net.gate import listen
import asyncio

host = '127.0.0.1'
port = 23301

asyncio.run(listen(host, port))