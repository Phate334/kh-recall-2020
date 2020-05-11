import json
from datetime import datetime

import pdfplumber

out = {
    'name': '高雄市第3屆市長罷免案投開票所設置地點一覽表',
    'datetime': '1589205495',
    'header': ['投開票所編號', '投開票所名稱', '投開票所地址', '所屬村里', '所屬鄰別', '備註'],
    'data': []
}

parse_time = int(datetime.now().timestamp())

with pdfplumber.open('090511.pdf') as pdf, open('{}.json'.format(parse_time), 'w', encoding='utf-8') as f:
    for page in pdf.pages:
        rows = page.extract_table()
        header = rows.pop(0)
        for row in rows:
            out['data'].append([r.replace('\n', '') for r in row])
    f.write(json.dumps(out, ensure_ascii=False))
