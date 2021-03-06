# TODO Wczytywanie pliku .net poprzez tk GUI

import os
import itertools
from datetime import datetime
start = datetime.now()
net_path = os.path.join(r"C:\!Projekty\Lublin_Fabryczna\00. Lublin_model\191106_Lublin_OSM_15.net")
"""new_net_path = net_path.replace("190610_Lublin_OSM_15.net", "190610_Lublin_OSM_15.net")"""
net_file = open(net_path, encoding="utf8")

network_list = []
detector_list = []
for line in net_file:
    network_list.append(line)

index_first = network_list.index("* Table: Detectors\n")
index_last = network_list.index("* Table: Matrix toll\n")

pre_list = network_list[index_first + 2:index_last - 3]

headlines = pre_list[0].rstrip().split(";")
detectors = []
list_detectors_string = []
ln = ''

for det in pre_list[1:]:
    temp_dict = {}
    for key_det, value_det in itertools.zip_longest(headlines, det.rstrip().split(";")):
        temp_dict[key_det] = value_det
    detectors.append(temp_dict)

for det in detectors:
    det['COUNTLOCATIONNO'] = det['CLOC']
    ln = ";".join(det.values())
    ln += "\n"
    list_detectors_string.append(ln)

for idx, det in itertools.zip_longest(range(index_first+3, index_last-1), list_detectors_string):
    network_list[idx] = det

new_net = open(net_path, 'w', encoding="utf8")

for line in network_list:
    if line:
        new_net.write(line)
    else:
        new_net.write('\n')

new_net.close()
print (datetime.now()-start)