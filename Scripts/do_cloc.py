# TODO Wczytywanie pliku .net

import os
import itertools
from datetime import datetime
start=datetime.now()

folder = os.path.join("C:\\", "Desktop", "cloc", "siec.net" )
new_folder = folder.replace("siec.net", "new_siec.net")
net_file = open(folder, encoding="utf8")

network_list = []
detector_list = []
for line in net_file:
    network_list.append(line)

# TODO Wczytanie zawartości tabeli Detectors

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

# TODO Podmiana wartości CLOC

for det in detectors:
    det['COUNTLOCATIONNO'] = det['CLOC']
    ln = ";".join(det.values())
    ln += "\n"
    list_detectors_string.append(ln)

for idx, det in itertools.zip_longest(range(index_first+3, index_last-1), list_detectors_string):
    network_list[idx] = det

# TODO Wklejenie do pliku

new_net = open(new_folder, 'w', encoding="utf8")

for line in network_list:
    if line:
        new_net.write(line)
    else:
        new_net.write('\n')

# TODO Zapisanie zmian

new_net.close()
print (datetime.now()-start)