import requests
import os
from os.path import isfile, join

MISTRAL_URL = "http://mistral-chom-2.sdnoshm05.netcracker.com"
workflow_root_path = "D:\git\workflow-service_mapping_5_mistral\mistral\workflow"

file_names = []
for path in os.walk(workflow_root_path):
    for file_name in path[2]:
        file_names.append(join(path[0], file_name))

for file_name in file_names:
    with open(file_name, "r") as f:
        content = "".join(f.readlines())
        print(content)
        resp = requests.post(u"%s/v2/workflows" % MISTRAL_URL, data=content)
        print(resp)
