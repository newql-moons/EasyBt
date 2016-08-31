from urllib import request, parse
import json

URL = 'http://api.xhub.cn' + '/api.php' + '?key={0}&page={1}&op=search_list'


def get_result(key, index=1):

    req = request.Request(URL.format(parse.quote(key, encoding='utf-8'), index))
    resp = request.urlopen(req)

    json_data = resp.read().decode(encoding='utf-8')

    data = json.loads(json_data, encoding='utf-8')

    return data
