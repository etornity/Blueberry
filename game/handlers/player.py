from pb import Cmd, PlayerHeartBeatCsReq, PlayerHeartBeatScRsp
from game.net.pk import send_pk
import asyncio
import time
from betterproto import Message

async def on_player_heartbeat_cs_req(connection, request):
    try:
        rsp_cmd = 'CmdPlayerHeartBeatScRsp'
        req = PlayerHeartBeatCsReq().parse(request)

        current_time_ms = int(time.time() * 1000)

        rsp = PlayerHeartBeatScRsp(
            retcode=0,
            client_timestamp_ms=req.client_timestamp_ms,
            server_timestamp_ms=current_time_ms
        )

        await send_pk(connection.reader, connection.writer, Cmd.GET_INT[rsp_cmd], rsp)
    except Exception as e:
        print(f"Error in on_player_heartbeat_cs_req: {e}")
