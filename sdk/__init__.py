from bottle import Bottle, response, request
from betterproto import Message
from pb import Gateserver, DispatchRegionData, RegionEntry
from base64 import b64encode as enc

RISKY_API_CHECK_RSP = r'{"data": {},"message": "OK","retcode": 0}'
MDK_SHIELD_LOGIN_RSP = r'{"data": {"account": {"area_code": "**","email": "x","country": "ID","is_email_verify": "1","token": "x","uid": "1"},"device_grant_required": false,"reactivate_required": false,"realperson_required": false,"safe_mobile_required": false},"message": "OK","retcode": 0}'
GRANTER_LOGIN_V2_RSP = r'{"data": {"account_type": 1,"combo_id": "1","combo_token": "x","data": "{\"guest\":false}","heartbeat": false,"open_id": "1"},"message": "OK","retcode": 0}'

server = Bottle()

@server.route('/query_dispatch', method = 'GET')
def on_query_dispatch():
    region_entry = RegionEntry(
        name = "x",
        title = "x",
        env_type = "2",
        dispatch_url = "http://127.0.0.1:21000/query_gateway",
    )

    rsp = DispatchRegionData(
        retcode = 0,
        region_list = [
            region_entry
        ],
    )

    vec = rsp.SerializeToString()
    str = enc(vec)
    return str

@server.route('/query_gateway', method = 'GET')
def on_query_gateway():
    rsp = Gateserver(
        ip = "127.0.0.1",
        port = 23301,
        use_tcp = True,
        unk1 = True,
        unk2 = True,
        unk3 = True,
        unk4 = True,
        unk5 = True,
        unk6 = True,
        unk7 = True,
    )

    vec = rsp.SerializeToString()
    str = enc(vec)
    return str

@server.route('/account/risky/api/check', method = 'POST')
def on_risky_api_check():
    return RISKY_API_CHECK_RSP

@server.route('/hkrpg_global/mdk/shield/api/login', method = 'POST')
def on_mdk_shield_login():
    return MDK_SHIELD_LOGIN_RSP

@server.route('/hkrpg_global/mdk/shield/api/verify', method = 'POST')
def on_mdk_shield_verify():
    return MDK_SHIELD_LOGIN_RSP

@server.route('/hkrpg_global/combo/granter/login/v2/login', method = 'POST')
def on_risky_api_check():
    return GRANTER_LOGIN_V2_RSP

# Start sdkserver
server.run(
    host = '127.0.0.1',
    port = 21000,
)