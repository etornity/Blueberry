from pb import Cmd, PlayerGetTokenScRsp, PlayerBasicInfo, PlayerLoginScRsp, GetBasicInfoScRsp
from game.net.pk import send_pk
import asyncio

async def on_player_get_token_cs_req(connection, request):
    rsp_cmd = 'CmdPlayerGetTokenScRsp'
    rsp = PlayerGetTokenScRsp(
        uid = 1,
        msg = "OK",
        retcode = 0,
    )

    await send_pk(connection.reader, connection.writer, Cmd.GET_INT[rsp_cmd], rsp)


async def on_player_login_cs_req(connection, request):
    rsp_cmd = 'CmdPlayerLoginScRsp'
    plr = PlayerBasicInfo(
        nickname = "x",
        level = 5,
        world_level = 0,
        exp = 0,
        stamina = 0,
        mcoin = 0,
        hcoin = 0,
        scoin = 0,
    )

    rsp = PlayerLoginScRsp(
        stamina = 0,
        basic_info = plr,
        retcode = 0,
    )

    await send_pk(connection.reader, connection.writer, Cmd.GET_INT[rsp_cmd], rsp)

async def on_get_basic_info_cs_req(connection, request):
    rsp_cmd = 'CmdGetBasicInfoScRsp'
    rsp = GetBasicInfoScRsp(
        retcode = 0,
        is_gender_set = True,
        gender = 1,
        week_cocoon_finished_count = 3,
    )

    await send_pk(connection.reader, connection.writer, Cmd.GET_INT[rsp_cmd], rsp)