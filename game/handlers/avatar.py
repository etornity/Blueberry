from pb import Cmd, Avatar, GetAvatarDataScRsp, GetAvatarDataCsReq
from game.net.pk import send_pk
from betterproto import Message
import asyncio

async def on_get_avatar_data_cs_req(connection, request):
    try:
        rsp_cmd = 'CmdGetAvatarDataScRsp'
        req = GetAvatarDataCsReq().parse(request)

        av = Avatar(
            base_avatar_id = 1001,
            level = 80,
            promotion = 6,
            rank = 6,
        )

        av2 = Avatar(
            base_avatar_id = 8001,
            level = 80,
            promotion = 6,
            rank = 6,
        )
        
        rsp = GetAvatarDataScRsp(
            avatar_list = [av, av2],
            is_get_all = req.is_get_all,
        )

        await send_pk(connection.reader, connection.writer, Cmd.GET_INT[rsp_cmd], rsp)
    except Exception as e:
        print(f"Error in on_get_avatar_data_cs_req: {e}")