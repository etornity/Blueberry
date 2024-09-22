from pb import Cmd, SpBarInfo, LineupAvatar, LineupInfo, GetCurLineupDataScRsp, AvatarType
from game.net.pk import send_pk
import asyncio

async def on_get_cur_lineup_data_cs_req(connection, request):
    rsp_cmd = 'CmdGetCurLineupDataScRsp'
    enr = SpBarInfo(
        cur_sp = 10000,
        max_sp = 10000,
    )

    av = LineupAvatar(
        hp = 10000,
        satiety = 0,
        id = 1001,
        avatar_type = AvatarType.AVATAR_FORMAL_TYPE,
        slot = 0,
        sp_bar = enr,
    )

    team = LineupInfo(
        name = "x",
        avatar_list = [av]
    )

    rsp = GetCurLineupDataScRsp(
        lineup = team,
        retcode = 0,
    )

    await send_pk(connection.reader, connection.writer, Cmd.GET_INT[rsp_cmd], rsp)
