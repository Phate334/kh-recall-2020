import re
import json
from datetime import datetime

import pdfplumber

WHOLE_NBH = '全里'
WHOLE_NBH_CODE = 'all'
REGEX_NBH = r'(\d{1,2})-?(\d{1,2})?'

out = {
    'name': '高雄市第3屆市長罷免案投開票所設置地點一覽表',
    'datetime': '1589205495',
    'header': ['id', 'name', 'address', 'village', 'neighborhood', 'neighborhood_extend'],
    'polling_place': []
}

# cleaned neighborhood data
def extend_neighborhood(nbh: str)->list:
    if nbh == WHOLE_NBH:
        return WHOLE_NBH_CODE
    result = []
    for n in nbh.split(','):
        match = re.match(REGEX_NBH, n)
        if match:
            if match.group(1) and match.group(2):
                for neighborhood in range(int(match.group(1)), int(match.group(2))+1):
                    result.append(neighborhood)
            else:
                result.append(int(match.group(1)))
    return result


# parsing raw data
with pdfplumber.open('090511.pdf') as pdf, open('data.json', 'w', encoding='utf-8') as f:
    for page in pdf.pages:
        rows = page.extract_table()
        header = rows.pop(0)
        for row in rows:
            raw_data = [r.replace('\n', '') for r in row]
            del raw_data[-1]  # remove remark
            raw_data.append(extend_neighborhood(raw_data[4]))
            out['polling_place'].append(raw_data)
    f.write(json.dumps(out, ensure_ascii=False))
