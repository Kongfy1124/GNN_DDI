import json
import numpy as np


num = 10

with open("/root/autodl-tmp/datasets/valid.json") as f:
    json_dict = json.load(f)

size = len(json_dict)
out_index = np.random.randint(0, size, num)
out = []
for i in out_index:
    json_data = json_dict[i]
    out.append(json_data)

with open("/root/autodl-tmp/datasets/100_valis.json", 'w') as f:
    json.dump(out, f, indent=4)


pass
