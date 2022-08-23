from flask import Blueprint, jsonify
from func import get_info
import json

bilibili_blue = Blueprint('bilibili', __name__, url_prefix='/bilibili')


@bilibili_blue.route('/info')
def get_bilibili_info():
    url = 'https://api.bilibili.com/x/member/web/account'
    data = get_info.get_my_info(url=url)
    res = json.loads(data)['data']
    print(res)
    data_infos = {
        "mid": res.get('mid', None),
        "name": res.get('uname', None),
        'birthday': res.get('birthday', None),
        'sex': res.get('sex', None),
        'rank': res.get('rank', None)
    }
    return jsonify(data_infos)
