import struct
import asyncio
from pb import Cmd
from typing import Dict, Literal

def dec_pk(buf: bytearray) -> Dict[str, int]:
    assert struct.unpack('>I', buf[0:4])[0] == 0x9D74C714
    assert struct.unpack('>I', buf[-4:])[0] == 0xD7A152C8

    cmd_int = struct.unpack('>H', buf[4:6])[0]
    head_len = struct.unpack('>H', buf[6:8])[0]
    body_len = struct.unpack('>I', buf[8:12])[0]

    body = buf[12 + head_len: 12 + head_len + body_len]

    return {'body': body, 'cmdInt': cmd_int}

def enc_pk(cmd_id: int, data: bytearray) -> bytearray:
    buffer_length = 12 + len(data) + 4
    buffer = bytearray(buffer_length)

    struct.pack_into('>I', buffer, 0, 0x9D74C714)
    struct.pack_into('>H', buffer, 4, cmd_id)
    struct.pack_into('>H', buffer, 6, 0)
    struct.pack_into('>I', buffer, 8, len(data))

    buffer[12:12 + len(data)] = data

    struct.pack_into('>I', buffer, 12 + len(data), 0xD7A152C8)

    return buffer

async def send_pk(reader, writer, cmd_id: int, data):
    name = Cmd.GET_STR[cmd_id]
    print(f"[SEND] {name}\n")

    if data != bytearray():
        encoded = data.SerializeToString()
    else:
        encoded = data

    buffer = enc_pk(cmd_id, encoded)

    writer.write(buffer)
    await writer.drain()
