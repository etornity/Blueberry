import asyncio
from game.net.pk import *
from game.handlers.login import on_player_get_token_cs_req, on_player_login_cs_req, on_get_basic_info_cs_req
from game.handlers.avatar import on_get_avatar_data_cs_req
from game.handlers.lineup import on_get_cur_lineup_data_cs_req
from game.handlers.scene import on_get_cur_scene_info_cs_req
from game.handlers.player import on_player_heartbeat_cs_req
from game.handlers.mission import on_get_mission_status_cs_req
from pb import Cmd

HANDLERS = {
    Cmd.GET_INT['CmdPlayerGetTokenCsReq']: on_player_get_token_cs_req,
    Cmd.GET_INT['CmdPlayerLoginCsReq']: on_player_login_cs_req,
    Cmd.GET_INT['CmdGetAvatarDataCsReq']: on_get_avatar_data_cs_req,
    Cmd.GET_INT['CmdGetCurSceneInfoCsReq']: on_get_cur_scene_info_cs_req,
    Cmd.GET_INT['CmdGetCurLineupDataCsReq']: on_get_cur_lineup_data_cs_req,
    Cmd.GET_INT['CmdPlayerHeartBeatCsReq']: on_player_heartbeat_cs_req,
    Cmd.GET_INT['CmdGetMissionStatusCsReq']: on_get_mission_status_cs_req,
    Cmd.GET_INT['CmdGetBasicInfoCsReq']: on_get_basic_info_cs_req,
    
    Cmd.GET_INT['CmdGetMainMissionCustomValueCsReq']: lambda connection, _: dummy(connection, 'CmdGetMainMissionCustomValueScRsp'),
    Cmd.GET_INT['CmdGetMultiPathAvatarInfoCsReq']: lambda connection, _: dummy(connection, 'CmdGetMultiPathAvatarInfoScRsp'),
    Cmd.GET_INT['CmdGetBagCsReq']: lambda connection, _: dummy(connection, 'CmdGetBagScRsp'),
    Cmd.GET_INT['CmdSceneEntityMoveCsReq']: lambda connection, _: dummy(connection, 'CmdSceneEntityMoveScRsp'),
    Cmd.GET_INT['CmdPlayerLoginFinishCsReq']: lambda connection, _: dummy(connection, 'CmdPlayerLoginFinishScRsp'),
}

async def dummy(connection, cmd: str):
    rsp = bytearray()
    await send_pk(connection.reader, connection.writer, Cmd.GET_INT[cmd], rsp)

class Connection:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer
        self.is_active = True

    async def handle(self):
        try:
            await self.on_data()
        except Exception as e:
            print(f'Error handling connection: {e}')
        finally:
            self.is_active = False
            self.writer.close()
            await self.writer.wait_closed()
            print('Connection closed.')

    async def on_data(self):
        try:
            while self.is_active:
                data = await self.reader.read(4096)
                if not data:
                    break
                
                packet = dec_pk(data)
                cmd_id = packet['cmdInt']
                cmd_name = Cmd.GET_STR[cmd_id]
                print(f"[RECV] {cmd_name}")

                if cmd_id in HANDLERS:
                    await HANDLERS[cmd_id](self, packet['body'])
                else:
                    print(f'[SEND] Unhandled\n')
                    
        except Exception as e:
            print(f'Error handling data: {e}')
        finally:
            self.is_active = False
            self.writer.close()
            await self.writer.wait_closed()
            print('Connection closed.')