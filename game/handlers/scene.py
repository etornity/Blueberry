from pb import Cmd, Vector, SceneActorInfo, MotionInfo, SceneEntityInfo, SceneEntityGroupInfo, ScenePropInfo, SceneInfo, GetCurSceneInfoScRsp, AvatarType
from game.net.pk import send_pk
import asyncio

plane = 20313
entry = (plane * 100) + 1
floor = (plane * 1000) + 1
zero = Vector(x = 0, y = 0, z = 0)

async def on_get_cur_scene_info_cs_req(connection, request):
    rsp_cmd = 'CmdGetCurSceneInfoScRsp'
    plr_actor = SceneActorInfo(
        avatar_type = AvatarType.AVATAR_FORMAL_TYPE,
        base_avatar_id = 1222,
        uid = 1,
        map_layer = 2,
    )

    plr_coord = Vector(
        x = 40748,
        y = 192819,
        z = 439218,
    )

    plr_motion = MotionInfo(
        pos = plr_coord,
        rot = zero,
    )

    plr_info = SceneEntityInfo(
        entity_id = 0,
        group_id = 0,
        inst_id = 0,
        motion = plr_motion,
        actor = plr_actor,
    )

    entity_plr = SceneEntityGroupInfo(
        group_id = 0,
        state = 1,
        entity_list = [plr_info],
    )

    ccn_prop = ScenePropInfo(
        prop_id = 808,
        prop_state = 1,
        life_time_ms = 0,
    )

    ccn_coord = Vector(
        x = 31440,
        y = 192820,
        z = 433790,
    )

    ccn_motion = MotionInfo(
        pos = ccn_coord,
        rot = zero,
    )

    ccn_info = SceneEntityInfo(
        entity_id = 1,
        group_id = 186,
        inst_id = 300001,
        motion = ccn_motion,
        prop = ccn_prop,
    )

    entity_ccn = SceneEntityGroupInfo(
        group_id = 186,
        state = 1,
        entity_list = [ccn_info],
    )

    scene_i = SceneInfo(
        plane_id = plane,
        entry_id = entry,
        floor_id = floor,
        game_mode_type = 1,
        entity_group_list = [entity_plr, entity_ccn],
    )

    rsp = GetCurSceneInfoScRsp(
        retcode = 0,
        scene = scene_i,
    )

    await send_pk(connection.reader, connection.writer, Cmd.GET_INT[rsp_cmd], rsp)
