import asyncio
from game.net.conn import *

async def listen(host: str, port: int):
    server = await asyncio.start_server(handle_client, host, port)
    addr = server.sockets[0].getsockname()
    print(f'Listening at {addr}')

    async with server:
        await server.serve_forever()

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f'Accepted connection from {addr}')
    
    connection = Connection(reader, writer)
    await connection.handle()
